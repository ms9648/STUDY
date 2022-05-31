# Processes and Threads

## The Process Model
하나의 프로세스는 실행중인 프로그램의 인스턴스로서 프로그램 카운터의 현재 값, 레지스터, 변수들을 포함한다. 물리적인 프로그램 카운터는 하나만 존재하므로 각 프로세스가 실행될 때 논리적인 프로그램 카운터는 실제 프로그램 카운터로 적재되어야 한다. 프로세스가 잠시 실행을 멈추면 물리적인 프로그램 카운터는 메모리에 있는 프로세스의 논리적인 프로그램 카운터 저장소에 저장되어야 한다. 

![Chap2_Trace_of_Processes](Chap2_Trace_of_Processes.PNG)
프로세스 실행 중 인터럽트 요청이 들어오면 인터럽트 주소로 가서 실행하고 끝날 때는 스케줄러에 의해 다음에 실행할 프로세스를 결정하여 해당 주소부터 수행한다.

## Process Creation
프로세서의 생성을 유발하는 네 가지 주요 이벤트
1. 시스템 초기화
2. 실행중인 프로세스가 프로세스 생성 시스템 호출(fork)을 부르는 경우
3. 사용자가 새로운 프로세스를 생성하도록 요청하는 경우
4. 배치 작업의 시작

## Process Termination
프로세스 종료를 유발하는 네 가지 주요 이벤트
1. 정상적인 종료(자발적)
2. 오류 종료(자발적)
3. 치명적인 오류(비자발적)
4. 다른 프로세스에 의해 종료(비자발적)

## Process States
![Chap2_Process_state](Chap2_Process_state.PNG)
1. Running -> Blocked: 논리적으로 프로세스가 수행을 계속할 수 없는 경우(프로세스 수행에 필요한 자원이 없는 경우)
2. Running -> Ready: 운영체제가 잠시 CPU를 다른 프로세스에 할당하기로 결정한 경우
3. Ready -> Running: 운영체제가 해당 프로세스에 CPU를 할당한 경우
4. Blocked -> Ready: 프로세스가 기다리던 외부 이벤트가 발생했을 경우(프로세스 수행에 필요한 자원이 할당된 경우), CPU가 이용 가능해질 때까지 Ready상태에서 기다렸다가 실행한다.

![Chap2_Queues_for_Scheduling](Chap2_Queues_for_Scheduling.PNG)
dispatcher(스케줄러)에 의해 Ready Queue의 프로세스가 프로세서에서 실행된다. 타임아웃의 경우 해당 프로세스는 다시 Ready Queue에 적재되고 스케줄러는 Ready Queue의 다른 프로세스를 실행한다. 프로세스가 어떤 외부 이벤트를 기다리는 경우 Event Queue라고 하는 Block Queue에 들어가서 외부 이벤트 발생을 기다린다. 이 상태를 blocked 상태라고 한다. 외부 이벤트가 발생하면 Ready Queue로 들어간다.

### Suspend State
![Chap2_Two_Suspend_State](Chap2_Two_Suspend_State.PNG)
New -> Ready: 새 프로세스가 생성되면 Ready상태로 실행을 기다린다.
New -> Ready/Suspend: 시스템 설계마다 다르나, 새 프로세스가 생성되어서 Ready Suspend에서 기다렸다가 메인메모리의 상태가 괜찮으면 activate 시켜서 ready상태로 전환한다. 
Ready -> Ready/Suspend: ready상태의 프로세스 중 우선순위가 상대적으로 낮은 프로세스는 Ready/Suspend로 잠시 빼두어 메인메모리를 알맞게 유지한다.
Ready -> Running: 스케줄러에 의해 선택되면 프로세스를 수행한다.
Running -> Ready/Suspend: 실행 중인 프로세스가 뭔가 문제를 일으킬 것 같다고 판단되면 Ready/Suspend 상태로 전이시킨다.
Running -> Exit: 프로세스 수행을 종료한다.
Running -> Ready: 프로세스가 타임아웃 인터럽트가 발생하면 타이머 인터럽트 명령 수행 후 ready 큐로 들어간다.
Running -> Blocked: 실행 중 외부 이벤트의 발생으로부터의 입력 값이 필요하면 Block queue에 들어간다.
Blocked -> Ready: 외부 이벤트가 발생하여 자원이 할당되면 ready 큐에 들어간다.
Blocked -> Blocked/Suspend: Block queue에 외부 이벤트를 기다리는 프로세스가 너무 많으면 blocked/suspend 상태로 전이시켜 메모리를 유지한다.
Blocked/Suspend -> Ready/Suspend: Blocked/suspend 상태에서 외부 이벤트가 발생하면 Ready/suspend상태로 전이한다.

