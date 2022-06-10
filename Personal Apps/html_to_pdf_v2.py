# GUI modules
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter.filedialog import asksaveasfile
import easygui

import os, sys

import requests

import pdfkit

def file_save(url):
	files = [('PDF Document', '*.pdf')]
	file = asksaveasfile(filetypes = files, mode = 'w',defaultextension = files)
	if file is None:
		return 1
	path = file.name
	save_file = pdfkit.from_url(url, path)

if __name__ == "__main__":

	root = tk.Tk()
	root.withdraw()

	# ask user to enter URL
	url = easygui.enterbox(msg='Enter the URL address to convert to PDF:', title='Prompt', default='', strip=True, image=None, root=None)
	print(url)

	if url == None or url == '':
		tk.messagebox.showinfo('Action Cancelled', 'Exiting Program')		
	elif 'http' not in url or 'https' not in url:
		tk.messagebox.showinfo('Error', '\nPlease make the website address starts with http:// or https://.\n')
	else:
		try:
			r = requests.get(url, allow_redirects = True)
			if 	r.status_code == 200:
				file_save(url)
				print('Success', 'File saved')
			else:
				tk.messagebox.showinfo('Error', 'Bad Request. URL not accessible.\n')
		except Exception as e:
			print(e)
			tk.messagebox.showinfo('Error', 'URL not accessible.\nPlease check the website address.\n')

	sys.exit(0)
