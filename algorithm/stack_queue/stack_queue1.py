from collections import deque

def solution(priorities, location):
    queue = deque([(v, i) for i, v in enumerate(priorities)])
    res:int = 0

    while queue:
        current = queue.popleft()
        if any(current[0] < q[0] for q in queue):
            queue.append(current)
        else:
            res +=1
            if current[1] == location:
                return res

# print(solution([1, 1, 9, 1, 1, 1], 0))


def solution(priorities, location):
    answer: int = 0
    queue = [(i, p) for i, p in enumerate(priorities)]

    while queue:
        current = queue.pop(0)
        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            answer +=1
            if current[0] == location:
                return answer


# lesson learned
# deque : Double-Ended Queue, 양쪽 끝에서 요소를 추가하고 제거할 수 있는 자료구조
    # append() , appendleft(), pop(), popleft() 메서드를 통해 앞 뒤의 요소를 제거
    # 효율성 : O(1)
# 구문: (expression for item in iterable if condition)
# Ex.) all(n % 2 ==0 for n in numbers) : 짝수 여부 예시
# EX.) max(x for x in numbers if x % 2 == 1) : 홀수 중 최대 값 예시
# Ex.) set(x * x for x in numbers) : 제곱값 중복 제거 후 집합 생성
# Ex.) dict((k,v) for k, v in zip(keys, values)) : 각각의 키와 value를 zip을 통해 묶어서 생성
