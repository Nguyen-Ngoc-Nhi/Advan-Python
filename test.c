#include <unistd.h>
#include <stdio.h>

int main() {
    printf("Main before fork()\n");
    int pid = fork();
    if (pid == 0) printf("pid is ZERO, value is %d\n",pid);
    else printf("pid is NOT ZERO, value is %d\n",pid);
    return 0;
}

