#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int ***matrix3d(){
  int i, j, k;
  int ***matrix;
  matrix = malloc(sizeof(int***) * 3);

  for(i = 0; i < 3; i++) {
      matrix[i] = malloc(sizeof(int**) * 3);
       for(j = 0; j < 3; j++) {
          matrix[i][j] = malloc(sizeof(int*) * 3);
      }
  }

  for(i = 0; i < 3; i++){
      for(j = 0; j < 3; j++){
          for(k = 0; k < 3; k++){
              matrix[i][j][k] = 0;

          }
      }
  }
  return matrix;
}


int **matrix2d(){
  
}



int main(){
  return 0;
}
