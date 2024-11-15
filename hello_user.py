# Importing modules and the only the neccesary modules for this process
import tm1637
import time


# Create the 4 digit display and which pins power the display
tm = tm1637.TM1637(clk=18, dio=17)  # Using GPIO pins 18 and 17
clear = [0, 0, 0, 0]  # Defining values used to clear the display

# Set up what the display is supposed to show 
s = input("What is your name? ") 
#Make sure that the display is clear before sending the text to display 
tm.write(clear)
time.sleep(1)
# create a value to display "hello" 
h = ("hello")
#using two functions to display the input and "hello" is neccessary
tm.scroll (h, delay=250)
tm.scroll(s, delay=250)
#use the sleep function to end the display after 2 seconds
time.sleep(2)
