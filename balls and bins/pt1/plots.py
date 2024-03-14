import math
import matplotlib.pyplot as plt
import numpy as np

n_values = np.linspace(1000, 101000, 100)
xaxis = []
plot1 = []
plot2 = []
plot3 = []
plot4 = []
plot5 = []
average1 = []
average2 = []
average3 = []
average4 = []
average5 = []
b1 = []
b2 = []
u1 = []
c1 = []
c2 = []
c3 = []
d1 = []
d2 = []
d3 = []
dc1 = []
dc2 = []
dc3 = []

with open('data.txt', 'r') as file:
    data = file.read()

lines = data.split('\n')

for line in lines:
    if not line:
        continue
    nums = line.split(" ")
    if "." in line:
        average1.append(float(nums[1]))
        average2.append(float(nums[2]))
        average3.append(float(nums[3]))
        average4.append(float(nums[4]))
        average5.append(float(nums[5])) 
    else:
        xaxis.append(int(nums[0]))
        plot1.append(int(nums[1]))
        plot2.append(int(nums[2]))
        plot3.append(int(nums[3]))
        plot4.append(int(nums[4]))
        plot5.append(int(nums[5]))  

for i in range(len(average1)):
    b1.append(average1[i] / n_values[i])

for i in range(len(average1)):
    b2.append(average1[i] / math.sqrt(n_values[i]))

for i in range(len(average2)):
    u1.append(average2[i] / n_values[i])

for i in range(len(average3)):
    c1.append(average3[i] / n_values[i])

for i in range(len(average3)):
    c2.append(average3[i] / (n_values[i] * math.log(n_values[i])))

for i in range(len(average3)):
    c3.append(average3[i] / (n_values[i] ** 2))

for i in range(len(average4)):
    d1.append(average4[i] / n_values[i])

for i in range(len(average4)):
    d2.append(average4[i] / (n_values[i] * math.log(n_values[i])))

for i in range(len(average4)):
    d3.append(average4[i] / (n_values[i] ** 2))

for i in range(len(average5)):
    dc1.append(average5[i] / n_values[i])

for i in range(len(average4)):
    dc2.append(average5[i] / (n_values[i] * math.log(n_values[i])))

for i in range(len(average4)):
    dc3.append(average4[i] / (n_values[i] * math.log(math.log(n_values[i]))))


fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()
fig4, ax4 = plt.subplots()
fig5, ax5 = plt.subplots()
fig6, ax6 = plt.subplots()
fig7, ax7 = plt.subplots()
fig8, ax8 = plt.subplots()
fig9, ax9 = plt.subplots()
fig10, ax10 = plt.subplots()
fig11, ax11 = plt.subplots()
fig12, ax12 = plt.subplots()
fig13, ax13 = plt.subplots()
fig14, ax14 = plt.subplots()
fig15, ax15 = plt.subplots()
fig16, ax16 = plt.subplots()
fig17, ax17 = plt.subplots()

ax1.scatter(xaxis, plot1, marker='o', color='xkcd:lightblue', s=2, label="powtórzenia")
ax1.scatter(n_values, average1, marker='o', color='xkcd:purple', s=15, label="średnia $B_n$")
ax1.set_xlabel("$n$ wartości")
ax1.set_ylabel("wyniki symulacji")
ax1.set_title("zachowanie $B_n$ wraz z rosnącym $n$")
ax1.legend()

ax2.scatter(xaxis, plot2, marker='o', color='xkcd:lightblue', s=2, label="powtórzenia")
ax2.scatter(n_values, average2, marker='o', color='xkcd:purple', s=15, label="średnia $U_n$")
ax2.set_xlabel("$n$ wartości")
ax2.set_ylabel("wyniki symulacji")
ax2.set_title("zachowanie $U_n$ wraz z rosnącym $n$")
ax2.legend()

ax3.scatter(xaxis, plot3, marker='o', color='xkcd:lightblue', s=2, label="powtórzenia")
ax3.scatter(n_values, average3, marker='o', color='xkcd:purple', s=15, label="średnia $C_n$")
ax3.set_xlabel("$n$ wartości")
ax3.set_ylabel("wyniki symulacji")
ax3.set_title("zachowanie $C_n$ wraz z rosnącym $n$")
ax3.legend()

ax4.scatter(xaxis, plot4, marker='o', color='xkcd:lightblue', s=2, label="powtórzenia")
ax4.scatter(n_values, average4, marker='o', color='xkcd:purple', s=15, label="średnia $D_n$")
ax4.set_xlabel("$n$ wartości")
ax4.set_ylabel("wyniki symulacji")
ax4.set_title("zachowanie $D_n$ wraz z rosnącym $n$")
ax4.legend()

ax5.scatter(xaxis, plot5, marker='o', color='xkcd:lightblue', s=2, label="powtórzenia")
ax5.scatter(n_values, average5, marker='o', color='xkcd:purple', s=15, label="średnia $(D_n - C_n)$")
ax5.set_xlabel("$n$ wartości")
ax5.set_ylabel("wyniki symulacji")
ax5.set_title("różnica między $D_n$ a $C_n$ wraz z rosnącym $n$")
ax5.legend()

