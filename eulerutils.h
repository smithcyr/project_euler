long unsigned int luisqrt(long unsigned int n){
  long unsigned int a;
  for (a=0;n>=(2*a)+1;n-=(2*a++)+1);
  return a;
}

int isprime(long unsigned int num){
  long unsigned int x;
  long unsigned int max = luisqrt( num);
  if (max*max == num) return 0;
  for(x=2;x<=max;x++) if(!(num%x)) return 0;
  return 1;
}
