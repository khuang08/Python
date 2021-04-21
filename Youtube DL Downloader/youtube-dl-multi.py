import os
from easygui import *
import tkinter as tk
from tkinter import messagebox

if __name__ == "__main__":

	count = 0
	os.chdir("D:\\youtube-dl")

	root = tk.Tk()
	root.withdraw()

	text = 'Fill in values for the fields.'
	title = 'Youtube-dl - Enter URL to download:'
	fieldNames = ["URL1","URL2","URL3","URL4","URL5"]
	default_list= ['','','','','']
	
	url_list = multenterbox(text, title, fieldNames, default_list)
		
	while("" in url_list): 
		url_list.remove("")

	for url in url_list:
		try:
			os.system('youtube-dl -f best "%s"' % url)
			count += 1
		except:
			tk.messagebox.showinfo('Youtube-dl', 'Invalid URL: %s.\n' % url)

	if count > 0:
		plural = 's'
	else:
		plural = ''

	tk.messagebox.showinfo('Youtube-dl', '%s video%s downloaded. Exiting.\n' % (count,plural))

	root.destroy()
