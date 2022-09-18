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

from math import pi, cos, sin # needed for angle calculus

# We also need a player
# let's make a class for it
class Player:
	"""Player's characteristics
	The player has a position and a direction (angle)"""
	def __init__(self):
		self.x = 100
		self.y = 100
		self.d = 3 * pi / 2 # equivalent to 270° direction up

	def move_left(self, e):
		self.x += cos(self.d+pi/2)
		self.y += sin(self.d+pi/2)
		canvas.coord(e, (self.x-3, self.y-3), (self.x+3, self.y+3))

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
		if int(v):
			canvas.create_rectangle(j*20+1,i*20+1,(j+1)*20+1,(i+1)*20+1, fill="red") # +1 to add a thin transparent line between square

# Add a player to the scene
p1 = Player() # init player
p1_dot = canvas.create_oval((p1.x-3, p1.y-3), (p1.x+3, p1.y+3), fill="yellow")
p1_dir = canvas.create_line((p1.x, p1.y), (p1.x+cos(p1.d)*20, p1.y+sin(p1.d)*20), fill="yellow")

p1_dot.bind("<left>", p1.move_left())

canvas.pack()

window.mainloop() # Event loop (wait for user action) necessary for a script to show window