def NM(fn, x, tol = 0.000001, maxiter = 1000):
      for i in range(maxiter):
            xnew = x-(fn[0](x)/fn[1](x))
            if abs(xnew -x) < tol : break # tolerance 
            x = xnew
      return round(xnew,6)
y = [lambda x : 7*x**3 +9.5*x +7.5 ,lambda x : 14*x**2 +9.5] # Function and its derivative
s = set({})
for i in range(-100,100): # Range in which you want to search for roots
      s.add(NM(y, i))
print(s)

# print("The root is %f and the number of iteration is %d" %(x,n))
