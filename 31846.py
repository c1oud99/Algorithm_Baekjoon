def max_folding_score():
    import sys
    input = sys.stdin.read  # 대량의 데이터를 한 번에 읽어들이기 위해 사용할 수 있습니다.
    data = input().split()

    # 입력 데이터 파싱
    index = 0
    N = int(data[index])  # 첫 번째 줄: 문자열의 길이 N
    index += 1
    S = data[index]  # 두 번째 줄: 문자열 S
    index += 1
    Q = int(data[index])  # 세 번째 줄: 질문의 수 Q
    index += 1

    queries = []
    for _ in range(Q):
        l = int(data[index])  # 질문에 대한 l 값
        r = int(data[index + 1])  # 질문에 대한 r 값
        queries.append((l, r))
        index += 2

    # 이제 S와 queries를 가지고 점수 계산 로직을 수행
    # ...


# 실제 환경에서 사용할 때는 이 함수를 직접 호출하여 사용합니다.
if __name__ == "__main__":
    max_folding_score()
