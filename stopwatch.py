# Importing modules and classes
import time
import tm1637
import numpy as np
from pynput import keyboard
import RPi.GPIO as GPIO

 #Set the board as a bcm to use the pins warnings and warnings can be false because they are unnecessary 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Define the pins  
Control = 20
Blue = 25

#setup the light pin
GPIO.setup(Blue, GPIO.OUT)
#set up the button pin
GPIO.setup(Control, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#send power to the pins that control the display
tm = tm1637.TM1637(clk=18, dio=17)  # Using GPIO pins 18 and 17

#clear the display to start
tm.write ([0,0,0,0]) 

#add the time and ticking to the stopwatch
def stopwatch():
	numbers = 0000 #define the amound of characters that can be displayed by the stopwatch
	while GPIO.input(Control) == GPIO.HIGH: #When the button is not pressed tick the stopwatch up by one
		numbers += 1 
		
		tm.show(str(numbers)) #makes the display show the numbers 
		time.sleep(1) #the speed of changing the numbers 
#define the light
def light():
	GPIO.output(Blue, GPIO.LOW) #Starting low so the light is off 
	time.sleep(2) #sleeping allows the light to be controlled by something, in this case the button 
	GPIO.output(Blue, GPIO.HIGH) #Ending high so that the light is only on when the button is low 
	
while True: #this function causing the code to only run if the button is pushed 
	if GPIO.input(Control) == GPIO.LOW: #The button must be low then high then low to run the code
		light() #start the light when the stopwatch starts 
		tm.write([0,0,0,0]) #make sure the display starts empty
		stopwatch() #callthe stopwatch function to start by the button 

