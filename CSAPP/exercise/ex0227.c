/* Determine whether arguments can be add without overflow */
int uadd_ok(unsigned x, unsigned y):
   return (x + y) < x;
