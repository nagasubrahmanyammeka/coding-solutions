# cook your dish here
test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    s = input()
    cnt = 0
    opened = 0
    
    for i in range(n):
        if i == 0 or s[i] != s[i-1]:
            cnt = 1
        else:
            cnt += 1
            
        
        if cnt == 3:
            opened += 1
            cnt = 0
            
    print(opened)