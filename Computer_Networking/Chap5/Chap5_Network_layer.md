# Ch5: Control Plane
### Network-layer functions
data plane: forwading
control plane: routing
- per-router control(traditional)
- logically centralized control(Software Defined Networking, SDN)

## 5.2 Routing protocols
송신자 호스트에서 수신자 호스트로의 네트워크 상의 최적의 경로를 결정하는 방법(least cost, fastest, least congested)
cost function을 결정하는 데는 hop 수, delay, congestion이 들어갈 수 있다.
### link state
대표적인 라우팅 프로토콜: OSPF
### distance vector
대표적인 라우팅 프로토콜: RIP

### Graph abstraction of the network
라우터를 노드로, 라우터간 연결 링크를 엣지로 표현한다.
weighted graph로 weight는 link cost이며 cost function에 의해 결정된다.
C(X, Y)는 X, Y사이에 연결된 링크의 COST를 의미한다. cost는 보통 1이지만, 대역폭에 비례하여, 혼잡 정도에 반비례한다. 대역폭은 minimum만 맞추면 된다.

### Routing Approach Classification
1. global or decentralized information?
- global(link state algorithm)
    - 모든 라우터는 전체 정보(link cost info)를 가지고 있다.
- decentralized(distance vector algorithm)
    - 바로 옆에 이웃한 라우터와 정보 교환을 한다. 따라서 이웃 라우터의 cost를 알 수 있다.
    - 전체 라우터의 정보를 알 수 없다.
    - 첫 계산에는 minimum cost path를 발견할 수 없지만 반복된 계산을 통해 발견할 수 있다.

2. Static or Dynamic?
- static(fixed): 경로가 정해지면 특별한 문제 없이는 그 경로를 사용한다. -> 네트워크 상황 반영이 잘 안 된다.
- Dynamic: 오버헤드 때문에 주기적으로 업데이트하여 link cost에 따라 경로를 결정한다. -> 네트워크 상황 반영이 잘 된다.