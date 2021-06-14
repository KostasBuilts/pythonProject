import matplotlib.pyplot as plt
import numpy as nmp
import random as rnd

class plnm:
    defused = 0

red = '#ff0000'
green = '#00ff00'
blue = '#0000ff'
cyan = '#00ffff'
purpl = '#5900b3'
magenta = '#ff00ff'
pink = '#ff99ff'
yellow = '#ffff00'
Lightgreen = '#66ff33'
orange = '#e67300'
black = '#000000'

def rndcolor():
    _randomnum = rnd.randrange(0, 10)
    if (_randomnum == 0):
        return red

    if (_randomnum == 1):
        return green

    if (_randomnum == 2):
        return blue

    if (_randomnum == 3):
        return cyan

    if (_randomnum == 4):
        return purpl

    if (_randomnum == 5):
        return magenta

    if (_randomnum == 6):
        return pink

    if (_randomnum == 7):
        return yellow

    if (_randomnum == 8):
        return Lightgreen

    if (_randomnum == 9):
        return orange

    if (_randomnum == 10):
        return black



def powercalc(power, colur):

    x = 0
    y = 0
    z = 0
    f = 0

    plnm.defused +=1

    array = []
    array2 = []
    array3 = []
    array4 = []

    if (plnm.defused == 1):
        for x in range(100000):
            array.insert(x, pow(x, power))
            plt.subplot(1, 1, 1)
            plt.plot(array, c=colur)
            converted_power = str(power)
            plt.title("to the power of " + converted_power)
            plt.grid()

    if (plnm.defused == 2):
        for x in range(100000):
            array2.insert(y, pow(y, power))
            plt.subplot(1, 2, 2)
            plt.plot(array2, c=colur)
            converted_power = str(power)
            plt.title("to the power of " + converted_power)
            plt.grid()

    if (plnm.defused == 4):
        for x in range(100000):
            array3.insert(z, pow(z, power))
            plt.subplot(2, 2, 3)
            plt.plot(array3, c=colur)
            converted_power = str(power)
            plt.title("to the power of " + converted_power)
            plt.grid()

    if (plnm.defused == 5):
        for x in range(100000):
            array4.insert(f, pow(f, power))
            plt.subplot(2, 2, 4)
            plt.plot(array4, c=colur)
            converted_power = str(power)
            plt.title("to the power of " + converted_power)
            plt.grid()
    print (plnm.defused)


powercalc(0.3, rndcolor())
plt.show()