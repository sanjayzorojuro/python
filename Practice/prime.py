import math

def is_prime(n):
    if n<=0:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i == 0:
            return False
    return True

def gen_prime(start,end):
    prime=[]
    for n in range(start,end):
        if is_prime(n):
            prime.append(n)
    return prime

start=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))
print(gen_prime(start,end))


