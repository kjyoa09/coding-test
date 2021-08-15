'''
이분탐색

바위 n개 이하 제거

mid 보다 값이 작을 때 Save에 저장했다가 더해주기


'''
def solution(distance, rocks, n):
    t = [0] + sorted(rocks) + [distance]
    arr = [t[idx] - t[idx-1] for idx in range(1,len(t))]
    lt,rt,ans = 0,distance,0
    while lt<=rt:

        mid = (lt+rt)//2
        cnt = 0;save = 0
        for tmp in arr:
            if tmp + save < mid:
                cnt +=1
                save += tmp
            else:
                save = 0
            if cnt > n:
                rt = mid - 1
                break
        else:
            if ans < mid:
                ans = mid
                lt = mid + 1
    return ans