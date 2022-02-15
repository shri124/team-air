from gpiozero import Servo
from time import sleep
from colors.py import getHue
import board
import adafruit_tcs34725
i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)

doorServo = Servo(17)
pushServo = Servo(27)
val = -1

# moves the ball with the servo
def moveBall():
    pushServo.min()
    sleep(.5)
    pushServo.max()
    sleep(.5)
    pushServo.min()


# opens the door of the sorting mechanism
def openDoor():
    doorServo.min()
    sleep(.5)
    doorServo.max()
    sleep(.5)
    doorServo.min()

# controls the overall mechanism to eject the ball into the holding chamber
def sortBall():
    openDoor()
    sleep(3)
    moveBall()

# Returns true if the correct color of the ball is found, else false.
def rightColor():
    pass

#main function
runSorter = True
vacuumMotor(True)
while(runSorter = True)
    if (rightColor() == True)
        sortBall()
    else
        vacuumMotor(False)