## Implementation of Processes
![Chap2_Process_Table_Entry](Chap2_Process_Table_Entry.PNG)
프로세스 모델을 구현하기 위해서 운영체제는 프로세스 테이블이라 불리는 각 프로세스마다 하나의 엔트리가 존재하는 테이블을 유지한다. 엔트리는 프로세스 상태에 대한 중요한 정보들을 가진다. 프로세스는 실행 상태에서 준비 또는 대기 상태로 전환될 때 이러한 엔트리 정보를 저장해야 다음 실행 때 재시작할 수 있다. 엔트리는 Process management(CPU 정보), Memory management(메모리 정보), File management(파일 정보)를 가진다.

![Chap2_Interrupt_Step](Chap2_Interrupt_Step.PNG)
모든 인터럽트 처리는 보통 현재 프로세스의 프로세스 테이블 엔트리에 레지스터들을 저장하는 것부터 시작한다. 
1. 하드웨어는 Program counter를 스택에 저장한다.
2. 하드웨어는 인터럽트 벡터라 불리는 메모리의 하나의 위치로부터 인터럽트 서비스 프로시저의 주소를 받아온다.
3. 어셈블리어 프로시저는 레지스터를 저장한다.
4. 새 스택을 설정한다.
5. C 인터럽트 서비스를 실행시킨다.
6. 스케줄러는 다음에 실행될 프로세스를 결정한다.
7. C 프로시저는 어셈블리 코드로 다시 제어를 넘긴다.
8. 어셈블리어 프로시저는 새로운 프로세스를 실행시킨다.

## Modeling Multiprogramming
![Chap2_CPU_Utilization](Chap2_CPU_Utilization.PNG)
일반적으로 CPU 이용률은 다음과 같은 식을 따른다.
CPU 이용률 = 1 - p^n

여기서 n은 I/O를 기다리는 확률이다. 따라서, 만약 프로세스가 자신의 시잔 중 80% 정도를 I/O를 기다리면서 보낸다면 적어도 10개의 프로세스가 메모리에 적재되어 있어야 CPU낭비를 10%이하로 줄일 수 있다.

## Thread
스레드를 사용해야 하는 주된 이유는 많은 응용에서 다수의 동작이 동시에 진행되기 때문이다. 준 병렬로 수행하는 다수의 순차적인 스레드로 분해하면 프로그래밍 모델이 훨씬 단순해진다.

스레드를 사용하여 새로운 요소를 하나 더 추가하면 이 요소는 주소 공간을 공유하여 실행의 흐름들 간에 모든 데이터를 공유하는 병렬로 수행하는 개체를 지원하는 능력이다. 
스레드는 프로세스보다 더 경량이어서 프로세스보다 생성과 제거가 쉽고 빠르다.
CPU-바운드의 경우 프로세스와 차이가 별로 없지만 I/O가 동시에 존재하는 경우 스레드는 I/O동작을 겹치도록 수행할 수 있어 응용의 속도를 향상시킬 수 있다.
스레드는 다수의 CPU를 가지는 시스템에서 유용하다.

