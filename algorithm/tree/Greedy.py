def solution(k, m, score):
    answer = 0
    c=0
    score = sorted(score,reverse=True)
    box_len = len(score)//m
    # min_lst = min(lst)
    # answer = min_lst*m*
    for _ in range(box_len):
        ss = score[0+c:m+c]
        min_val = min(ss)
        answer += min_val*m
        c+=m
    
    return answer



def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m

