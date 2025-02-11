from collections import deque

def josephus_q(N, K):
    res = []
    q = deque(range(1, N + 1))  # 1부터 N까지의 숫자를 큐에 추가
    while len(q) > 1:
        # K-1번 앞에서 꺼내 뒤로 보냄
        for _ in range(K - 1):
            q.append(q.popleft())
        # K번째 사람을 제거하고 결과에 추가
        res.append(q.popleft())
    # 마지막 남은 사람을 추가
    res.append(q.popleft())
    return res

# 예제 실행
print(josephus_q(7, 3))
