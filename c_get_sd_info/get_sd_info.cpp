#include <iostream>
#include <fcntl.h>
#include <stdint.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <linux/fs.h>

#define INPUT_SD argv[1]

int main(int argc, char** argv)
{
    size_t i = 0;
    int32_t ret = 0;
    uint64_t size = 0;
    uint64_t sd_size = 0;
    int32_t fd = 0;
    char model_name[50] = {0};
    char dev_name[150] = {0};

    if (argc != 2) {
        std::cout << "input error, argc = " << argc << std::endl;
    	return -1;
    }

    sprintf(dev_name, "/dev/%s", INPUT_SD);
    fd = open(dev_name, O_RDONLY);
    if (fd < 0) {
        std::cout << "Open " << dev_name  << " error!" << std::endl;
    	return fd;
    }

    ret = ioctl(fd, BLKGETSIZE64, &sd_size);
    if (ret < 0) {
        std::cout << "Ioctl error" << std::endl;
        close(fd);
	    return ret;
    }
    close(fd);

    sprintf(dev_name, "/sys/block/%s/device/model", INPUT_SD);
    fd = open(dev_name, O_RDONLY);
    if (fd < 0) {
        std::cout << "Open " << dev_name  << " error!" << std::endl;
    	return fd;
    }
    while (1) {
	    size = read(fd, model_name + i, 1);
        if (!((1 == size) || (0 == size))) {
            close(fd);
            std::cout << "Read " << dev_name  << " error!" << std::endl;
            return -1;
        }
        if (EOF == *(model_name + i)) {
            *(model_name + i) = '\0';
            break;
        }
        i ++;
    }
    close(fd);

    sprintf(dev_name, "/dev/%s:%0.2f GiB, %s", INPUT_SD,
                      (double) ((sd_size >> 20) / 1024.0),
                      model_name);
    std::cout << dev_name << std::endl; // MiBytes

    return ret;
}
