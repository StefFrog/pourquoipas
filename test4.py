"""
N = input("Entrer le maximum de la suite : ")

U=range(1,N*N)
U[0]=1
U[1]=1

for i in range(2,N+1) :
         U[i] = U[i-1] + U[i-2]

for i in range (0,N):
         print U[i]
"""

"""
N = input("Entrer le maximum de la suite : ")

U=range(1,N*N)

for i in range(2, N) :
         U.append(U[i-1] + U[i-2])

for i in range (0,N):
         print U[i] #affiche ta liste
"""



import os
def fibonacci(limit):
    res = 0;
    x = 0;
    y = 1;
    while res < limit :
        print res
        res = x + y
        x = y
        y = res

def main():
    os.system('cls')
    print """
    image
