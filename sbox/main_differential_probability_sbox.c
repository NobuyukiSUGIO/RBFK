#include<stdio.h>
#include <stdlib.h>
#include<time.h>
typedef unsigned char u8;
typedef unsigned short u16;
typedef unsigned int u32;

main(void) {
    u16 x, dx,dy;
    u16 S_RBFK[16] = { 0xA,0xE,0xD,0xC,0xB,0xF,0x9,0x8,0x7,0x6,0x0,0x4,0x3,0x2,0x1,0x5 };
    int c=0;
    
    /* Differential probability of S-box */
    /* Input differential : delta_x*/
    for (dx = 0; dx <16; dx++) {
        printf("dx = %x : ", dx);
        /* Output differential : delta_y*/
        for (dy = 0; dy < 16; dy++) {
            /* input 2^4 values */
            for (x = 0; x < 16; x++) {
                if ((S_RBFK[x] ^ S_RBFK[x ^ dx]) == dy) { c += 1; }
            }
            printf("%d,", c);
            c = 0;
        }
        printf("\n");
    }

    return 0;

}