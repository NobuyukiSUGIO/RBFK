#include<stdio.h>
#include <stdlib.h>
#include<time.h>
typedef unsigned char u8;
typedef unsigned short u16;
typedef unsigned int u32;

main(void) {
    u16 x, gx, gy;
    u16 S_RBFK[16] = { 0xA,0xE,0xD,0xC,0xB,0xF,0x9,0x8,0x7,0x6,0x0,0x4,0x3,0x2,0x1,0x5 };
    int counter = 0, tx,ty,i;

    /* Input mask Gamma_x */
    for (gx = 0; gx < 16; gx++) {
        printf("gx=%x : ", gx);
        /* Output mask Gamma_y */
        for (gy = 0; gy < 16; gy++) {
            /* Input 2^4 values */
            for (x = 0; x < 16; x++) {
                tx = 0; ty = 0;
                for (i = 0; i < 4; i++) {
                    tx ^= ((x & gx) >> i) & 1;
                    ty ^= ((S_RBFK[x] & gy) >> i) & 1;
                }
                if (tx == ty) { counter += 1; }
            }
            printf("%d,", counter-8);
            counter = 0;
        }
        printf("\n");
    }

    return 0;

}