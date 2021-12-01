#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#define fun system("python 1.py")
int main(int argc, char *argv[]) {
  while (1) {
	  system("python test.py run");
	  sleep(24*60*60);
  }
  return 0;
}
