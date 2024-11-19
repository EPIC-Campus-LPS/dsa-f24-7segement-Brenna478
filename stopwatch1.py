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


GPIO.output(Blue, GPIO.LOW)
while True: 
	if GPIO.input(Control) == GPIO.LOW:
		time.sleep(1)
		tm.write ([0, 0, 0, 0]) 
		count = 0000 
		while True:
			GPIO.output(Blue, GPIO.HIGH)
			count += 1 
			time.sleep(1)
			tm.show(str(count))
			if GPIO.input(Control) == GPIO.LOW:
				GPIO.output(Blue, GPIO.LOW)
				time.sleep(0.5) 
				break 
