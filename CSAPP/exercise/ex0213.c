#include <stdio.h>

/* Declarations of functions implementing operations bis and bic */
int bis(int x, int m) {
    int ret;
    ret = x | m;
    return ret;
};

int bic(int x, int m) {
    int ret;
    ret = x & (~m);
    return ret;
};

/* Compute x|y using only calls to functions bis and bic */
int bool_or(int x, int y) {
    int result = bis(x, y);
    return result;
};

/* Compute x^y using only calls to functions bis and bic */
int bool_xor(int x, int y) {
    int result = bic ( bis(x, y), bic ( x, bic (x, y)));
    return result;
}

int main (void)
{
    /*
    int bis(int x, int m);
    int bic(int x, int m);
    */

    int x = 3, m = 5;

    printf("%x\n", bool_or(x, m));
    printf("%x\n", bool_xor(x, m));

    return 0;
}
