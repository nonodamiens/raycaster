### Main program of RAYCASTER ###
### Made by me ###
### First step : Experimentation ! ###

print("Hello my little program")

# First we need a environement
# let's try with a list
# m for wall and 0 for empty
# map size 10x10

environement = ["mmmmmmmmmm",
				"m00000000m",
				"m00000000m",
				"m00000000m",
				"m00000000m",
				"m0000m000m",
				"m00000000m",
				"m00000000m",
				"m00000000m",
				"mmmmmmmmmm",]

# ok now let's show graphicaly a map of our environement
# We need a graphical library
# let's try tkinter (the most used/famous one perhaps)

import tkinter as tk

# Initialise a window with black background
window = tk.Tk()

# Make colored squares to build environement
canvas = tk.Canvas()
canvas.configure(bg='black', width=99, height=99)
for i, row in enumerate(environement):
	for j, v in enumerate(row):
		if v == "m":
			canvas.create_rectangle(i*10+1,j*10+1,(i+1)*10+1,(j+1)*10+1, fill="red")
canvas.pack()

window.mainloop() # Event loop (wait for user action) necessary for a script to show window