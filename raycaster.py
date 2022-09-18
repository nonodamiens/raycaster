### Main program of RAYCASTER ###
### Made by me ###
### First step : Experimentation ! ###

# First we need a environement
# let's try with a list
# 1 for wall and 0 for empty
# map size 10x10

environement = ["1111111111",
				"1001000001",
				"1001000001",
				"1000000001",
				"1000001001",
				"1000000001",
				"1000000001",
				"1000000001",
				"1000000001",
				"1111111111",]

# We also need a player
# let's make a class for it
class Player:
	"""Player's characteristics
	The player has a position and a method to change position"""
	def __init__(self):
		self.x = 50
		self.y = 50

	def move(self, dx, dy):
		self.x = self.x + dx
		self.y = self.y + dy

# ok now let's show graphicaly a map of our environement
# We need a graphical library
# let's try tkinter (the most used/famous one perhaps)

import tkinter as tk

# Initialise a window with black background
window = tk.Tk()

# Make colored squares to build environement
canvas = tk.Canvas()
canvas.configure(bg='black', width=200, height=200)
for i, row in enumerate(environement):
	for j, v in enumerate(row):
		# print("coordinates :", i, j, v)
		if int(v):
			canvas.create_rectangle(j*20+1,i*20+1,(j+1)*20+1,(i+1)*20+1, fill="red")
		# if v == "p":
		# 	canvas.create_oval(j*10+1,i*10+1,(j+1)*10+1,(i+1)*10+1, fill="white")
		# 	canvas.create_line(j*10+6,i*10+1,j*10+6,(i+1)*10+1, fill="blue")

canvas.pack()

window.mainloop() # Event loop (wait for user action) necessary for a script to show window