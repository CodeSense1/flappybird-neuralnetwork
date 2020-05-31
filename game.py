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
	print("Update loop\n")
	if len(list(filter(lambda i: i[0].alive, birds))) == 0:
		map(lambda b, g: b.resurrect(), birds)
	drawBirds()
	drawPipes()
	updateBirds()
	predict()
	updatePipes()
	checkCollision()
	main.after(FRAMERATE, update) # Recursive function call

def updateBirds():
	for i in filter(lambda i: i[0].alive, birds):
		bird, gfx = i
		bird.update()

def drawBirds():

	for i in filter(lambda i: i[0].alive, birds):
		bird, birdGfx = i
		print(birdGfx)
		x,y = bird.getPos()
		if y < 0:
			y = 0
		if y > HEIGHT:
			y = HEIGHT
		canvas.coords(birdGfx, x,y, x+10, y+10)

def predict():
	for i in filter(lambda i: i[0].alive, birds):
		bird, gfx = i
		# Get pipe postition
		x,y,gap = obstacles[0].getPos()
		output = bird.predict( x, y, gap, height=HEIGHT, width=WIDTH )
		if output > 0.9:
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
	for i in filter(lambda i: i[0].alive, birds):
		bird, gfx = i
		x,y = bird.getPos()
		pipe = obstacles[0]
		px, py, gap = pipe.getPos()
		if (x > px and x < px+gap) and (y > py+gap or y < py):
			bird.die()
			canvas.delete(gfx)


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
	y = y+random()*HEIGHT
	gfx = canvas.create_rectangle(x, y,x+10, y+10, fill="orange")
	
	birds.append([bird, gfx])



pipes.append([canvas.create_rectangle(0,HEIGHT/3, 20, GAP, fill='green'),
				canvas.create_rectangle(0,HEIGHT/3, 20, GAP, fill='green')])

main.after(FRAMERATE, update)
# main.bind("<space>", bird.jump) # Make neural network to press space
main.mainloop()
