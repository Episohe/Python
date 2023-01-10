"""
section 1
Multithreading - Difference between Process and Thread
Keyword - Process, Thread
"""

"""

(1). 프로세스
    - 운영 체제 -> 할당 받는 자원 단위(실행 중인 프로그램)
    - cpu 동작 시간. 주소 공간(독립적)
    - Code, Data, Stack, Heap -> 독립적
    - 최소 1개의 메인 스레드 보유
    - 파이프. 파일, 소켓 등을 사용해서 프로세스간 통신(Cost 높음) -> Context Swithcing.
    
(2).스레드
    - 프로세스 내에 실행 흐름 단위
    - 프로세스 자원 사용
    - Stack만 별도 할당, 나머지는 공유(Code, Data, Heap)
    - 한 스레드의 결과가 다른 스레드에 영향 끼침
    - 동기화 문제는 정말 주의(디버깅 어려움)
    
(3). 멀티 스레드
    - 한 개의 단일 어플리케이션(응용프로그램) -> 여러 스레드로 구성 후 작업 처리
    - 시스템 자원 소모 감소(효율성), 처리량 증가(Cost 감소)
    - 통신 부담 감소. 디버깅 어려움, 단일 프로세스에는 효과 미약. 자원의 공유 문제(교착 상태), 프로세스 영향을 끼침

(4) 멀티 프로세스
    - 한개의 단일 어플리케이션(응용프로그램) -> 여러 프로세스로 구성 후 작업 처리
    - 한개의 프로세스 문제 발생은 확산이 없다. (프로세스 Kill시키면 된다.)
    - 캐시 체인지. Cost 비용 매우 높은(오버헤드) 복잡한 통신 방식 사용

"""
