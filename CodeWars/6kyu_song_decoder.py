def song_decoder(song):
	return(' '.join(song.replace('WUB',' ').split()))

print(song_decoder("AWUBBWUBC"))
print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))
print(song_decoder("WUBAWUBBWUBCWUB"))
print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))
