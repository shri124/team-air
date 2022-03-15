from time import sleep
from statistics import mean
import numpy as np

# these are the values we get from testing
red = (74, 5, 3)
orange = (67, 8, 2)
yellow = (27, 27, 2)
green = (8, 41, 7)
blue = (2, 18, 47)
purple = (13, 11, 27)
pink = (43, 6, 1)

# convert rgb to hue
def getHue(color_rgb):
    R = color_rgb[0] / 255
    G = color_rgb[1] / 255
    B = color_rgb[2] / 255

    new_rgb = (R, G, B)

    max = -1
    max_index = -1
    min = 256
    for i in range(3):
        if (new_rgb[i] > max):
            max = new_rgb[i]
            max_index = i
        if (new_rgb[i] < min):
            min = new_rgb[i]

    hue = -1
    if (max_index == 0):
        hue = (G-B)/(max-min)
    elif (max_index == 1):
        hue = 2.0 + (B-R)/(max-min)
    elif (max_index == 2):
        hue = 4.0 + (R-G)/(max-min)

    hue *= 60
    if hue < 0:
        hue += 360
    return hue

# get the hue and temp from the color sensor
def readColorSensor(sensor):
    hue = round(getHue(sensor.color_rgb_bytes))
    temp = round(sensor.color_temperature)
    return hue, temp

# read color 10 times, get the average, then return a string color depending on hue and temp values
def getBallColor(sensor):
    rgbReadings = []

    print("getting average...")

    for i in range(10):
        rgbReadings.append(sensor.color_rgb_bytes)
        sleep(0.1)
    
    print("done")

    rgbAverage = np.mean(rgbReadings, axis=0)

    return getClosestColor(rgbAverage)

def getClosestColor(rgbAverage):
    pass