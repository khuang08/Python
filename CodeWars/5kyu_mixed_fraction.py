from math import gcd

def mixed_fraction(s):
	dividend = int(s.split('/')[0])
	divisor = int(s.split('/')[1])

	if dividend < 0 and divisor < 0:
		dividend = -dividend
		divisor = -divisor
	elif divisor <  0 and dividend > 0:
		dividend = -dividend
		divisor = -divisor

	number = dividend // divisor
	remainder = dividend % divisor

	g = gcd(remainder, divisor)
	remainder = int(remainder/g)
	divisor = int(divisor/g)

	if divisor == 0:
		raise ZeroDivisionError
	elif dividend == 0:
		return '0'
	elif dividend > divisor and remainder == 0:
		return(str(number))
	elif dividend > divisor:
		return(str(number) + ' ' + str(remainder) + '/' + str(divisor))
	else:
		g = gcd(dividend, divisor)
		return(str(int(dividend/g)) + '/' + str(int(divisor/g)))


print(mixed_fraction('42/9'), '4 2/3')
print(mixed_fraction('6/3'), '2')
print(mixed_fraction('4/6'), '2/3')
print(mixed_fraction('0/18891'), '0')
print(mixed_fraction('-10/7'), '-1 3/7')
print(mixed_fraction('-22/-7'), '3 1/7')
print(mixed_fraction('-4982466/5619380'), '-2491233/2809690')

#Test.expect_error("Must raise ZeroDivisionError", lambda: mixed_fraction(0, 0))
#Test.expect_error("Must raise ZeroDivisionError", lambda: mixed_fraction(3, 0))