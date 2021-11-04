#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

np.random.seed(20200802)
x = np.random.rand(50) * 3 + 0.5
y = np.random.rand(50) * 3 + 0.5

#fig, ax = plt.subplots()
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

ax.scatter(x, y)
#ax.scatter(x, y, marker='s')

fig.suptitle('Anatomy of a Figure')

ax.set_xlim([0, 4])
ax.set_ylim([0, 4])

ax.xaxis.set_major_locator(mticker.MultipleLocator(1))
ax.xaxis.set_major_formatter(mticker.FormatStrFormatter('%d'))
ax.xaxis.set_minor_locator(mticker.MultipleLocator(0.25))
ax.xaxis.set_minor_formatter(mticker.FormatStrFormatter('%.2f'))
ax.yaxis.set_major_locator(mticker.MultipleLocator(1))
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%d'))
ax.yaxis.set_minor_locator(mticker.MultipleLocator(0.25))
ax.yaxis.set_minor_formatter(mticker.FormatStrFormatter('%.2f'))

ax.set_xlabel('X axis label')
ax.set_ylabel('Y axis label')

ax.xaxis.grid(True, which='major', linestyle='--')
ax.yaxis.grid(True, which='major', linestyle='--')

def minor_skip_format(val, pos):
    if val % 1 == 0:
        return ''
    else:
        return '%.2f' % val

ax.xaxis.set_minor_formatter(mticker.FuncFormatter(minor_skip_format))
ax.yaxis.set_minor_formatter(mticker.FuncFormatter(minor_skip_format))

ax.tick_params(which='major', length=8)

X = np.linspace(0.5, 3.5, 100)
Y1 = 3+np.cos(X)
Y2 = 1+np.cos(1+X/0.75)/2
ax.plot(X, Y1, 'b-', label="Blue signal")
ax.plot(X, Y2, 'r--', label="Red signal")
ax.legend()

plt.show()
