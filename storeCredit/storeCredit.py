"""
storeCredit.py
"""
# waffer

def find2items(items, credit):
    for i in range(len(items)):
        for j in range(len(items)):
            if i == j: continue
            
            if items[i] + items[j] == credit:
                return "{0} {1}".format(min(i, j) + 1, max(i, j) + 1)
            

T = int(input())
for testcase in range(1, T + 1):
    C = int(input())
    I = int(input())
    Li = [int(P) for P in input().split(' ')]
    print("Case #{0}: {1}".format(testcase, find2items(Li, C)))
