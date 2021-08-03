import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pathlib

def plotPressure(measure, timeline, pSP, tSP, pDP, tDP, k):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.xaxis.set_major_locator(ticker.MultipleLocator(5.0))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1.0))
    ax.grid(which = 'major', color = 'black')           
    ax.grid(which = 'minor', color = 'gray', linestyle = ':')
    ax.set(title = 'График зависимости P(t)', xlabel = 'Время, с', ylabel = 'Давление, мм.рт.ст.')

    ax.plot(timeline, k*measure, label ='')

    ax.scatter(tSP, pSP, color = 'red', marker='.', label = 'SP - Систолическое давление')
    ax.scatter(tDP, pDP, color = 'red', marker='.', label = 'DP - Диастолическое давление')
    ax.text(tSP + 0.5, pSP, 'SP = {}'.format(pSP))
    ax.text(tDP + 0.5, pDP, 'DP = {}'.format(pDP))
    ax.legend()
    
    fig.savefig('/home/pi/Desktop/marina/9-blood/Smoothed_plot_measure_{}.png'.format(pSP))

def plotCalibration(measure, timeline, level, k):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.xaxis.set_major_locator(ticker.MultipleLocator(5.0))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1.0))
    ax.grid(which = 'major', color = 'black')           
    ax.grid(which = 'minor', color = 'gray', linestyle = ':')
    ax.set(title = 'График зависимости P(t) при калибровке', xlabel = 'Время, с', ylabel = 'Отсчеты АЦП')

    ax.plot(timeline, k*measure, label ='')
    
    fig.savefig('/home/pi/Desktop/marina/9-blood/Smoothed_plot_calibration_{}.png'.format(level))

def plotPuls(measure, timeline, puls, k):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.xaxis.set_major_locator(ticker.MultipleLocator(5.0))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1.0))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(50))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
    ax.grid(which = 'major', color = 'black')           
    ax.grid(which = 'minor', color = 'gray', linestyle = ':')
    ax.set(title = 'График пульсовой волны', xlabel = 'Время, с')
    
    ax.plot(timeline, measure, label = 'Пульс {}'.format(puls))
    ax.legend()

    fig.savefig('/home/pi/Desktop/marina/9-blood/Puls_wave_{}'.format(puls))