![Chap2_Web_Server_Multithread](Chap2_Web_Server_Multithread.PNG)
Dispatcher는 메인스레드로, 네트워크로부터 도착하는 작업 요청을 읽어 들인다. 그 후, 작업 스레드(Worker thread)를 선정하고 각 스레드마다 지정된 위치의 워드에 메시지의 포인터를 기록함으로써 요청을 이 스레드에 전달한다. 디스패처는 잠들어 있던 작업 스레드를 꺠워 이 스레드가 대기 상태에서 준비 상태가 되도록 한다.
작업 스레드가 깨어나면 이 작업 스레드는는 작업 요청이 웹페이지 캐시에서 만족될 수 있는지를 검사한다. 만약 그렇지 않으면 스레드는 디스크 읽기 연산을 시작하고 디스크 동작이 완료될 때까지 대기 상태가된다. 
디스패처 프로그램은 작업 스레드를 선정하고 작업 스레드에게 요청을 전달하는 무한 루프로 구성된다. 각 작업 스레드 코드는 디스패처로부터 요청을 전달 받고 웹 캐시에서 해당 페이지가 존재하는지 검사하는 무한 루프로 구성된다.

```C++
// 웹 서버 스레드

// 디스패처 스레드
while (TRUE){
    get_next_request(&buf); // 다음 요청을 받는다.
    handoff_work(&buf); // 작업스레드에 요청을 전달한다.
}

// 작업 스레드
while (TRUE){
    wait_for_work(&buf); // 요청을 기다린다.
    look_for_page_in_cache(&buf, &page); // 캐시에 페이지가 존재하는지 확인한다.
    if (page_not_in_cache(&page)) // 캐시에 페이지가 존재하지 않으면
        read_page_from_disk(&buf, &page); // 디스크로 부터 읽기 연산을 하고 대기상태로 들어간다.
    return_page(&page); // 페이지를 반환한다.
}
```

### Three ways to construct a server
![Chap2_Way_To_Constructing_Server](Chap2_Way_To_Constructing_Server.PNG)

## The Classical Thread Model
![Chap2_Classical_Thread_Model](Chap2_Classical_Thread_Model.PNG)
스레드: PC(Program Counter), 현재 작업 변수를 저장하는 레지스터, 실행 히스토리를 담고있는 스택을 가진다.

(a)의 경우 각 스레드는 서로 다른 주소 공간에서 동작하는 반면 (b)의 경우 세 스레드 모두 동일한 주소 공간을 공유한다.
다중스레드 프로세스가 하나의 CPU를 가진 시스템에서 실행될 때 스레드는 순서대로 수행된다. 한 프로세스 내부의 서로 다른 스레드들은 완전히 동일한 주소 공간을 가지며 동일한 전역 변수를 공유한다. 스레드는 다른 스레드의 스택을 읽고, 기록하고, 지워버릴 수 있다.

![Chap2_Process_Thread_item](Chap2_Process_Thread_item.PNG)
스레드는 다른 스레드가 작업중인 파일을 볼 수 있으므로 프로세스가 자원 관리의 단위가 되어야한다. 따라서, 스레드는 PC, Register, Stack, State만 가진다.
스레드는 Running, Blocked, Ready, Terminate의 상태를 가진다. 
스레드는 자신만의 스택을 가지고 있으며, 스택에는 호출되었으나 아직 복귀하지 않은 프로시저당 하나의 프레임이 존재한다. 이 프레임은 프로시저의 지역 변수들과 프로시저 수행이 끝날 때 돌아갈 복귀 주소를 가지고 있다. 
예를 들어 프로시저 a가 프로시저 b를 호출하고 b가 c를 호출했으면 a, b, c의 프레임들이 스택에 존재한다. 
일반적으로 각 스레드는 서로 다른 프로시저들을 호출하며 따라서 서로 다른 실행 히스토리를 가진다. 따라서 각 스레드들은 각자 자신의 스택을 가져야 한다.

