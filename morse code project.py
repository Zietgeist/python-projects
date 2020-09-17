#library imports
import morse
import RPi.GPIO as GPIO
import time

# set GPIO numbering 
GPIO.setmode(GPIO.BCM)

# the pin number (choose another pin if 27 is occupied by another device)
RedbuttonPin = 26      #red button is g26
GreenbuttonPin =13     #Green button is at g13
BluebuttonPin =16      #blue button is at g16
YellowbuttonPin = 17   #yellow button is g17

# setup LED
LEDPin = 27
GPIO.setup(LEDPin, GPIO.OUT)

# use an internal pull-down resistor - returns 0 when the button is released
GPIO.setup(RedbuttonPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(GreenbuttonPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(YellowbuttonPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(BluebuttonPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

print(str(GPIO.input(RedbuttonPin)) + " 1 = button is pressed. 0= button is not pressed")

# store your message
GreenbuttonMessage = 'Hello world!'
RedbuttonMessage = "SOS"
BluebuttonMessage = "The quick brown fox jumped over the lazy dog"
YellowbuttonMessage = 'break' 

#morse flashing
def morseFlash():
    # setup LED
    LEDPin = 27
    GPIO.setup(LEDPin, GPIO.OUT)
    
    myUpperMessage = myMessage.upper() #convert to upper case
    characters = list(myUpperMessage)  #convert to a list

    for i in range (len(characters)):
        j = characters [i]
        
        if j == ' ':
            k = (' ')
        elif j == '!':
            k = '.'
        else:
            k = (morse.code()[j])
        
            if k == '.':
                GPIO.output(LEDpin, True)
                time.sleep(.1)
                GPIO.output(LEDPin, False)
                time.sleep(.1)
            
            if k == '-':
                GPIO.output(LEDpin, True)
                time.sleep(.3)
                GPIO.output(LEDPin, False)
                time.sleep(.1)
            
    



for i in range(5):
    
    GPIO.output(LEDPin, True)   # turn on
    time.sleep(0.2)             # wait
    GPIO.output(LEDPin, False)  # turn off
    time.sleep(0.2)             # wait, then repeat

while True:
    print("press a button within 5 seconds")
    time.sleep(5)
    
    if GPIO.input(RedbuttonPin) == 1:
        myMessage = (RedbuttonMessage)
        morseFlash()
        break
    
    elif GPIO.input(GreenbuttonPin) ==1:
        myMessage = (GreenbuttonMessage)
        morseFlash()
        break
    
    elif GPIO.input(YellowbuttonPin) ==1:
        myMessage = (YellowbuttonMessage)
        morseFlash()
        break
    
    elif GPIO.input(BluebuttonPin) ==1:
        myMessage = (BluebuttonMessage)
        morseFlash()
        break
    
    else:
       
        break
        
    
# clean-up GPIO
GPIO.cleanup()
