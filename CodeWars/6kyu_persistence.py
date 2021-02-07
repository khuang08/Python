def persistence(n):
	counter, result = 0, 1
	stop = False
	
	if n < 10:
		return(0)

	num_str = list(str(n))

	while stop == False:
		for i in num_str:
			result = result * int(i)
		
		counter += 1

		if result < 10:
			stop = True
		else:
			num_str = list(str(result))
			result = 1
			
	return(counter)

print(persistence(39))
print(persistence(4))
print(persistence(25))
print(persistence(999))

'''
Test.it("Basic tests")
Test.assert_equals(persistence(39), 3)
Test.assert_equals(persistence(4), 0)
Test.assert_equals(persistence(25), 2)
Test.assert_equals(persistence(999), 4)
'''
