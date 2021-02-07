#create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

def create_phone_number(n):
	nums = ''.join(map(str,n))
	return('(' + nums[0:3] + ')' + ' ' + nums[3:6] + ('-') + nums[6:10])


telephone_num = create_phone_number([1,2,3,4,5,6,7,8,9,0])
print(telephone_num)
