# Importing modules and classes
import time
import tm1637
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
tm = tm1637.TM1637(clk=17, dio=13)  # Using GPIO pins 18 and 17
tm.write([0,0,0,0])
tm.brightness(7)
time.sleep(1)

#turn the light off to start 
GPIO.output(Blue, GPIO.LOW)
#while the code has power 
while True: 
	#if the button is pressed 
	if GPIO.input(Control) == GPIO.LOW:
		#wait one second for the timer to start 
		time.sleep(1)
		#show how many variables can be displayed
		tm.write ([0, 0, 0, 0]) 
		#define count
		count = 0000 
		#while this program is running
		while True:
			#turn the light on
			GPIO.output(Blue, GPIO.HIGH)
			#have the stopwatch tick up
			count += 1 
			#only tick up once per second
			time.sleep(1)
			#show the count on the display 
			tm.show(str(count))
			#when the button is pressed again 
			if GPIO.input(Control) == GPIO.LOW:
				#turn off the light
				GPIO.output(Blue, GPIO.LOW)
				#take into account the button kick back
				time.sleep(0.5) 
				#break back to the first while true
				break 
