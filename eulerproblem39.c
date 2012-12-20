/* Cyrus Smith (https://github.com/smithcyr/project_euler)
 * 
 * http://projecteuler.net/problem=33
 * */
#include <stdio.h>

int main(){
  int p; int x; int y; int count; int max = 0; int maxnum;
  for(p=3;p<=1000;p++){ 
    count = 0;
    for(x=1;x<p-1;x++)
      for(y=1;y<(p-x)/2;y++)
        if(x*x == y*y + (p-x-y-1)*(p-x-y-1)) 
          count++;
    if(count > max){ 
      max = count; 
      maxnum = p-1;
    }
  }
  printf("Perimeter under 1000 that has the most right triangle integer solutions: %d\n",maxnum);
}
