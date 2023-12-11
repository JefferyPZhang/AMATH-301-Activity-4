import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

x = np.arange(35)
y = np.array([35, 34, 32, 30, 32, 35, 37, 39, 36, 35, 33, 36, 37, 40, 41, 40, 38, 37, 40, 43, 45,44, 40, 40, 42, 46, 47, 45, 43, 44, 48, 50, 51, 49, 47])
n = len(y)

plt.plot(x, y)

coeffs = np.polyfit(x, y, 1)
xplot = np.linspace(0, n, 1000)
yplot = np.polyval(coeffs, xplot)

plt.plot(xplot, yplot)

A1 = coeffs
A2 = yplot

coeffs = np.polyfit(x, y, 2)
yplot = np.polyval(coeffs, xplot)

plt.plot(xplot, yplot)

A3 = coeffs
A4 = yplot

coeffs = np.polyfit(x, y, 3)
yplot = np.polyval(coeffs, xplot)

plt.plot(xplot, yplot)

A5 = coeffs
A6 = yplot

coeffs = np.polyfit(x, y, 35)
yplot = np.polyval(coeffs, xplot)

plt.plot(xplot, yplot)

A7 = coeffs
A8 = yplot

coeff = np.array([np.pi, 1, 2/3, 30])

Sum_Squared_Error = lambda coeff: np.sum((np.abs(coeff[0] * np.cos(coeff[1] * x) + coeff[2] * x + coeff[3] - y)) ** 2)
RMS_Error = lambda coeff: np.sqrt((1 / n) * np.sum(np.abs(coeff[0] * np.cos(coeff[1] * x) + coeff[2] * x + coeff[3] - y) ** 2))
coeff_min = scipy.optimize.fmin(RMS_Error, coeff)

A9 = Sum_Squared_Error(coeff)
A10 = coeff_min
print(A10)
A11 = RMS_Error(coeff)

def f(x, coeff):
    return coeff[0] * np.cos(coeff[1] * x) + coeff[2] * x + coeff[3]
xplot = np.linspace(0,35, 1000)
yplot_rms = f(xplot, coeff_min)

A12 = yplot_rms

Ave_Error = lambda coeff: (1 / n) * np.sum(np.abs(coeff[0] * np.cos(coeff[1] * x) + coeff[2] * x + coeff[3] - y))
coeff_min = scipy.optimize.fmin(Ave_Error, coeff)
yplot_ave = f(xplot, coeff_min)

A13 = Ave_Error(coeff)
A14 = coeff_min
print(A14)
A15 = Ave_Error(coeff_min)
A16 = yplot_ave

Max_Error = lambda coeff: np.max(np.abs(coeff[0] * np.cos(coeff[1] * x) + coeff[2] * x + coeff[3] - y))
print(Max_Error)
coeff_min = scipy.optimize.fmin(Max_Error, coeff)
yplot_max = f(xplot, coeff_min)

A17 = Max_Error(coeff)
A18 = coeff_min
print(A18)
A19 = Max_Error(coeff_min)
A20 = yplot_max