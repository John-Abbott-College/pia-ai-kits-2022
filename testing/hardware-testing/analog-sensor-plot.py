# References
# Graph Sensor Data with Python and Matplotlib by Sparkfun
# https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/all

# Matplotlib Tutorial (Part 9): Plotting Live Data in Real-Time
# https://www.youtube.com/watch?v=Ercd-Ip5PfQ

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from itertools import count
from grove.adc import ADC

# Address must be specified to work with Base Hat. See issue below
# https://github.com/Seeed-Studio/grove.py/issues/64
adc = ADC(address = 0x04)

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

xs = []
ys = []
counter = count()

# This function is called periodically from FuncAnimation


def animate(i, xs, ys):

    # Read voltage from Pi Hat
    volt = adc.read_voltage(2)

    # Add x and y to lists
    xs.append(next(counter))
    ys.append(volt)

    # Limit x and y lists to 50 items
    xs = xs[-50:]
    ys = ys[-50:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.subplots_adjust(bottom=0.30)
    ax.set_title(f'Current value: {volt}')
    plt.xlabel('Sample number')
    plt.ylabel('Volt digital reading')


# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=50)
plt.show()
