# Karatsuba multiplication:

## decomposing x into a,b and y into c,d        ~ mul
## finding recursive multiplication of ab,bd    ~ mul
## recursively computing (a+b)*(c+d)            ~
## gauss's trick: 
## compute the whole expression and return
# using string manupilation

def decomposition(x):                           # x is any numberto decompose into 2
    num = str(x)
    mid = len(str(num))//2
    part1 = num[:mid]
    part2 = num[mid:]
    #print("part1: ",int(part1),"part2: ", int(part2))
    return int(part1), int(part2)

def mul(a,b): # recursively finding multiplication of two numbers
    c = (a*b)
    #print("mul: ", c)
    return int(c)

def karatsuba(a,b,c,d,ac,bd):     # 3rd step
    x = ((a+b)*(c+d)) - ac - bd
    #print("karatsuba",x)
    return x

# driver's module:
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
n = len(str(num1))
a,b = decomposition(num1)
c,d = decomposition(num2)
ac = mul(a,c)
bd = mul(b,d)
newnum = karatsuba(a,b,c,d,ac,bd)
#print("(10**n)*ac)",(10**n)*ac)
#print("((10**n//2)*(newnum))",((10**(n//2))*(newnum)))
#print("(10**(n//2))",(10**(n//2)),"newnum",newnum)
#print("bd",bd)
mul =  ((10**n)*ac) + ((10**(n//2))*(newnum)) + bd            # division or integer division
print(mul)


# testcase:
##num1 = 3141592653589793238462643383279502884197169399375105820974944592
##num2 = 2718281828459045235360287471352662497757247093699959574966967627
##ans: 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184





