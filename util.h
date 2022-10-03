#include <stdio.h>

int in(char x, char str[], int len){

  for (int i = 0; i<len; i++){
    if (str[i] == x){
      return 1;
    }
  }
  return 0;
}
