import os, sys
from easygui import *
import tkinter as tk
from tkinter import messagebox

if __name__ == "__main__":

	count = 0

	path = "C:\\youtube-dl"

	# checks if folder exists
	if os.path.isdir(path) == False:
		os.mkdir(path)

	os.chdir(path)

	root = tk.Tk()
	root.withdraw()

	text = 'Fill in values for the fields.'
	title = 'Youtube-dl - Enter URL to download:'
	fieldNames = ["URL1","URL2","URL3","URL4","URL5"]
	default_list= ['','','','','']
	
	url_list = multenterbox(text, title, fieldNames, default_list)
	
	# Exit if user presses Cancel
	if url_list == None:
		tk.messagebox.showinfo("Youtube-dl", f"Exiting.")
		sys.exit()

	# remove blank entries in URL list
	while("" in url_list): 
		url_list.remove("")

	# go through each URL and download
	for url in url_list:
		try:
			os.system(f"youtube-dl -f best {url}")
			count += 1
		except:
			tk.messagebox.showinfo("Youtube-dl", f"Invalid URL: {url}.\n")

	if count > 0:
		plural = 's'
	else:
		plural = ''

	tk.messagebox.showinfo("Youtube-dl", f"{count} video{plural} downloaded to {path}. Exiting.\n")

	root.destroy()

