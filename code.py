# --------------
#Code starts here
def palindrome(num):
    num=num+1
    while True:
        if num == reverse(num):
            return num
        num+=1

def reverse(a):
    rev=0
    while(a>0):
        n = a%10
        
        rev = rev*10+n
        a = a//10
        print(n,a,rev)
    return rev
print(palindrome(10201))


# --------------
#Code starts here
def a_scramble(str_1,str_2):
    count=0
    news = [j for j in str_2.lower()]
    news1= [i for i in str_1.lower()]
    trace1=news1
    trace=news
    for i in news1:
        if i in news and i in trace1:
            trace.remove(i)
            count+=1
    
    if len(trace)==0:
        return True
    else:
        return False

print(a_scramble("Tom Marvolo Riddle","Voldemort"))
print(a_scramble("ticket","chat"))
print(a_scramble("baby shower","shows"))
print(a_scramble("eatcher","teacher"))
print(a_scramble("labratory","Bat"))


# --------------
import math
def check(num):
        i = int(math.sqrt(num))
        return(num == i*i)
        
def check_fib(num):
    if check(5*num*num+4) or check(5*num*num-4):
        return True
    else:
        return False
print(check_fib(145))


# --------------
from itertools import groupby
def compress(word):
    return ''.join('%s%s' % (char, sum(1 for _ in group)) for char, group in groupby(word.lower()))
compress("Ss")


# --------------
#Code starts here
def k_distinct(string,k):
    s = list(set(string.lower()))

    if len(s) == k:
        return True
    else:
        return False
print(k_distinct('Messoptamia',8))

print(k_distinct('banana',4))


