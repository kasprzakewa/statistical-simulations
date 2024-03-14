import math
import matplotlib.pyplot as plt
import numpy as np

xaxis_average1=[]
xaxis1 = []
plot1 = []
average1 = []

xaxis_average2 = []
xaxis2 = []
plot2 = []
average2 = []

function1 = []
function2 = []

def func1(n):
    return math.log(n)/math.log(math.log(n))

def func2(n):
    return math.log(math.log(n))/math.log(2)

with open('data.txt', 'r') as file:
    data = file.read()

lines = data.split('\n')

for line in lines:
    if not line:
        continue
    nums = line.split(" ")
    if "." in line:
        xaxis_average1.append(int(nums[0]))
        average1.append(float(nums[1]))
    else:
        xaxis1.append(int(nums[0]))
        plot1.append(int(nums[1])) 

for i in range(len(average1)):
    function1.append(average1[i] / func1(xaxis_average1[i])) 

fig1, ax1 = plt.subplots()
fig3, ax3 = plt.subplots()

ax1.scatter(xaxis1, plot1, marker='o', color='hotpink', s=2, label="powtórzenia")
ax1.scatter(xaxis_average1, average1, marker='o', color='darkblue', s=15, label="średnia $L_n$")
ax1.set_xlabel("$n$ wartości")
ax1.set_ylabel("wyniki symulacji")
ax1.set_title("zachowanie $L_n$ wraz z rosnącym $n$")
ax1.legend()

ax3.plot(xaxis_average1, function1, marker='o', linestyle='-', color='darkblue', markersize=3, label="średnia $\\frac{L_n}{\\frac{\ln(n)}{\ln(\ln(n))}}$")
ax3.set_xlabel("średnie wartości dla $L_n$")
ax3.set_ylabel("wyniki")
ax3.set_title("skalowanie $\\frac{L_n}{\\frac{\ln(n)}{\ln(\ln(n))}}$ wraz z rosnącą średnią $L_n$")
ax3.legend()


with open('data1.txt', 'r') as file:
    data = file.read()

lines = data.split('\n')

for line in lines:
    if not line:
        continue
    nums = line.split(" ")
    if "." in line:
        xaxis_average2.append(int(nums[0]))
        average2.append(float(nums[1]))
    else:
        xaxis2.append(int(nums[0]))
        plot2.append(int(nums[1]))  

for i in range(len(average2)):
    function2.append(average2[i] / func2(xaxis_average2[i]))

fig2, ax2 = plt.subplots()
fig4, ax4 = plt.subplots()

ax2.scatter(xaxis2, plot2, marker='o', color='hotpink', s=2, label="powtórzenia")
ax2.scatter(xaxis_average2, average2, marker='o', color='darkblue', s=15, label="średnia $L_n$")
ax2.set_xlabel("$n$ wartości")
ax2.set_ylabel("wyniki symulacji")
ax2.set_title("zachowanie $L_n$ wraz z rosnącym $n$")
ax2.legend()

ax4.plot(xaxis_average2, function2, marker='o', linestyle='-', color='darkblue', markersize=3, label="średnia $\\frac{L_n}{\\frac{\ln(\ln(n))}{\ln(2)}}$")
ax4.set_xlabel("średnie wartości dla $L_n$")
ax4.set_ylabel("wyniki")
ax4.set_title("skalowanie $\\frac{L_n}{\\frac{\ln(\ln(n))}{\ln(2)}}$ wraz z rosnącą średnią $L_n$")
ax4.legend()

plt.show()

