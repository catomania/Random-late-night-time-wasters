# https://www.hackerrank.com/challenges/designer-door-mat

# weirdly enough, this script passes Test 0 before Submit Code, and then fails the same Test 0 after Submit Code.

N, M = map(int,raw_input().split()) 


for i in xrange(1,N,2): # ugh, this is ugly...
    print ('-' * int((M - len('.|.'* i))/2)).ljust(1) + ('.|.'* i) + ('-' * int((M - len('.|.'* i))/2)).rjust(1) 
    

print (N * '-').ljust(1) + str("WELCOME") + (N * '-').rjust(1) 

for i in xrange(N-2,-1,-2): 
    print ('-' * int((M - len('.|.'* i))/2)).ljust(1) + ('.|.'* i) + ('-' * int((M - len('.|.'* i))/2)).rjust(1) 
