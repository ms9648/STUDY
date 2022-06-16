# Ch13: Graph Optimization Problems and Greedy Algorithm
## 00. Prim's Minimum Spanning Tree Algorithm
### Definition and Examples of Minimum Spanning Trees
G = (V, E)에 대한 spanning tree는 G의 모든 정점을 포함하고 있는 트리이다.
가중 그래프 G = (V, E, W)에 대하여 subgraph의 가중치는 subgraph의 edge들의 가중치의 합이다.
가중 그래프 minimum spanning tree(MST)는 최소 가중치를 가진 spanning tree이다.

## 01. Kruskal's Minimum Spanning Tree Algorithm
### An Overview of Kruskal's Algorithm
Kruskal 알고리즘의 일반적인 개요는 다음과 같다. 각 단계에서 그래프의 최소 가중치를 가진 edge를 선택한다. 만약 이 edge를 선택함으로 인해 사이클이 만들어진다면 선택을 취소한다.
현재까지 선택된 edge들은 forest를 구성하지만 하나의 트리일 필요는 없다. 
```python
def kruskalMST(G, n):
    R = E # R is remaining edges
    F = 0 # F is forest edges
    while (R is not empty)
        Remove the lightest edge(vw) from R
        if (vw does not make a cycle in F)
            add vw to F
    return F

```
## 02. Prim's Minimum Spanning Tree Algorithm
### Definition and Examples of Minimum Spanning Trees
Greedy algorithms은 최적화 문제에 대한 알고리즘 이다. 그리디 알고리즘은 각 단계마다 local optimal choice를 하여 그 결과가 global optimal solution이 되도록 희망하는 알고리즘이다.

Tree vertices: 지금까지 구성된 트리내의 정점
Fringe vertices: 트리안에는 없지만 트리내에 속하는 정점 인근에 있는 정점
Unseen vertices: 트리안에도 없고 Fringe vertices도 아닌 정점

### An Overview of Prim's Algorithm
Prim의 알고리즘은 tree vertex의 정점에서 fringe vertex의 정점까지의 최소 가중치 edge를 선택한다.
알고리즘의 일반적인 구조는 다음과 같다.
```python
def primMST(G, n):
    Initialize all vertices an unseen.# 처음은 모두 unseen에 있다.
    Select an arbitrary vertex s to start the tree
    reclassify it as tree
    Reclassify all vertices adjacent to s as fringe
    while there are fringe vertices:
        Select an edge of minimum weight between a tree vertex t and a fringe vertex v
        Reclassify v as tree
        add edge tv to tree
        Reclassify all unseen vertices adjacent to v as fringe
```

### Theorem 4.1
G = (V, E, W)가 connected, weighted graph라고 하자. E'는 E의 부분집합으로, G에 대한 minimum spanning tree $T = (V, E_T)$ 의 edge들의 부분집합이다. V'는 E'에 있는 정점들이다. 만약 xy가 minimum weight을 가진 edge이며 x는 V'에 속하고 y는 V'에 속하지않으면 E'와 xy의 합집합은 minimum spanning tree의 부분집합이 된다.

## 03. Shortest Paths and Dijkstra's Algorithm
### Problem 8.1 Single-source shortest paths
가중 그래프 G = (V, E, W), 근원지 정점 s가 있다고 하자. 문제는 s부터 다음 정점까지의 가장 짧은 거리를 찾는 것이다.

MST알고리즘을 사용하여 s에서 출발해보자. 알고리즘에 의해 선택된 v까지의 경로는 가장 짧은 경로인가?

MST에서 A부터 C까지의 경로를 고려해보자. 그림의 경우 최단거리가 아니다. A, B, C로 가는 경우가 가장 짧다.

### An Overview of Dijkstra's Algorithm
Dijkstra's algorithm은 greedy하다. 항상 가장 가까워보이는 정점으로의 edge를 선택한다. 하지만 이 경우 closest의 의미는 정점 s에 closest가 아닌 트리에 closest하다는 의미이다.

d(s, v)는 s부터 v까지의 경로의 가중치를 의미한다.
Dijkstra's algorithm의 일반적인 구조는 다음과 같다.
```C++
dijkstraSSSP(G, n){
    unseen 집합에서 시작한다.
    특정 정점 s에서 tree를 시작한다. 트리를 재분류한다.
    d(s, s) = 0으로 정의한다.
    s에 인접한 모든 정점을 fringe로 재분류한다.
    
    while there are fringe vertices:
        트리안에 있는 정점 t와 fringe vertex v사이의 edge를 선택하여 d(s, t) + W(tv)가 최소가 되게한다.
        v를 tree vertex로 재분류한다. edge tv를 tree로 추가한다.
        d(s, v) = d(s, t) + W(tv)
        v에 인접한 모든 unseen 정점들을 fringe로 재분류한다.
}
```

후보 edge yz에 대한 d(s, y) + W(yz)가 반복되어 사용될지도 모르기 때문에 한번 계산되면 저장해야 한다. yz가 처음 candidate가 됐을 때 효율적으로 계산하기 위해  트리 내의 y에 대한 d(s, y)도 저장한다. 그러므로 array를 사용해야 한다.