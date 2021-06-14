import matplotlib.pyplot as plt
import numpy as nmp

x = 0
arr = []
x2 = 0
arr2 = []

def powercalc(rng,power,powerint,array,colur,powof,rows,colmns,plotnum):
    for powerint in range(rng):
        array.insert(powerint, pow(powerint, power))
    plt.subplot(rows, colmns, plotnum)
    plt.plot(array, c = colur)
    plt.title("to the power of " + powof)


num = 10
converted_num = str(num)
powercalc(2222, 4, x, arr,'#ff0088',converted_num,1,2,1)
plt.grid()
powercalc(100, 2, x2, arr2,'#00ffff',"2",1,2,2)
plt.grid()
plt.show()