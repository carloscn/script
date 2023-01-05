#include <fcntl.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <sys/stat.h>
#include <sys/types.h>

// gcc strip_padding.c -o strip_padding

int main(int argc, char* argv[]) {
  size_t i = 0;
  ssize_t sz = 0;

  printf("[INFO] This is the strip the NIST SHA3 rsa padding tools\n\n");

  if (argc < 3 || argv[1] == NULL || argv[2] == NULL) {
    printf(
        "[ERR] error input, example: $ strip_padding ./digest.bin "
        "./digest_nopad.bin\n");
    return -1;
  }

  FILE* in = fopen(argv[1], "r");
  FILE* out = fopen(argv[2], "w");

  char dig[48] = {0};

  if (!in || !out) {
    perror("[ERR] open file failed");
    return -1;
  }

  fseek(in, 464, SEEK_CUR);
  sz = fread(dig, 8, 6, in);
  printf("[INFO] read sz = %ld : \nwrite file data: \n", sz);
  for (i = 0; i < 48; i++) {
    if (i % 8 == 0) {
      printf("\n");
    }

    printf("0x%02X, ", (int)dig[i] & 0xFF);
  }
  printf("\n\n");

  fclose(in);
  sz = fwrite(dig, 8, 6, out);
  printf("[INFO] write block count is %ld\n", sz);
  fclose(out);
  return 0;
}
