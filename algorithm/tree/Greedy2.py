def solution(n, lost, reserve):
    answer = 0
    reserve_st = list(set(reserve) - set(lost))
    lost_st = list(set(lost) - set(reserve))

    for i in reserve_st:
        if i-1 in lost_st:
            lost_st.remove(i-1)
        elif i+1 in lost_st:
            lost_st.remove(i+1)
    return n - len(lost_st)


# 풀이 2
def solution(n, lost, reserve):
    reserve_st = [r for r in reserve if r not in lost]
    lost_st = [l for l in lost if l not in reserve]
    
    for r in reserve_st:
        if r-1 in lost_st:
            lost_st.remove(r-1)
        elif r+1 in lost_st:
            lost_st.remove(r+1)
    return n - len(lost_st)