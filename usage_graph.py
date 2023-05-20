# Copyright 2023 by NST333
# All rights reserved.
# This file is the Usage Grapher (UG) source code,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

# This program shows CPU and RAM usage by percentage in matplotlib graph

import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_val = []
cpu_percentage = []
ram_percentage = []


def animate(i):
    x_val.append(i)
    cpu_percent = psutil.cpu_percent()
    ram_percent = psutil.virtual_memory().percent
    cpu_percentage.append(cpu_percent)
    ram_percentage.append(ram_percent)
    plt.cla()

    plt.subplot(211)
    plt.title("CPU" + " - " + str(cpu_percent) + "%")
    plt.plot(x_val, cpu_percentage)

    plt.subplot(212)
    plt.title("RAM" + " - " + str(ram_percent) + "%")
    plt.plot(x_val, ram_percentage)


ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.tight_layout()
plt.show()
