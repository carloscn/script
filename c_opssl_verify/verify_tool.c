#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <ctype.h>
#include <errno.h>
#include <openssl/ssl.h>

// gen_sign ssk.pen
// verify_tool ssk.pem sign.out hash.out

int crypto_rsa_verify(void *img_hash, uint32_t len, void *rsa_sign,
                      uint32_t rsa_len, char *key_name)
{
    int ret;
    FILE *fp;
    RSA *pub_key;

    /* Open the private Key */
    fp = fopen(key_name, "r");
    if (fp == NULL) {
        printf("Error in file opening %s:\n", key_name);
        return -1;
    }

    pub_key = PEM_read_RSAPublicKey(fp, NULL, NULL, NULL);
    fclose(fp);
    if (pub_key == NULL) {
        printf("Error in key reading %s. (PKCS#1 format should be assigned)\n", key_name);
        printf("You can convert PKCS#8 format pem to PKCS#1 format by : \n\n");
        printf("\t $ openssl rsa -pubin -in %s -RSAPublicKey_out > pkcs1_pubkey.pem\n\n", key_name);
        return -1;
    }
    /* Sign the Image Hash with Private Key */
    ret = RSA_verify(NID_sha256, img_hash, len,
            rsa_sign, rsa_len,
            pub_key);
    if (ret != 1) {
        printf("Error in RSA_verify\n");
        return -1;
    }

    return 0;
}
// ./verfy key sig.out hash.out
int main(int argc, char *argv[])
{
    int ret = 0;
    FILE *fp = NULL;
    size_t read_len = 0;
    unsigned char sig[256] = {0};
    unsigned char hash[32] = {0};

    if (argc < 4) {
        printf("Error input! please input ./verfy_tool pubkey.pem sig.out hash.out\n");
        ret = -1;
        return ret;
    }

    fp = fopen(argv[2], "r");
    if (fp == NULL) {
        printf("Error in file opening signature file %s:\n", argv[2]);
        ret = -1;
        goto finish;
    }

    read_len = fread(sig, 1, 256, fp);
    if (read_len != 256) {
        printf("Error in file read signature file %s. the read len = %zu, exp = %u \n", argv[2], read_len, 256u);
        ret = -1;
        goto finish;
    }

    fclose(fp), fp = NULL;

    fp = fopen(argv[3], "r");
    if (fp == NULL) {
        printf("Error in file opening hash file %s:\n", argv[3]);
        ret = -1;
        goto finish;
    }

    read_len = fread(hash, 1, 32, fp);
    if (read_len != 32) {
        printf("Error in file read hash file %s. the read len = %zu, exp = %u\n", argv[32], read_len, 32u);
        ret = -1;
        goto finish;
    }

    fclose(fp), fp = NULL;

    ret = crypto_rsa_verify(hash, 32, sig, 256, argv[1]);
    if (ret != 0) {
        printf("Error in crypto_rsa_verify\n");
        goto finish;
    }

    printf("Verify Pass by the OpenSSL (RSA_verify). \n");

finish:
    if (fp != NULL) {
        fclose(fp);
    }

    return ret;
}

