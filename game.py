from tkinter import Tk, Canvas, PhotoImage, W, ALL
from bird import Bird
from pipe import Pipe
from perceptron import Perceptron
from random import randint, random
import os

FRAMERATE = 20
SCORE = -1
WIDTH = 550
HEIGHT = 700
GAP = 350

def update():
	print(len(canvas.find_all()))
	drawBirds()
	drawPipes()
	bird.update()
	predict()
	updatePipes()
	checkCollision()
	main.after(FRAMERATE, update) # Recursive function call

def drawBirds():

	for i in birds:
		bird, birdGfx = i
		x,y = bird.getPos()
		if y < 0:
			y = 0
		if y > HEIGHT:
			y = HEIGHT
		canvas.coords(birdGfx, x,y)

def predict():
	for i in birds:
		bird, gfx = i
		# Get pipe postition
		x,y,gap = obstacles[0].getPos()
		output = bird.predict( x, y, gap, height=HEIGHT, width=WIDTH )
		if output > 0.5:
			bird.jump()
	
def drawPipes():
	for pipe, gfx in zip(obstacles,pipes):
		x,y,gap = pipe.getPos()
		upper, lower = gfx
		if x < 0:
			# Reset the pipe
			pipe.setX(WIDTH)
			pipe.setY(randint(30, HEIGHT-GAP-30))
		
		canvas.coords(upper, x, 0, x+20, y)
		canvas.coords(lower, x, y+GAP, x+20, HEIGHT)
		

def updatePipes():
	for pipe in obstacles:
		pipe.update()

def checkCollision():
	for i in birds:
		bird, gfx = i
		x,y = bird.getPos()
		pipe = obstacles[0]
		px, py, gap = pipe.getPos()
		if (x > px and x < px+gap) and (y > py+gap or y < py):
			bird.die()
			birds.remove([bird, gfx])


pipes = []
obstacles = []
obstacles.append(Pipe(500, HEIGHT/2, GAP))

main = Tk()
main.resizable(width = False, height = False)
main.title("Flappy Bird")
main.geometry( '{}x{}'.format(WIDTH, HEIGHT) )
canvas = Canvas(main, width=WIDTH, height=HEIGHT)
canvas.pack()

birds = []
for i in range(100):
	bird = Bird(100, randint(50, 650))

	x, y = bird.getPos()
	img = PhotoImage(file="images/bird.gif")
	gfx = canvas.create_image(x, y,image=img)
	
	birds.append([bird, gfx])



pipes.append([canvas.create_rectangle(0,HEIGHT/3, 20, GAP, fill='green'),
				canvas.create_rectangle(0,HEIGHT/3, 20, GAP, fill='blue')])

main.after(FRAMERATE, update)
# main.bind("<space>", bird.jump) # Make neural network to press space
main.mainloop()
