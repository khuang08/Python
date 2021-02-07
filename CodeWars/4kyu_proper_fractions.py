import math

def proper_fractions(d):
	if d == 1:
		return 0
	else:
		x = [x for x in range(0,d) if math.gcd(d,x) == 1]
		return len(x)



print(proper_fractions(1),0)
print(proper_fractions(2),1)
print(proper_fractions(5),4)
print(proper_fractions(15),8)
print(proper_fractions(25),20)
