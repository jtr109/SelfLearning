//
//  main.c
//  prog15_2
//
//  Created by liyuanpei on 16/4/28.
//  Copyright © 2016年 jtr109. All rights reserved.
//

#include <stdio.h>

int main()
{
    float d = 6.5;
    float half, square, cube;
    
    half = d / 2;
    square = d * d;
    cube = d * d * d;
    
    printf("\nYour number is %.2f\n", d);
    printf("Half of it is %.2f\n", half);
    printf("Square it to get %.2f\n", square);
    printf("Cube it to get %.2f\n", cube);
    
    return 0;
}