def solution(answers):
    
    ans1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] * (10000//10)
    ans2 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5] * (10000//16 + 1)
    ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (10000//20 + 1)
    
    ans = [0,0,0]
    while answers:
        tmp_an,a1,a2,a3 = answers.pop(0),ans1.pop(0),ans2.pop(0),ans3.pop(0)
        if tmp_an == a1:
            ans[0] +=1
        if tmp_an == a2:
            ans[1] +=1
        if tmp_an == a3:
            ans[2] +=1
    
    return [idx+1 for idx,x in enumerate(ans) if x == max(ans)]