from tkinter import *
from tkinter import filedialog, messagebox

# used for multenterbox
from easygui import *

import sqlite3
from sqlite3 import Error

import os, sys
import pandas as pd

class Window(Frame):

	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.master = master
		self.init_window()

	def init_window(self):
		global connection
		global cursor
		global sqliteConnection
		sqliteConnection = None
		connection = False

		# title of our master widget   
		self.master.title("Database Import")

		# allowing the widget to take the full space of the root window
		self.pack(fill=BOTH, expand=1)


		# creating button instances

		# Open Database File
		connectButton = Button(self, text = "Open Database File", command = lambda: [Sqlite.cursor_connect(self,connectText)])
		connectButton.place(x=15, y=10)
		connectText = Text(self, height = 1,
						width = 30,
						bg = "light cyan")
		connectText.place(x=150, y=10)

		# Get Table Names
		tablesButton = Button(self, text = "Get Table Names", command = lambda: self.getTables(tablesText))
		tablesButton.place(x=15, y=80)
		tablesText = Text(self, height = 6,
						width = 30,
						bg = "light cyan")
		tablesText.place(x=150, y=80)

		# Execute Query
		executeButton = Button(self, text = "Execute Query", command = lambda: Sqlite.cursor_execute(self, cursor, queryText, exportStatus))
		executeButton.place(x=15, y=220)
		queryText = Text(self, height = 1,
						width = 30,
						bg = "light yellow")
		queryText.place(x=150, y=220)

		exportStatus = Text(self, height = 1,
						width = 30,
						bg = "light yellow")
		exportStatus.place(x=150, y=255)

		# Export to CSV
		exportCSVButton = Button(self, text = "Export to CSV", command = lambda: Sqlite.exportCSV(self, results, exportedCheck))
		exportCSVButton.place(x=15, y=255)

		exportedCheck = Text(self, height = 1,
						width = 30,
						bg = "light yellow")
		exportedCheck.place(x=150, y=280)

		# Quit
		quitButton = Button(self, text = "Quit", command = lambda: self.exitProgram())
		quitButton.place(x= 180, y=350)


	def updateText(self, database, textbox, message):
		global connection

		if database != None:
			textbox.delete("1.0", "end")
			textbox.insert(END, message)
			connection = True
		else:
			textbox.delete("1.0", "end")
			textbox.insert(END, 'No database.')
			connection = False

	def getTables(self, textbox):
		if connection == True:
						
			tables = Sqlite.displayTables(self)

			textbox.delete("1.0", "end")
			textbox.insert(END, tables)

			print('Done.')
		else:
			print('No database selected.\n')

	def exitProgram(self):
		global sqliteConnection

		if sqliteConnection != None:
			sqliteConnection.close()
			print('\nSqlite3 database connection is closed.\nExiting Program.\n')
		else:
			print('Exiting Program.\n')

		root.destroy()


class Sqlite():

	def cursor_connect(self, messagebox):
		global cursor
		global database
		global sqliteConnection
		sqliteConnection = None

		ftypes = [('Sqlite Database', '*.db')]
		rootdir = 'D:\\Program Files\\DB Browser for SQLite\\databases'

		database = filedialog.askopenfilename(filetypes=ftypes, initialdir=rootdir)
		
		if database != '' or database != None:
			try:
				sqliteConnection = sqlite3.connect(database) #connect to database
				print(sqlite3.version)

				print('Connected.\n')

				cursor = sqliteConnection.cursor()
				Window.updateText(self, database, messagebox, 'Connected')

			except Error as e:
				print(e)
		else:
			print('No database selected.\n')

	def displayTables(self):
		cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
		names = list(map(' '.join, cursor.fetchall()))
		return names

	def cursor_execute(self, cursor, querybox, messagebox):
		global results
		
		query = querybox.get("1.0",END)

		if 'select' in query.lower():
			cursor.execute(query)

			header = [description[0] for description in cursor.description]
			results = cursor.fetchall()
			results.insert(0, header)

			Window.updateText(self, database, messagebox, 'Ready')

		else:
			Window.updateText(self, database, messagebox, 'Please enter a valid query.')

	def exportCSV(self, results, messagebox):
		df = pd.DataFrame(results)
		export_file_path = filesavebox()

		if export_file_path == '':
			print('\nAction cancelled.\n')
		else:
			print('\nFile exported to %s' % str(export_file_path))
			df.to_csv (export_file_path, index = False, header = False)

		Window.updateText(self, database, messagebox, 'Done')		

	def ConfirmationDialog(self, message):
		MsgBox = tk.messagebox.askquestion('Proceed?',message ,icon = 'warning')
		return(MsgBox)


if __name__ == '__main__':

	root = Tk()

	# width and heigh of root window
	w = 410 
	h = 400

	# get screen width and height
	ws = root.winfo_screenwidth() # width of the screen
	hs = root.winfo_screenheight() # height of the screen

	# calculate x and y coordinates for the Tk root window
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	# set the dimensions of the screen 
	# and where it is placed
	root.geometry('%dx%d+%d+%d' % (w, h, x, y))

	app = Window(root)
	root.mainloop()

	#cleanup
	sys.exit(0)
