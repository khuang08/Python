from collections import Counter

def mix(s1, s2):
	result = []

	s1_dict = {k: v for k,v in Counter(s1).items() if k != ' ' and v > 1 and k.islower()}
	s2_dict = {k: v for k,v in Counter(s2).items() if k != ' ' and v > 1 and k.islower()}


	for k1, v1 in s1_dict.items():
		for k2, v2 in s2_dict.items():
			if k1 == k2 and v1 > v2 and :
				result.append('1:' + k1*v1)
			elif k1 == k2 and v1 < v2:
				result.append('2:' + k2*v2)
			elif k1 == k2 and v1 == v2:
				result.append('=:' + k1*v1)
	result.sort()

	return('/'.join(result))



print(mix("Lords of the Fallen", "gamekult")) #"1:ee/1:ll/1:oo"
print(mix("Are they here", "yes, they are here")) # "2:eeeee/2:yy/=:hh/=:rr"
print(mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwKizfd$lvse+gnbaGydxyXzayp")) #'2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz'
print(mix("looping is fun but dangerous", "less dangerous than coding")) #"1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"
print(mix(" In many languages", " there's a pair of functions")) #"1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt"
print(mix("codewars", "codewars")) #""
print(mix("A generation must confront the looming ", "codewarrs")) #"1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr"



