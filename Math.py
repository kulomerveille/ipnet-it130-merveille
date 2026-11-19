"""u =3
v =1
n =int(input("donner n="))
for k in range(n):
    print("u(",k,")",u)
    u = sum_(k-0)^(n) 1/k!
    v = u + 1/(n)"""
from math import *
def u(n): 
    return sum(1/factorial(k)for k in range (n+1))
def v(n) :
    return u(n) + 1/(n*factorial(n))

n = int (input("entrer un entier n >=1 :"))
print (f"{'n' :>4} | {'u_n' :>20} |{'v_n' :>20} | {'v_n - u_n' :>14} ")
print("-" * 70)
for k in range (1,n+1):
    uk, vk =  u(k), v(k)
    print (f"{k :>4} | {uk :>20.10f} |{vk :>20.10f} | {vk - uk :>14.6e}  ")