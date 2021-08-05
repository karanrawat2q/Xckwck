# Python program to print all primes smaller than or equal to n using Sieve of Eratosthenes

def SOE(n):
        # Creating boolean array where all the values are True
        # A value in prime[i] will be false if i is not prime
        prime = [True for i in range(n+1)]
        p = 2
        
        while (p*p <= n):
                if prime[p] == True:
                        for i in range(p*p,n+1,p):
                                prime[i] = False
                p +=1

        for p in range(2,n+1):
                if prime[p] == True:
                        print(p)

if __name__ == "__main__":
        n = 30
        SOE(n)
