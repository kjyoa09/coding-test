def solution(board, moves):
    board = list(map(list,zip(*board)))
    
    maps = []
    for tmp in board:
        maps += [[x for x in tmp if x != 0]]
        
    
    stack = []
    ans = 0
    for move in moves:
        tmp = move - 1
        if len(maps[tmp]) == 0:
            continue
        else:
            if len(stack) != 0 and stack[-1] == maps[tmp][0]:
                stack.pop()
                ans += 2
            else:
                stack.append(maps[tmp][0])
            maps[tmp] = maps[tmp][1:]
    
    return ans