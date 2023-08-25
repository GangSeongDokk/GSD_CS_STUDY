# CPU 스케줄링 알고리즘
- CPU 스케줄러
    - CPU 스케줄링 평가 기준
- 비선점형
    - FCFS
    - SJF
    - 우선순위
- 선점형
    - 라운드로빈
    - SRF
    - 다단계 큐
        - MFQ


## CPU 스케줄러
- CPU 스케줄링 알고리즘에 따라 프로세스에서 해야하는 일을 스레드 단위로 CPU에 할당함

### CPU 스케줄링 평가 기준
- CPU 이용률(CPU utilization)
    - 시간당 CPU를 사용한 시간의 비율
    - 프로세서를 실행상태로 항상 유지하려 해야함
- 처리율(Throughput)
    - 시간당 처리한 작업의 비율
    - 단위 시간당 완료되는 작업 수가 많도록 해야 함.
- 반환시간(Turnaround Time) 
    - 프로세스가 생성된 후 종료되어 사용하던 자원을 모두 반환하는 데까지 걸리는 시간
    - 작업이 준비 큐(ready queue)에서 기다린 시간부터 CPU에서 실행된 시간, I/O 작업 시간의 합이다.
- 대기시간(Waiting Time)
    - 대기열에 들어와 CPU를 할당받기 까지 기다린 시간
    - 준비 큐에서 기다린 시간의 총합
- 반응시간(Response Time)
    - 대기열에서 처음으로 CPU를 얻을 때까지 걸린 시간
    - 대기시간과 비슷하지만 다른 점은, 대기시간은 준비 큐에서 기다린 모든 시간을 합친 것이지만 반응 시간은 CPU를 할당받은 최초의 순간까지 기다린 시간 한번 만을 측정.

#### -> CPU 이용률과 처리율은 극대화하는 것이 좋고 반환시간, 대기시간, 반응시간은 줄이는 것이 일반적으로 좋다.


## 비 선점형 방식(non-preemptive)
- 프로세스가 스스로 CPU 소유권을 포기하는 방식
- (강제로 프로세스 중지 X) -> 컨텍스트 스위칭으로 인한 부하가 적음

### FCFS(First Come, First Served)
- 가장 `먼저` 온 것을 가장 먼저 처리하는 알고리즘
- 단점 : 준비 큐에서 오래 기다리는 현상(호위 현상, convoy effect)이 발생
![FCFS](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fcj1eAz%2FbtrwVseqDoP%2FkywQBfZVaeLRcEJ7nFNXk0%2Fimg.png)

### SJF(Shortest Job First)
- 실행시간이 가장 `짧은` 프로세스를 가장 먼저 실행하는 알고리즘
- 과거 실행했던 시간을 토대로 실행시간을 추측
- 장점 : 평균 대기 시간이 가장 짧음
- 단점 : 긴 시간을 가진 프로세스가 실행되지 않는 현상(starvation)이 발생
![SJF](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FLvUVD%2FbtrwVsSWLbJ%2FoIOaF3SBtE9Gd87sWqjGWK%2Fimg.png)


### 우선순위(priority)
- 가장 `짧은` 프로세서 + `오래된` 프로세서
- SJF의 단점을 보완한 알고리즘
![SJF](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FA4IZf%2FbtrwVrs2Cux%2Fs1k5EWSxBkYRMgULlr4F70%2Fimg.png)

## 선점형 방식(preemptive)
- 지금 사용중인 프로세스를 알고리즘에 의해 중단, 강제로 다른 프로세스에 CPU 소유권을 할당하는 방식
- 현대 운영체제가 쓰는 방식

### 라운드로빈(RR, Round Robin)
- 현대 컴퓨터가 쓰는 스케줄링인 우선순위 스케줄링(priority scheduling)의 일종
- 각 프로세스는 `동일한 할당 시간`을 주고 그 시간안에 끝나지 않으면 다시 준비 큐(ready queue)의 뒤로 가는 알고리즘
- 로드밸런서에서 트래픽 분산 알고리즘으로도 사용
- 장점 : 평균 응답 시간이 짧음
- 단점 : 할당 시간이 너무 크면 FCFS, 짧으면 컨텍스트 스위칭이 잦아져서 오버헤드가 발생
![RR](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FoVKvq%2Fbtrw2NV85g2%2FymVM3yVGOHXr9GqSkkZPD0%2Fimg.png)

### SRF
- 중간에 실행 시간이 더 짧은 작업이 들어오면 프로세스를 중지하고 해당 프로세스를 수행하는 알고리즘

![SRF](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FL2iRd%2FbtrwXz49BtP%2FucHEyokTcjfydBSZdogOhK%2Fimg.png)

||SRF|SJF|
|---|---|---|
|순서|실행시간이 짧은 순서|실행시간이 짧은 순서|
|더 짧은 프로세서 추가 시|실행 중인 프로세스 다음에 추가|중단 후 새 프로세서 실행|

### 다단계 큐(Multilevel Queue)
- 우선순위에 따른 준비 큐를 여러개 사용, 큐마다 다른 스케줄링 알고리즘을 적용한 것
- 큐 간의 프로세스는 이동이 안되므로 스케줄링 부담은 적지만 유연성이 떨어짐
![Multilevel Queue](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FL2iRd%2FbtrwXz49BtP%2FucHEyokTcjfydBSZdogOhK%2Fimg.png)

```
ex) 다단계 큐
높은 우선순위 - 시스템 프로세스 - FCFS
중간 우선순위 - 상호 작용적인 프로세스 - 상호 작용적인 프로세스
낮은 우선순위 - 배치 프로세스 - RR

=> CPU
```

#### Multilevel Feedback Queue(MFQ)
- Multilevel Queue와 비슷하지만, MFQ는 각 큐 간에 프로세스들이 이동가능
![Multilevel Queue](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbbMjai%2FbtrwVsZNvAn%2FD8SiDqyVytoNg1usFOeBw0%2Fimg.png)


참고
- [코드연구소](https://code-lab1.tistory.com/45)
- [웨지의 개발 블로그](https://sihyung92.oopy.io/os/5)
