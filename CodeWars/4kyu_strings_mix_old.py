import re
from collections import Counter

def mix(s1, s2):
	s1_dict = Counter(s1)
	s2_dict = Counter(s2)
	s1_result = ''
	s2_result = ''
	result = []

	for i in s1_dict:
		if s1_dict[i] > 1 and i != " ":
			s1_result += i*s1_dict[i]

	for j in s2_dict:
			if s2_dict[j] > 1 and j != " ":
				s2_result += j*s2_dict[j]

	substring1 = [match[0] for match in re.findall(r'((.)\2*)', s1_result)]
	substring2 = [match[0] for match in re.findall(r'((.)\2*)', s2_result)]
	substring1.sort()
	substring2.sort()
	
	return (substring1, substring2)


print(mix("Lords of the Fallen", "gamekult")) #"1:ee/1:ll/1:oo"
print(mix("Are they here", "yes, they are here")) # "2:eeeee/2:yy/=:hh/=:rr"
print(mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwKizfd$lvse+gnbaGydxyXzayp")) #'2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz'
print(mix("looping is fun but dangerous", "less dangerous than coding")) #"1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"
print(mix(" In many languages", " there's a pair of functions")) #"1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt"
print(mix("codewars", "codewars")) #""
print(mix("A generation must confront the looming ", "codewarrs")) #"1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr"



