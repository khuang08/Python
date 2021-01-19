# GUI modules
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter.filedialog import asksaveasfile
import easygui

import os, sys

import requests

import pdfkit

def ConfirmationDialog(message):
	MsgBox = tk.messagebox.askquestion('Proceed?',message ,icon = 'warning')
	return(MsgBox)

def file_save(url):
	files = [('PDF Document', '*.pdf')]
	file = asksaveasfile(filetypes = files, mode = 'w',defaultextension = files)
	if file is None:
		return 1
	path = file.name
	save_file = pdfkit.from_url(url, path)
	return 0

def ConfirmationDialog(message):
	MsgBox = tk.messagebox.askquestion('Proceed?',message ,icon = 'warning')
	return(MsgBox)	

def ConfirmExit():
	if ConfirmationDialog('Do you want to exit?')== 'yes':
		sys.exit(0)

def getURL():
	link = easygui.enterbox(msg='Enter the URL address to convert to PDF:', title='Prompt', default='', strip=True, image=None, root=None)	
	return link

def invalidURL():
	global url
	tk.messagebox.showinfo('Error', 'URL not accessible.\nPlease check the website address.\n')
	ConfirmExit()
	url = None

def missingHTTP():
	global url
	tk.messagebox.showinfo('Error', '\nPlease make the website address starts with http:// or https://.\n')
	ConfirmExit()
	url = None

def PageNotFound():
	global url

	tk.messagebox.showinfo('Error', 'Bad Request. URL not accessible.\n')
	ConfirmExit()
	url = None

if __name__ == "__main__":

	repeat = 1
	url = None

	root = tk.Tk()
	root.withdraw()

	while repeat == 1:
		while url == None:
			url = getURL() #prompt user for URl
			if url == None or url == '':
				ConfirmExit()
			elif 'http' not in url or 'https' not in url:
				missingHTTP()
			else:
				try:
					r = requests.get(url, allow_redirects = True)
					if 	r.status_code == 200:
						repeat = file_save(url)
					else:
						PageNotFound()
				except:
					invalidURL()

	print('\nDone.')
	root.destroy()

# test: https://www.tokyotosho.info/?cat=1
