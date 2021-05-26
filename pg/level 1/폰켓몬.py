def solution(nums):
    sp = len(set(nums))
    
    if sp < len(nums)//2:
        return sp
    else:
        return len(nums)//2