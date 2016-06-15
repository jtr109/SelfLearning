#include <stdio.h>
#include "show-bytes.h"

int main (void)
{
  const char *s = "abcdef";
  show_bytes( (byte_pointer) s, strlen(s) );
}
