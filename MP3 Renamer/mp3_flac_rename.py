# GUI modules
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

# audio file modules
from mutagen.flac import FLAC
import eyed3

import os, sys

def choose_folder():
	root = os.path.normpath(filedialog.askdirectory(initialdir=os.getcwd()))
	return root

def ConfirmationDialog(message):
	MsgBox = tk.messagebox.askquestion('Proceed?',message ,icon = 'warning')
	return(MsgBox)

def file_rename():
	global count_rename
	global count_skip
	try:
		os.rename(file,new_name)
		print(file , ' >>\n' , new_name)
		print('')
		count_rename += 1
	except:
		print('Unable to rename \n' + file)
		count_skip += 1

root = tk.Tk()
root.withdraw()

path = '.'

repeat = 'yes'

while(path == '.' and repeat == 'yes'):
	count = 0
	count_rename = 0
	count_skip = 0

	path = choose_folder()
	if(path == '.' and ConfirmationDialog('Do you want to exit?') == 'yes'):
		tk.messagebox.showinfo('Done', 'Exiting.\n')
		sys.exit(1)

	os.chdir(path)

	files = [x for x in os.listdir() if any(x.endswith(s) for s in ('.mp3', '.flac'))] # returns only .mp3 or .flac files, any keyword in fancy list comprehension
	files_str = '\n'.join(files)

	count = len(files)

	# get file count and ask user to confirm
	if ConfirmationDialog(str(count) + ' files found.\n' + files_str +'\n\nDo you want to continue?') == 'yes':
		print('Files renamed:')

		for file in files:
			if file.endswith('.mp3'):
				audio = eyed3.load(file)

				tracknumber = str(audio.tag.track_num[0])
				if  0 <= int(tracknumber) < 10:
					tracknumber = '0' + str(int(tracknumber))

				new_name = str(tracknumber) + ' - ' + str(audio.tag.title) + '.mp3'
				
				file_rename()

			elif file.endswith('.flac'):
				audio = FLAC(file)

				tracknumber = str(''.join(audio['tracknumber']))
				if  0 <= int(tracknumber) < 10:
					tracknumber = '0' + str(int(tracknumber))

				new_name = str(tracknumber) + ' - ' + str(''.join(audio['title'])) + '.flac'
				
				file_rename()

		message = str(count_rename) + ' files renamed.\n' + str(count_skip) + ' files skipped.'
		tk.messagebox.showinfo('Done', message)

	if(ConfirmationDialog('Do you wish to select another folder?') == 'yes'):
		path = '.'

tk.messagebox.showinfo('Done', 'Exiting.\n')
root.destroy()
