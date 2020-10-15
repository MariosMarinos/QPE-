import math
#m service rate, p = utilization.
m = 0.75
p =0.85
# k values from 1 to 64 (k = servers). 
k = [2**x for x in range(0,7)]
# p = l/k*m -----> l = pkm
l = [p*k*m for k in k]
# question i) derive the frcation of customers that are delayed for each k (server).
for k, l in zip(k, l):
    p0 = 0
    pQ = 0
    # calculate the sum of the formula (Lecture 8 page 12.)
    for i in range(0, k):
        p0 +=((k*p)**i) / math.factorial(i) 
        
    p0 += ((k*p)**k) / (math.factorial(k) * (1-p))
    p0 = p0 ** (-1)
    # the probability of an arrival finding all servers busy pQ.
    pQ = (((k*p)**k) * p0) / (math.factorial(k) * (1-p))
    print("the probability of finding all servers occupied and thus customers are delayed pQ =  {}".format(pQ))
    ExpectedNQ = (p / (1-p)) * pQ
    ExpectedTQ = (1/l) * ExpectedNQ
    print("the expected waiting time for the customers that are delayed is E[TQ] = {} seconds".format(ExpectedTQ))
