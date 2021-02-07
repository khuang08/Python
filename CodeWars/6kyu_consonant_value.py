def solve(s):
	vowels = "aeiou"
	top = 0
	score = 0
	count = 1
	consonants = dict()

	for x in "abcdefghijklmnopqrstuvwxyz":
			consonants[x] = count
			count += 1

	for i in s:
		if i not in vowels:
			score = score + consonants[i]
			if score > top:
				top = score
		else:
			score = 0

	return(top)



print(solve("zodiac")) #26
print(solve("chruschtschov")) #80
print(solve("khrushchev")) #38
print(solve("strength")) #57
print(solve("catchphrase")) #73
print(solve("twelfthstreet")) #103
print(solve("mischtschenkoana")) #80
print(solve("strength")) #57