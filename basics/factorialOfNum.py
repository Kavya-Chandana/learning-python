#waf to find the sum of first n numbers(while)
def fact_num(num):
    fact=1
    for i in range (1,num+1):
        fact*=i
    print(fact)
    
fact_num(4)
fact_num(5)
