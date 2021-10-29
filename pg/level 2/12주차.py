import heapq as hq

def solution(k, dungeons):
    N = len(dungeons)
    
    remain = [-float('inf')] * (2**N)
    visit = [False] * (2**N)

    que = [(-k,0,0)]
    ans = -1
    while que:
        
        r,bit,cnt = hq.heappop(que)
        
        if not visit[bit]:
            
            visit[bit] = True
            
            if ans < cnt:
                ans = cnt
                
            for i in range(N):
                
                if bit & (1<<i) == 0 :
                    
                    tmp = bit | (1<<i)
                    
                    if dungeons[i][0] <= -r and remain[tmp]<-r-dungeons[i][1]:
                        
                        remain[tmp]=-r-dungeons[i][1]
                        
                        hq.heappush(que,(r+dungeons[i][1],tmp,cnt+1))
    return ans