from sys import stdin,stdout
stdin = open('in.txt')
input = stdin.readline

for _ in range(int(input())):
    dic = {}
    arr = [input().strip() for _ in range(int(input()))]
    arr.sort(key = lambda x:-len(x))

    for a in arr:
        cur_dic,TF = dic,False
        for n in a:
            if n not in cur_dic:
                cur_dic[n],TF = {},True
            cur_dic = cur_dic[n]
        
        if not TF:
            print('No')
            break
    else:
        print('Yes')