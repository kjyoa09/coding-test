from collections import deque,defaultdict

def bfs(s,maps):
    dic = defaultdict(list)
    que = deque([(-1,s,0)])
    
    while que:
        pre,now,cnt = que.popleft()
        dic[cnt].append(now)
        for next_node in maps[now]:
            if next_node != pre:
                que.append((now,next_node,cnt+1))
                
    return dic,cnt

def solution(n, edges):
    maps = [[] for _ in range(n)]
    for s,e in edges:
        maps[s-1].append(e-1)
        maps[e-1].append(s-1)
    
    dic,cnt = bfs(0,maps)
    dic,cnt = bfs(dic[cnt][0],maps)
    
    ans = cnt - 1 if len(dic[cnt]) == 1 else cnt
    dic,cnt = bfs(dic[cnt][0],maps)
    
    return max(ans,cnt - 1 if len(dic[cnt]) == 1 else cnt)