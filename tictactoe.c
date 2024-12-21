#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

int* range(int start, int stop){
    int size = stop-start;
    if (size<0){
        printf("Error negtive range");
        exit(1);
    }
    int* arr = malloc(size*sizeof(int));
    if (!arr){
        printf("range generation failed");
        exit(1);
    }
    int count = 0;
    for (int i = start; i<stop; i++){
        arr[count] = i;
        count++;
    }
    return arr;
}

void pArr(int *arr,int length){ // just for testing
    for (int i = 0; i<length; i++){
    printf("%d", arr[i]); }
}

bool inArr(int val, int *arr, int length){
    for (int i = 0;i<length;i++ ){
        if (val == arr[i]){
            return true;
        }
    }
    return false;
}
void pboard(char (*board)[3]){
    for (int i = 0; i < 3; i++){
        for (int j = 0; j< 3; j++){
            printf(" %c", board[i][j]);            
        }
    printf("\n");
    }
}

void playerIn(char symbol, char (*board)[3]){
    bool validMove = false;
    int x,y;
    int* validInRange = range(1,4);
    while (!validMove){
        printf("player %c to play enter coords in x y origin is top right", symbol);
        scanf( "%d %d", &x, &y );
        if (!(inArr(x, validInRange, 3)||inArr(y,validInRange, 3))){
            printf("you entered an invalid number");
            continue;
        }
        x--;
        y--;
        if (board[y][x] != '-'){
            printf("spot taken");
            continue;
        }
    }
    free(validInRange);
    validInRange = NULL;
    board[y][x] = symbol;
}

int main(){
    char board[3][3] = {
        {'-','-','-'},
        {'-','-','-'},
        {'-','-','-'},
    };
    playerIn('X', board);
    pboard(board);
}
