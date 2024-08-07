#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <linux/uinput.h>
#include <linux/input.h>
#include <sys/time.h>
#include <signal.h>
#include <time.h>

#define KEY_CUSTOM_PAUSE KEY_PAUSE

static struct uinput_user_dev uinput_dev;
static int uinput_fd = -1;

void cleanup(int signum);
int create_user_uinput(void);
int report_key(unsigned int type, unsigned int keycode, unsigned int value);
void close_uinput(void);
int within_working_hours(void);

int main(int argc, char *argv[])
{
    if (argc < 2) {
        printf("Usage: %s --start <seconds> | --clean\n", argv[0]);
        return -1;
    }

    if (strcmp(argv[1], "--start") == 0) {
        if (argc != 3) {
            printf("Usage: %s --start <seconds>\n", argv[0]);
            return -1;
        }

        int seconds = atoi(argv[2]);
        if (seconds <= 0) {
            printf("Invalid interval: %s\n", argv[2]);
            return -1;
        }

        signal(SIGINT, cleanup); // Setup signal handler for Ctrl+C

        int ret = create_user_uinput();
        if (ret < 0) {
            printf("%s:%d - Failed to create uinput device\n", __func__, __LINE__);
            return -1;
        }
        printf("uinput device created successfully\n");

        while (1) {
            if (within_working_hours()) {
                report_key(EV_KEY, KEY_CUSTOM_PAUSE, 1);
                report_key(EV_KEY, KEY_CUSTOM_PAUSE, 0);
            } else {
                printf("Outside working hours, no key events sent\n");
            }
            sleep(seconds);
        }
    } else if (strcmp(argv[1], "--clean") == 0) {
        close_uinput();
        printf("uinput device closed\n");
    } else {
        printf("Invalid command: %s\n", argv[1]);
        printf("Usage: %s --start <seconds> | --clean\n", argv[0]);
        return -1;
    }

    return 0;
}

int create_user_uinput(void)
{
    int i;
    int ret = 0;

    uinput_fd = open("/dev/uinput", O_RDWR | O_NDELAY);
    if (uinput_fd < 0) {
        printf("%s:%d - Failed to open /dev/uinput\n", __func__, __LINE__);
        return -1;
    }
    printf("/dev/uinput opened successfully\n");

    memset(&uinput_dev, 0, sizeof(struct uinput_user_dev));
    snprintf(uinput_dev.name, UINPUT_MAX_NAME_SIZE, "uinput-custom-dev");
    uinput_dev.id.version = 1;
    uinput_dev.id.bustype = BUS_VIRTUAL;

    ioctl(uinput_fd, UI_SET_EVBIT, EV_SYN);
    ioctl(uinput_fd, UI_SET_EVBIT, EV_KEY);

    for (i = 0; i < 256; i++) {
        ioctl(uinput_fd, UI_SET_KEYBIT, i);
    }
    ioctl(uinput_fd, UI_SET_KEYBIT, KEY_CUSTOM_PAUSE);

    ret = write(uinput_fd, &uinput_dev, sizeof(struct uinput_user_dev));
    if (ret < 0) {
        printf("%s:%d - Failed to write to /dev/uinput\n", __func__, __LINE__);
        return ret;
    }
    printf("uinput device setup written successfully\n");

    ret = ioctl(uinput_fd, UI_DEV_CREATE);
    if (ret < 0) {
        printf("%s:%d - Failed to create uinput device\n", __func__, __LINE__);
        close(uinput_fd);
        return ret;
    }
    printf("uinput device created\n");

    return 0;
}

int report_key(unsigned int type, unsigned int keycode, unsigned int value)
{
    struct input_event key_event;
    int ret;

    if (uinput_fd < 0) {
        printf("%s:%d - uinput_fd is not valid\n", __func__, __LINE__);
        return -1;
    }

    memset(&key_event, 0, sizeof(struct input_event));
    gettimeofday(&key_event.time, NULL);
    key_event.type = type;
    key_event.code = keycode;
    key_event.value = value;
    ret = write(uinput_fd, &key_event, sizeof(struct input_event));
    if (ret < 0) {
        printf("%s:%d - Failed to report key event\n", __func__, __LINE__);
        return ret;
    }
    printf("Reported key event: type=%u, code=%u, value=%u\n", type, keycode, value);

    gettimeofday(&key_event.time, NULL);
    key_event.type = EV_SYN;
    key_event.code = SYN_REPORT;
    key_event.value = 0;
    ret = write(uinput_fd, &key_event, sizeof(struct input_event));
    if (ret < 0) {
        printf("%s:%d - Failed to synchronize event\n", __func__, __LINE__);
        return ret;
    }
    printf("Event synchronized\n");

    return 0;
}

void cleanup(int signum)
{
    close_uinput();
    exit(0);
}

void close_uinput(void)
{
    if (uinput_fd >= 0) {
        ioctl(uinput_fd, UI_DEV_DESTROY);
        close(uinput_fd);
        uinput_fd = -1;
        printf("uinput device closed\n");
    }
}

int within_working_hours(void)
{
    time_t t = time(NULL);
    struct tm *tm_info = localtime(&t);

    int hour = tm_info->tm_hour;
    int minute = tm_info->tm_min;

    // Check if current time is within 09:30 - 12:30 or 14:00 - 19:00
    if ((hour == 9 && minute >= 30) || (hour >= 10 && hour < 12) || (hour == 12 && minute < 30) ||
        (hour >= 14 && hour < 16) || (hour >= 17 && hour < 19) || (hour == 19 && minute == 0)) {
        return 1;
    }

    // Check if current time is within 16:00 - 17:00 (stop reporting)
    if (hour == 16) {
        return 0;
    }

    return 0;
}
