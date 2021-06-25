# n = list(map(int,input().split()))
#Sum of Consecutive Nth Powers Equals an sum of Nth Power of Next Consecutive numbers
def eqz(n):
# Return the list of number if the sum of p consecutive numbers is equal to sum of q consecutive number.
    for i in range(1,len(n)):
        if sum(n[:i]) == sum(n[i:]):   
            print(f"{n[:i]}={n[i:]}")

def createList(r1, r2):
    # It create a list
    return list(range(r1, r2+1))

def D(k):
    # apply a range of list (k elements) to th eqz function
    for i in range(1,1000):
        eqz([pow(x,2) for x in createList(i,i+k)])

for j in range(100):
    D(j)