ax6.scatter(n_values, b1, marker='o', color='xkcd:purple', s=15, label="średnia $\\frac{B_n}{n}$")
ax6.set_xlabel("średnie wartości dla $B_n$")
ax6.set_ylabel("wyniki")
ax6.set_title("skalowanie $\\frac{B_n}{n}$ wraz z rosnącą średnią $B_n$")
ax6.legend()

ax7.scatter(n_values, b2, marker='o', color='xkcd:purple', s=15, label="średnia $\\frac{B_n}{\sqrt{n}}$")
ax7.set_xlabel("średnia wartość dla $B_n$")
ax7.set_ylabel("wyniki")
ax7.set_title("skalowanie $\\frac{B_n}{\sqrt{n}}$ wraz z rosnącą średnią $B_n$")
ax7.legend()

ax8.scatter(n_values, u1, marker='o', color='xkcd:purple', s=15, label="średnia $\\frac{U_n}{n}$")
ax8.set_xlabel("średnia wartość dla $U_n$")
ax8.set_ylabel("wyniki")
ax8.set_title("skalowanie $\\frac{U_n}{n}$ wraz z rosnącą średnią $U_n$")
ax8.legend()

ax9.scatter(n_values, c1, marker='o', color='xkcd:purple', s=15, label="średnia $\\frac{C_n}{n}$")
ax9.set_xlabel("średnia wartość dla $C_n$")
ax9.set_ylabel("wyniki")
ax9.set_title("skalowanie $\\frac{C_n}{n}$ wraz z rosnącą średnią $C_n$")
ax9.legend()

ax10.scatter(n_values, c2, marker='o', color='xkcd:purple', s=15, label="średnia $\\frac{C_n}{n\ln(n)}$")
ax10.set_xlabel("średnia wartość dla $C_n$")
ax10.set_ylabel("wyniki")
ax10.set_title("skalowanie $\\frac{C_n}{n\ln(n)}$ wraz z rosnącą średnią $C_n$")
ax10.legend()

ax11.scatter(n_values, c3, marker='o', color='xkcd:purple', s=15, label="średnia $\\frac{C_n}{n^2}$")
ax11.set_xlabel("średnia wartość dla $C_n$")
ax11.set_ylabel("wyniki")
ax11.set_title("skalowanie $\\frac{C_n}{n^2}$ wraz z rosnącą średnią $C_n$")
ax11.legend()

ax12.scatter(n_values, d1, marker='o', color='xkcd:purple', s=15, label="średnia $\\frac{D_n}{n}$")
ax12.set_xlabel("średnia wartość dla $D_n$")
ax12.set_ylabel("wyniki")
ax12.set_title("skalowanie $\\frac{D_n}{n}$ wraz z rosnącą średnią $D_n$")
ax12.legend()

ax13.scatter(n_values, d2, marker='o', color='xkcd:purple', s=15, label="średnia $\\frac{D_n}{n\ln(n)}$")
ax13.set_xlabel("średnia wartość dla $D_n$")
ax13.set_ylabel("wyniki")
ax13.set_title("skalowanie $\\frac{D_n}{n\ln(n)}$ wraz z rosnącą średnią $D_n$")
ax13.legend()

ax14.scatter(n_values, d3, marker='o', color='xkcd:purple', s=15, label="średnia $\\frac{D_n}{n^2}$")
ax14.set_xlabel("średnia wartość dla $D_n$")
ax14.set_ylabel("wyniki")
ax14.set_title("skalowanie $\\frac{D_n}{n^2}$ wraz z rosnącą średnią $D_n$")
ax14.legend()

ax15.scatter(n_values, dc1, marker='o', color='xkcd:purple', s=15, label="średnia $\\frac{(D_n - C_n)}{n}$")
ax15.set_xlabel("średnia $\\frac{(D_n - C_n)}{n}$")
ax15.set_ylabel("wyniki")
ax15.set_title("skalowanie $\\frac{(D_n - C_n)}{n}$ wraz z rosnącą średnią $(D_n - Cn)$")
ax15.legend()

ax16.scatter(n_values, dc2, marker='o', color='xkcd:purple', s=15, label="średnia $\\frac{(D_n - C_n)}{n\ln(n)}$")
ax16.set_xlabel("średnia $\\frac{(D_n - C_n)}{n\ln(n)}$")
ax16.set_ylabel("wyniki")
ax16.set_title("skalowanie $\\frac{(D_n - C_n)}{n\ln(n)}$ wraz z rosnącą średnią $(D_n - C_n)$")
ax16.legend()

ax17.scatter(n_values, dc3, marker='o', color='xkcd:purple', s=15, label="średnia $\\frac{(D_n - C_n)}{n\ln(\ln(n))}$")
ax17.set_xlabel("średnia $\\frac{(D_n - C_n)}{n\ln(\ln(n))}$")
ax17.set_ylabel("wyniki")
ax17.set_title("skalowanie $\\frac{(D_n - C_n)}{n\ln(\ln(n))}$ wraz z rosnącą średnią $(D_n - C_n)$")
ax17.legend()

plt.show()
