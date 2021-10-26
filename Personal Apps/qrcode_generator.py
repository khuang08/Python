import os, sys
from easygui import *
import tkinter as tk
from tkinter import messagebox

from datetime import date
import qrcode
from PIL import Image

if __name__ == "__main__":

	count = 0

	path = "C:\\QRCode\\"
	os.chdir(path)

	# checks if folder exists
	if os.path.isdir(path) == False:
		os.mkdir(path)

	os.chdir(path)

	root = tk.Tk()
	root.withdraw()

	text = 'Enter URL to convert:'
	title = 'QR Code Generator'
	fieldNames = ["URL1"]
	default_list= ['']
	
	url_list = multenterbox(text, title, fieldNames, default_list)

	# Exit if user presses Cancel
	if url_list == None:
		sys.exit()

	# remove blank entries in URL list
	while("" in url_list): 
		url_list.remove("")

	# go through each URL and download
	for url in url_list:
		try:
			img = qrcode.make(url)
			today = date.today()
			date = today.strftime("%m_%d_%y")
			filename = f"qrcode_{date}.png"
			img.save(filename)
		except:
			tk.messagebox.showinfo("QR Code Generator", f"Invalid URL: {url}.\n")

	if count > 0:
		plural = 's'
	else:
		plural = ''

	im = Image.open(filename) 
	im.show()

	tk.messagebox.showinfo("QR Code Gnenerator", f"QR code saved to {path}{filename}.\n")

	root.destroy()

