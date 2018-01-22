import math
n = eval(input("How many objects do you want?"))
r = eval(input("How many permutations do you want?"))
perm = math.factorial(n)/math.factorial(n-r)
print("There are {} permutations ".format(perm))
comb = math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
print("There are {} combinations ".format(comb))

