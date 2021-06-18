import matplotlib.pyplot as plt
import random as rnd

class plnm:
    defused = 0

class arrnum:
    array = []
    array2 = []
    array3 = []
    array4 = []
    _power = ""
    _power2 = ""
    _power3 = ""
    _power4 = ""
    colur = ""
    colur2 = ""
    colur3 = ""
    colur4 = ""


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

    x = 1
    y = 0
    z = 0
    f = 0

    plnm.defused +=1



    if (plnm.defused == 1):
        for x in range(100000): #How many points the graph will have
            arrnum.array.insert(x, pow(x, power)) #filling the array with the mantatory values
        plt.grid() #turning the grid on
        plt.subplot(1, 1, 1) #cteating a subplot witch in this case is not a sub plot because the function in used only one time
        arrnum.colur = colur
        plt.plot(arrnum.array, c= arrnum.colur) #ploting the graph and giving it the color of choice
        arrnum._power = str(power) #converting an integer to a string so that we can print it
        plt.title("to the power of " + arrnum._power) #giving the plot a name to show


    if (plnm.defused == 2):
        for y in range(100000):
            arrnum.array2.insert(y, pow(y, power))
        plt.subplot(1, 2, 1)
        plt.plot(arrnum.array, c= arrnum.colur)
        plt.grid()
        plt.title("to the power of " + arrnum._power)
        plt.subplot(1, 2, 2)
        arrnum.colur2 = colur
        plt.plot(arrnum.array2, c= arrnum.colur2)
        arrnum._power2 = str(power)
        plt.title("to the power of " + arrnum._power2)
        plt.grid()

    if (plnm.defused == 3):
        for z in range(100000):
            arrnum.array3.insert(z, pow(z, power))
        plt.subplot(2, 2, 1)
        plt.plot(arrnum.array, c=arrnum.colur)
        plt.grid()
        plt.title("to the power of " + arrnum._power)
        plt.subplot(2, 2, 2)
        plt.plot(arrnum.array2, c=arrnum.colur2)
        plt.title("to the power of " + arrnum._power2)
        plt.grid()
        plt.subplot(2, 2, 3)
        arrnum.colur3 = colur
        plt.plot(arrnum.array3, c= arrnum.colur3)
        arrnum._power3 = str(power)
        plt.title("to the power of " + arrnum._power3)
        plt.grid()

    if (plnm.defused == 4):
        for f in range(100000):
            arrnum.array4.insert(f, pow(f, power))
        plt.subplot(2, 2, 1)
        plt.plot(arrnum.array, c=arrnum.colur)
        plt.title("to the power of " + arrnum._power)
        plt.subplot(2, 2, 2)
        plt.plot(arrnum.array2, c=arrnum.colur2)
        plt.title("to the power of " + arrnum._power2)
        plt.subplot(2, 2, 3)
        plt.plot(arrnum.array3, c=arrnum.colur3)
        plt.title("to the power of " + arrnum._power3)
        plt.subplot(2, 2, 4)
        arrnum.colur4 = colur
        plt.plot(arrnum.array4, c= arrnum.colur4)
        arrnum._power4 = str(power)
        plt.title("to the power of " + arrnum._power4)
        plt.grid()
    print (plnm.defused)


powercalc(2, rndcolor())
powercalc(4, rndcolor())
powercalc(0.3, rndcolor())
powercalc(0.5, rndcolor())
plt.show()