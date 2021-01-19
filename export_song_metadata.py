#! python3

# os module
import os

# audio file modules
from mutagen.flac import FLAC
import eyed3
from mutagen import ogg

# tkinter modules for windows GUI
from tkinter import *
from tkinter import filedialog

# pandas DataFrame
import pandas as pd

# time formatting
import datetime

# functions

# prompt user for the directory to search
def choose_folder(root=''):
	root = os.path.normpath(filedialog.askdirectory(initialdir=root))
	return root

# prompt user to select a file
def choose_file():
	new_path = filedialog.askopenfilename()
	return new_path

# prompt user for Yes/No
def user_reponse():
	response = ''
	while response.lower() not in ['n','no','y','yes']:
		response = str(input(''))
	return response

# extract tags from mp3
def get_tag_mp3(audio):
	try:
		duration = int(audio.info.time_secs)
		length = str(datetime.timedelta(seconds=duration))

		date_tag =  str(audio.tag.getBestDate()), # this one was hard to find
		date_list = list(map(int, re.findall(r'\d+', date_tag[0]))) # retrieves digits from tag
		date = str([i for i in date_list if len(str(i)) == 4][0]) # return on digits of length 4

		tracknumber = str(audio.tag.track_num[0])
		if  0 <= int(tracknumber) < 10:
			tracknumber = '0' + str(int(tracknumber))

		meta = {
		'Track' : tracknumber,
		'Title' : audio.tag.title,
		'Artist' : audio.tag.artist,
		'Album' : audio.tag.album,
		'Date' : date,
		'Length' : length,
		'Bitrate' : audio.info.bit_rate[1],
		'Genre': audio.tag.genre
		}
		return meta
	except:
		meta = {}
		print('Failed to retrieve ID3 tags for %s.' % audio)
		return meta

# extract tags from flac
def get_tag_flac(audio):
	#test for empty or missing ID3 tags
	try:
		duration = int(audio.info.length)
		length = str(datetime.timedelta(seconds=duration))

		bitrate = int(audio.info.bitrate/1000)

		tracknumber = str(''.join(audio['tracknumber']))
		if  0 <= int(tracknumber) < 10:
			tracknumber = '0' + str(int(tracknumber))

		date_tag = ''.join(audio['date'])
		date_list = list(map(int, re.findall(r'\d+', date_tag)))
		date = str([i for i in date_list if len(str(i)) == 4][0])

		meta = {
		'Track' : tracknumber,
		'Title' : ''.join(audio['title']),
		'Artist' : ''.join(audio['artist']),
		'Album' : ''.join(audio['album']),
		'Date' : date,
		'Length' : length,
		'Bitrate' : bitrate,
		'Genre' : ''.join(audio['genre'])
		}
		return meta
	except:
		meta = {}
		print('Failed to retrieve ID3 tags for %s.' % audio)
		return meta

# main loop

tk = Tk() # assign tk object to variable tk
tk.withdraw() # hide tk window

# allow user to select folder
print('Please select a folder:')
path = choose_folder()

os.chdir(path)

df = pd.DataFrame(columns = ['Track', 'Title','Artist','Album','Date','Length','Bitrate'])

for root, dirs, files in os.walk(path):
	for file in files:
		if file.endswith('.mp3'):
				filepath = root + '\\' + file
				meta = get_tag_mp3(eyed3.load(filepath))
				df = df.append(meta, ignore_index=True) # df.append returns a new dataframe, so you need to write df = df.append
		elif file.endswith('.flac'):
				filepath = root + '\\' + file
				meta = get_tag_flac(FLAC(filepath))
				df = df.append(meta, ignore_index=True)

print(df)

print('Create new file?')

response = user_reponse()

if response.lower() in ['y','yes']:
	print('Please enter a file name:')

	user_input = str(input())
	filename = user_input.split('.csv')[0]

	desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

	print('Choose a directory and file name:')

	save_path = choose_folder(desktop)

	df.to_csv( save_path + '\\' + filename + '.csv', mode='w',index=False)
	print('Done.')

elif response.lower() in ['n','no']:
	print('Append to existing file?')

	response = user_reponse()

	if response in ['a','A','append','Append']:
		print('Choose a file to append:')
		filename = choose_file()
		df.to_csv( save_path + '\\' + filename, mode='a',index=False)

		print('Done.')
	else:
		print('\nCancelling.')



# Cleanup
tk.destroy()

