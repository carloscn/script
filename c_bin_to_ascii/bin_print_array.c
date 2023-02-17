#include <fcntl.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <string.h>

int main(int argc, char* argv[]) {

    size_t i = 0, k = 0;
    ssize_t r_sz = 0, w_sz = 0;
    ssize_t file_size = 0;
    char pbuf[10] = {0};
    char buffer_line[1024] = {0};

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

    stat(argv[1], &statbuf);
    file_size = statbuf.st_size;

    if (!in || !out) {
      perror("[ERR] open file failed");
      return -1;
    }

    printf("[INFO] Write the value to %s.", argv[2]);
    k = 0;
	sprintf(buffer_line, "uint8_t temp_array[] = {\n    ");
    fwrite(buffer_line, strlen(buffer_line), 1, out);
    for(i = 0; i < file_size; i ++) {
        k ++;
        r_sz = fread(buffer, 1, 1, in);
        sprintf(pbuf, "0x%02x", buffer[0] & 0xFF);
        fwrite(pbuf,strlen(pbuf), 1, out);
        if(k != 16)
            fwrite(", ",strlen(", "), 1, out);
        else
            fwrite(",",strlen(","), 1, out);
        if(k == 16) {
            k = 0;
            sprintf(buffer_line, "\n    ");
            fwrite(buffer_line, strlen(buffer_line), 1, out);
        }
    }
    fseek(out, 0, SEEK_END);
    if(k == 0)
        fwrite("};",strlen("};"), 1, out);
    else
        fwrite("\n};",strlen("\n};"), 1, out);

    printf("\n");
    printf("[INFO] binary file %s converted ASCII file %s\n", argv[1], argv[2]);
    printf("[INFO] Success!\n");

finish:
    fclose(in);
    fclose(out);
    return 0;
}
