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

