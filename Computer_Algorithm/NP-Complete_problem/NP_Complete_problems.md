# Ch14: NP_Complete Problems
## 00. Graph Coloring
## Definition 13.1 Graph coloring and chromatic number
그래프 G = (V, E)를 coloring하는 것은 V를 유한 집합 S(colors)로 매핑하는 것이다. 따라서, 만약 edge vw가 E의 원소이면 C(v) != C(w) 이다.
> 인접한 두 노드의 색깔은 다르다.

G의 chromatic number는 $ \chi(G)$ 라고 표기하며 이는 그래프 G를 칠하는데 필요한 최소한의 색깔 수이다. 즉, G를 칠하는 coloring C의 수가 k이면 |C(V)| = k이다.

### Problem 13.1 Graph coloring
방향이 없는 그래프 G = (V, E)를 칠한다고 가정하자.
Optimization Problem: G가 주어졌을 때 $\chi(G)$ 를 구하라.
Decision Problem: 그래프 G, 양의 정수 k가 주어졌을 때 k개 색깔 이내로 G를 칠할 수 있는가?

### Algorithm 13.3 Sequential Coloring(SC)
Input: G = (V, E), 방향이 없는 그래프, V = $ v_1,..., v_n$
Output: G를 칠하는 색의 수
```C++
void seqColor(V, E){
    int c, i;
    for (int i = 1; i <= n; i++){
        for (int c = 1; c <= n; c++){
            if no vertex adjacent to vi has color c:
                Color vi with c
                break
            Continue for (c)
        Continue for (c)
        }
    }
}
```

### Problem 13.1 Graph coloring
graph color 문제는 스케줄링의 특정 형태의 추상화이다.

## 01. Job scheduling
### Problem 13.2 Job scheduling with penalties
Jobs: $J_1, J_2, ..., J_n$
Execution times: $t_1, t_2, ..., t_n$
Deadlines: $d_1, d_2, ..., d_n$
Penalties: $p_1, p_2, ..., p_n$

job에 대한 스케줄은 $J_1, J_2, ..., J_n$에 대한 순열문제이다.

$P_j = P_{\pi(j)}$ if job $J_{\pi(j)}$가 deadline $d_{\pi(j)}$ 을 넘겨서 끝마친 경우
$P_j = 0$ 데드라인 전에 끝마친 경우

따라서 특정 스케줄에 대한 패널티의 합은 다음과 같다.
$P_\pi = \sum P_j$

Optimization Problem: 패널티가 최소가 되게 하라.

## 02. Bin packing
가방의 용량이 1이고, 용량이 0~1인 물건 n개가 있다고 할 때 가방을 최소로 써서 물건 n개를 넣는 방법

Optimization Problem: object가 모두 들어가는데 필요한 최소한의 가방의 수를 구하라

![bin](image/bin.PNG)
위 방법은 first fit decreasing 방법으로, 용량이 큰 물건부터 차례대로 들어갈 수 있는 곳에 넣는 방법이다. optimal한 방법은 아니다.

## 03.Knapsack Problem
### Problem 13.4 Knapsack
용량이 C인 배낭과 사이즈가 $s_1, ..., s_n$ 인 n개의 object와 각각의 이익이 $p_1, p_2, ..., p_n$ 이라고 하자.

Optimization Problem: 배낭에 물건을 넣었을 때 이익이 최대가 되는 부분집합을 구하여라.

### Problem 13.5 Subset sum
입력값이 양의 정수 C, 사이즈가 양의 정수 $s_1, ..., s_n$ 인 n개의 object일 때
Optimization Problem: 최대 합이 C인 물체의 부분 집합 중에서, 가장 큰 부분 집합의 합은 무엇인가?

### Problem 13.6 Satisfiability
propositional variable: 불리언 변수
literal: 불리언 변수이거나 불리언 변수의 negation
conjunctive normal form: propositional formular의 정규 형태
clause: literal과 operator(and, or, not)로 이루어진 식이다.
