from sys import stdin,stdout
stdin = open('in.txt')
input = stdin.readline

color_dic = {'data':0}
C,N = map(int,input().strip().split(' '))
for _ in range(C):
    cur_dic = color_dic
    for c in input().strip():
        if c not in cur_dic:
            cur_dic[c] = {'data':0}
        cur_dic = cur_dic[c]
    cur_dic['data'] = True

team_dic = {'data':0}
for _ in range(N):
    cur_dic = team_dic
    for n in input().strip()[::-1]:
        if n not in cur_dic:
            cur_dic[n] = {'data':0}
        cur_dic = cur_dic[n]
    cur_dic['data'] = 1
for _ in range(int(input())):
    tmp = input().strip()
    Len = len(tmp)
    arr = [0] * Len
    cur_dic = color_dic
    for idx1 in range(Len):
        if tmp[idx1] in cur_dic:
            cur_dic = cur_dic[tmp[idx1]]
            arr[idx1] += cur_dic['data']
        else:
            arr[idx1] += cur_dic['data']
            break
    cur_dic = team_dic
    for idx2 in range(Len-1,-1,-1):
        if tmp[idx2] in cur_dic:
            cur_dic = cur_dic[tmp[idx2]]
            arr[idx2] += cur_dic['data']
        if arr[idx2] == 2:
            print('Yes')           
            break
    else:
        print('No')
