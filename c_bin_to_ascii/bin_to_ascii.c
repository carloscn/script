#include <fcntl.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>

int main(int argc, char* argv[]) {

    size_t i = 0;
    ssize_t r_sz = 0, w_sz = 0;
    ssize_t file_size = 0;

    printf("[INFO] This is the tool for converting BIN to ASCII file\n");

    if (argc < 3 || argv[1] == NULL || argv[2] == NULL) {
        printf(
            "[ERR] error input, example: $ bin_to_ascii.elf ./digest.bin "
            "./digest.txt\n");
        return -1;
    }

    struct stat statbuf;
    FILE* in = fopen(argv[1], "r");
    FILE* out = fopen(argv[2], "w+");
    char buffer[2] = {0};
    char w_buf[3] = {0};

    stat(argv[1], &statbuf);
    file_size = statbuf.st_size;

    if (!in || !out) {
      perror("[ERR] open file failed");
      return -1;
    }

    printf("[INFO] Write the value to %s :\n                  ", argv[2]);
    for (i = 0; i < file_size; i ++) {
        r_sz = fread(buffer, 1, 1, in);
        sprintf(w_buf, "%02x", buffer[0]&0xFF);
        printf("%02x", buffer[0]&0xFF);
        w_sz = fputs(w_buf, out);
    }
    printf("\n");
    printf("[INFO] binary file %s converted ASCII file %s\n", argv[1], argv[2]);
    printf("[INFO] Success!\n");

finish:
    fclose(in);
    fclose(out);
    return 0;
}