## POSIX Thread
이식 가능한 스레드 프로그램(POSIX Thread)
![Chap2_Pthread_function](Chap2_Pthread_function.PNG)
Pthread_create: 새로운 스레드를 생성한다. 새로 생성된 스레드에 대한 식별자가 함수의 값으로 반환된다. 스레드 식별자는 PID와 동일한 역할을 가지며 다른 호출에서 스레드를 지정하고 식별하는 역할을 수행한다.
Pthread_exit: 스레드가 지시된 작업을 마치면 이 함수를 호출하여 종료한다. 스레드를 종료시키고 스레드의 스택을 반환한다.
Pthread_join: 다른 스레드가 종료할 때까지 기다린다. 기다릴 대상 스레드의 식별자가 인자로 주어진다.
Pthread_yield: 다른 스레드에게 수행 권리를 양보한다.
Pthread_attr_init: 스레드와 관련된 속성 구조체를 생성하고 필드들을 기본 값으로 설정한다.
Pthread_attr_destory: 스레드의 속성 구조체를 파괴하여 메모리를 반환한다. 이 호출은 이 속성을 현재 사용하고 있는 스레드들에게는 그대로 존재하도록 하여 영향을 미치지 않는다.

### An example program using threads
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

## Implementing Threads
스레드 패키지를 구현하는 주요 방법으로는 두 가지가 있는데 하나는 사용자 공간에서 하나는 커널 내에서 구현하는 것이다.
둘을 혼합하면 하이브리드 방법이 된다.

![Chap2_Implementing_Thread](Chap2_Implementing_Thread.PNG)
(a)는 스레드 패키지 전체를 사용자 공간에 위치시키는 것이다. 커널은 이들에 대해 전혀 알지 못한다. 커널이 나는 것은 단지 자신이 평범한 단일 스레드 프로세스를 수행하고 있다는 점이다. 이는 스레드를 전혀 지원하지 않은 운영체제에서도 구현될 수 있다는 장점이 있다. 스레드는 런타임 시스템 상에서 수행되며 런타임 시스템은 스레드를 관리하는 프로시저들의 모음이다.
스레드가 사용자 공간에서 관리되면 프로세스는 프로세스 내 모든 스레드를 관리하기 위해 각자의 스레드 테이블을 가져야 한다. 스레드 테이블은 런타임 시스템에 의해 관리된다. 스레드가 실행 상태에서 준비 또는 대기 상태로 전환되면 재시작하기위해 필요한 정보들은 스레드 테이블에 저장된다.
스레드를 대기 상태로 만들지도 모르는 어떤 작업을 수행할 경우 스레드는 런타임 프로시저를 호출한다. 이 프로시저는 스레드가 대기 상태가 되어야하는지를 검사하고 대기 상태로 들어가야 한다면 스레드의 레지스터를 스레드 테이블에 저장하고 실행 가능한 ready상태 스레드를 테이블에서 검색한 다음 이 새로운 스레드의 저장된 값들을 CPU의 레지스터로 적재한다.
이와 같은 스레드 전환은 인터럽트를 통해 커널 내부로 들어가는 것과 비교했을 때 매우 빠르다.
사용자 레벨 스레드는 각 프로세스마다 자신에게 특화된 스케줄링 알고리즘을 가질 수 있도록 한다.

(b)는 커널 내부에서 스레드를 구현한 것이다. 이는 프로세스마다 런타임 시스템이 필요하지 않다. 또, 각 프로세스마다 스레드 테이블이 존재하지 않는다. 대신 커널은 시스템 내부의 모든 스레드를 관리하기 위하여 스레드 테이블을 가진다. 스레드가 다른 스레드 생성을 요구하거나 기존 스레드의 제거를 요구하면 커널 호출을 통해 커널 스레드 테이블을 변경하여 생성과 삭제를 수행한다. 

![Chap2_Hybrid_Thread](Chap2_Hybrid_Thread.PNG)
커널 레벨 스레드를 사용하고 커널 스레드 상에서 사용자 레벨 스레드를 다중화 시키는 것이다. 커널은 단지 커널 레벨 스레드들만을 인식하고 이들을 스케줄한다. 이 커널 스레드 중 일부는 그 위에서 다수의 사용자 레벨 스레드를 다중화 시킨다. 

