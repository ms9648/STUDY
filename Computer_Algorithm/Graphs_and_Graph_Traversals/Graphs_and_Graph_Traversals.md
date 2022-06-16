# Ch12: Graphs and Graph Traversals
## 00. Definitions and Representations
### A binary relation
Set S = {1, 2, ..., 10}의 원소 x, y에 대하여 x가 y의 인수(x != y)일 때 xRy라고 하며, R을 binary relation(이진 관계)라고 한다. xRy, yRz가 성립하면 xRz도 성립한다.
ex. 2R4, 4R8이면 2R8이다.

### 그래프의 종류
1. Star Network
![star_network](image/star_network.PNG)

2. Ring Network
![ring](image/ring.PNG)

3. Tree Network
![tree](image/tree.PNG)

4. Mesh Network
![mesh](image/mesh.PNG)

5. Torus Network
![Torus](image/Torus.PNG)

6. Hypercude Network
![hypercube](image/hypercube.PNG)

노드의 개수가 n일 때 선의 개수
Star: $n-1$
Ring: $n$
B-tree: $n-1$
Mesh: $2 * \sqrt n * (\sqrt n - 1)$
Torus: $2n$
Hyp.Cube: $n * lg n \over 2 $

### Definition 7.1 Graph, Vertex, Edge
그래프 G는 (V, E) 쌍으로 이루어져 있으며, V는 Vertices로 그래프의 정점들의 집합을 뜻하며, E는 두 정점(V)을 이은 선들의 집합이다.

### Definition 7.3 Subgraph, Complete graph
그래프 G의 subgraph G'은 그래프 G = (V, E)에 대하여 V', E'가 부분집합인 그래프를 뜻한다.

complete graph는 모든 정점 사이에 edge로 연결되어 있는 그래프를 뜻한다.

edge(v, w)에 대하여 각 정점 v, w는 서로 incident 관계에 있다고 한다.

### Definition 7.5 Path in graph
그래프 G = (V, E)에서 정점 v로부터 w까지의 경로(path)는 edge $v_{0}v_{1}, v_{1}v_{2}, ..., v_{k-1}v_{k}$ 의 연속이며, $v=v_0, v_k = w$ 이다. 경로의 길이는 k이다. 정점 v에서 자기 자신으로의 경로의 길이는 0이다. 

### Definition 7.6 Connected, strongly connected
undirected graph에서 정점 v로부터 w까지 연결되어 있으면 connected 되었다고 한다.

directed graph에서 정점 v로부터 w까지의 경로가 존재하고 w에서 v까지 경로가 존재하면 정점 v, w는 strongly connected 되었다고 한다.

### Definition 7.7 Cycle in a graph
a cycle is a graph G = (V, E) like a path $v_0, v_1, v_2, ..., v_k$, with k>=2, except that $v_k = v_0$

만약 cycle이 없으면 그래프는 acyclic 하다고 한다.

### Definition 7.8 Connected component
undirected graph에서 가장 큰 connected subgraph는 connected component라고 한다.

만약 undirected graph가 connected 되어있지 않으면, 그 그래프는 여러 connected components로 나누어져 있는 것이다.

### Definition 7.9 Weighted graph
가중 그래프는 (V, E, W)으로, (V, E)는 그래프이고 W는 가중치이다.

Edge e에 대하여 W(e)는 e의 가중치라고 부른다.

## 01. Graph Representation and Data Structure
### Adjacency Matrix Representation
G = (V, E)에서 n = |V|, m = |E|이고, V = $\{v_1, v_2, ..., v_n \}$ 일 때 G는 n by n 인접행렬로 정의된다.

$$ a_ij = 1 if v_{i}v_{j} in E or a_ij = 0 otherwise $$

만약 G가 가중 그래프라면 가중치는 인접행렬에 정의된다.
$$ a_ij = W(v_{i}v_[j]) if v_{i}v_{j} in E or a_ij = c otherwise $$

### Adjacency Lists Representation
![adjacency_list](image/adjacency_list.PNG)

weighted graph의 경우 다음과 같이 표기한다.
![weighted_adjacency_list](image/weighted_adjacency_list.PNG)

## 02.Directed Acyclic Graphs
A Directed Acyclic Graph(DAG)는 순환하지 않는 방향 그래프이다.

스케줄링 알고리즘이 DAG를 활용하여 접근되어진다.
- CPU scheduling: FCFS(First Come First Service), SJF(Shortest Job Fisrt)
- Real-time scheduling: Siggraph
- Parallel Task scheduling

### Topological Orger
G = (V, E)가 n개의 정점을 가진 방향그래프라고 하자.
그래프 G에 대한 topological order는 각각의 정수 1, ..., n을 정점 V들에 배정하는 것이다. 이 때 edge vw에 대하여 v의 topological number는 w의 topological number보다 작다.

reverse topological order는 반대로 v의 topological number가 w의 topological order보다 큰 경우이다.

#### Lemma 7.4
만약 방향 그래프 G가 사이클을 가지고 있으면 G는 topological order가 없다.

### Critical Path Analysis
프로젝트가 
v에 대한 초기 시작 시간은 다음과 같다.
1. 만약 v에 선행되어야하는 작업이 없으면 est는 0이다.
2. v보다 선행되어야하는 작업이 있으면 est는 선행 작업의 earliest finish time의 최대 시간이다.

earliest finish time(eft)는 earliest start time + 지속기간으로 계산된다.

프로젝트에서 critical path는 업무 $v_0, v_1, ..., v_k$의 연속이다.
1. $v_0$ 는 의존성이 없다.
2. 각 업무$v_i (1 <= i <= k)$ 에 대하여 $v_{i-1}$ 은 $v_i$ 의 의존성이다.
3. eft 또는 $v_k$ 는 프로젝트의 모든 업무에 대하여 최고이다.