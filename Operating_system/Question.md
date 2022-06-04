# 운영체제 공부 중 궁금한 것들

1. pthread_create는 새로 생성된 스레드에 대한 식별자가 함수의 값으로 반환된다고 했는데 여기서 status != 0일 때 에러가 나는 것이라면 스레드에 대한 식별자는 항상 0인가?

```C++
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

#define NUMBER_OF_THREADS 10

void *print_hello_world(void *tid)
{
    /* This function prints the thread's identifier and then exits */
    printf("Hello World. Greetings from thread %d\n", tid);
    pthread_exit(NULL);
}

int main(int argc, char *argv[])
{
    /* This main program creates 10 threads and then exits */
    // 메인 스레드가 10개의 스레드를 생성했으므로 11개의 스레드가 존재한다.
    pthread_t threads[NUMBER_OF_THREADS];
    int status, i;

    for(i = 0; i < NUMBER_OF_THREADS; i++){
        printf("Main here. Creating thread %d\n", i);
        status = pthread_create(&threads[i], NULL, print_hell_world, (void *)i);

        if (status != 0) {
            printf("Oops. pthread_create returned error code %d\n", status)
            exit(-1);
        }
    }
    exit(NULL);
}
```

2. Partitioning에서 Internal fragmentation과 External fragmentation의 차이가 무엇인가?

Answer) Internal fragmentation은 필요한 양보다 더 큰 메모리가 할당되어서 사용하지 않는 메모리 공간이 발생했을 떄를 말하고, External fragmentation은 메모리가 할당이 되고 해제가 되는 작업이 반복될 때 작은 단위의 메모리가 hole처럼 띄엄띄엄 존재하게 되는데, 빈 메모리 공간의 합은 충분히 크지만 실제로 사용할 수 없는 경우를 말한다.