## Pop-Up Threads
![Chap2_Popup_thread](Chap2_Popup_thread.PNG)
서비스 요청 메시지가 도착하면 시스템은 이를 처리하는 새로운 스레드를 생성하는데 이를 팝업 스레드라고 한다. 이는 완전히 새로 만들어진 것이라서 복원할 정보가 없다.

## Making Single-Threaded Code Multithreaded
단일 스레드 코드를 다중스레드 형태로 만들려면 몇 가지 위험 사항이 있다.
1. 스레드에게는 전역이면서 전체 프로그램 입장에서는 전역이 아닌 변수가 문제가 될 수 있다.
![Chap2_problem_global_variable](Chap2_problem_global_variable.PNG)
한 가지 예로 UNIX에서 프로세스는 시스템 호출을 부를 때 호출이 실패하는 경우 오류 코드가 errno에 기록된다. 위 그림에서 Thread 1은 특정 파일을 접근할 수 있는 권한이 있는지 알아보기 위해 access 시스템 호출을 실행한다. 운영체제는 전역 변수 errno에 응답을 적어 복귀한다. 제어가 Thread 1로 넘어왔지만 errno를 읽어보기 직전에 스케줄러는 Thread 1이 충분한 CPU 시간을 사용했다고 판단해서 Thread 2로의 문맥 교환을 결정한다. Thread 2는 open 시스템 호출을 부르지만 실패하여 errno 값이 다시 기록되고 결국 Thread 1의 access 호출로 인한 errno 값은 사라진다. 나중에 Thread 1이 실행될 때 이 스레드는 잘못된 값을 읽어 정확하게 행동할 수 없다.

![Chap2_private_global_variables](Chap2_private_global_variables.PNG)
이를 해결하는 방법은 각 스레드에게 자신만의 개별 전역 변수를 할당하는 것이다. 이런 방식은 개별적으로 다른 전역 변수의 복사본을 가지게 되어 충돌을 피할 수 있다.

## Inter Process Condition
몇몇 운영체제에서 협력하는 프로세스들은 종종 각 프로세스가 읽고 쓸 수 있는 저장 공간을 공유한다. 스풀러 디렉터리(공유 메모리)는 번호로 색인되며 이름을 저장하는 다수의 슬롯을 가지고 있다. 두 프로세스가 하나의 슬롯에 접근하려고 할 때 문제가 발생한다. 이 때 두 프로세스는 공유 데이터를 읽거나 기록하는데 최종 결과는 누가 언제 수행되는가에 따라 달라지는 상황을 경쟁 조건(race condition)이라 부른다.

## Critical Regions
경쟁조건은 회피하기 위해서는 한 프로세스가 공유 변수나 파일을 사용중이면 다른 프로세스들은 똑같은 일을 수행하지 못하도록 해야한다. 이를 상호 배제(mutual exclusion)이라고 한다. 공유 메모리를 접근하는 프로그램 부분을 임계구역이라 한다. 만약 두 프로세스가 동시에 임계구역에 존재하지 않도록 조절한다면 경쟁조건을 피할 수 있다. 경쟁조건을 피하려면 다음 4가지 조건을 모두 만족해야 한다.
1. 두 프로세스가 동시에 자신의 임계구역에 존재하는 경우는 없어야 한다.(Mutual Exclusion)
2. CPU의 개수나 속도에 대해 어떤 가정도 하지 않는다.
3. 임계구역 외부에서 실행하고 있는 프로세스는 다른 프로세스들을 블록시켜서는 안된다.(Progress)
4. 임계구역에 진입하기 위해 무한히 기다리는 프로세스는 없어야 한다.(Bounded Waiting)

![Chap2_mutual_exclusion](Chap2_mutual_exclusion.PNG)
위 그림처럼 프로세스 A가 시간 T1에 자신의 임계 구역에 진입할 경우 프로세스가 시간 T2에 임계구역에 진입하려고 해도 A는 T3에 임계구역에서 나오기 때문에 B는 T3까지 기다렸다가 임계구역에 진입한다.