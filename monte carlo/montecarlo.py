import random
import math
import matplotlib.pyplot as plot
    
def monte_carlo(func, a, b, n, m): # Monte Carlo method implementation
    c = 0

    for _ in range(n):
        x = a + (b - a) * random.uniform(0, 1) # Rescaling random numbers from [0,1] to [a,b]; Python language, to generate random numbers, uses Mersenne Twister algorithm by default, so there is no need to implement it 
        y = m * random.uniform(0, 1) # Rescaling random numbers from [0,1] to [0,m]

        if func == pi: # Condition checking for the pi function
            if (((y - 1) ** 2) + ((x - 1) ** 2)) <= 1:
                c += 1
        elif y <= func(x): # Condition checking for root, sinus, and function functions
            c += 1

    integral_approx = (c / n) * (b - a) * m # Estimating the integral using the Monte Carlo method
    return integral_approx

def root(x):
    return x ** (1/3)

def sinus(x):
    return math.sin(x)

def function(x):
    return 4 * x * ((1-x) ** 3)
    
def pi(x): # Function to calculate the value of pi (constant function always returning 1)
    return 1

a_values = [0, 0, 0, 0] #List of lower bounds
b_values = [8, math.pi, 1, 2] #List of upper bounds
functions = [root, sinus, function, pi] #List of functions
exact_integrals = [12, 2, 0.2, math.pi] #List of exact integral values 
max = [2, 1, 0.43, 2] #List of maximums used in monte carlo method

n_values = list(range(50, 5050, 50)) #List of n for which we execute monte carlo method
k = 50 #iterator

for index, func in enumerate(functions): # Iterate through each function and generate plots
    plot.figure(figsize=(10,6))
    plot.xlabel('number of points (n)')
    plot.ylabel('integral value')

    integral_average = []

    for n in n_values:

        approximation = []

        for _ in range(k):
            approx = monte_carlo(func, a_values[index], b_values[index], n, max[index]) # Calculate the approximated integral value using Monte Carlo
            approximation.append(approx)

        plot.plot([n] * k, approximation, 'o', color='xkcd:green', markersize=2)
        average = sum(approximation)/k
        integral_average.append(average)

    plot.plot(n_values, integral_average, 'o', color='xkcd:coral',  markersize=5)
    plot.axhline(y = exact_integrals[index], color='darkblue', lw=2)
plot.show()  # Display the generated plots



