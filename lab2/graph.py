import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
import statsmodels.api as sm
import math
import numpy
import plotly.graph_objs as go

title = ""


def getPoints(x1, y1, x2, y2):
    xval = []
    yval = []
    xval.append(0)
    yval.append(0)
    for a in range(-10, 10):
        for b in range(-10, 10):
            xnew = a * x1 + b * x2
            xval.append(xnew)
            ynew = a * y1 + b * y2
            yval.append(ynew)
    return xval, yval


x1 = 2
y1 = 1
x2 = 3
y2 = -1

print("x1=" + str(x1) + ",y1=" + str(y1) + "x2=" + str(x2) + ",y2=" + str(y2))
print()

xval, yval = getPoints(x1, y1, x2, y2)

plt.title(title)
plt.xlabel('x')
plt.ylabel('y')
plt.axis([0, max(xval) / 2, 0, max(yval) / 2])

plt.scatter(xval, yval)

plt.show()
