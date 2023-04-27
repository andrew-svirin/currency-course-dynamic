# Main file that should be run to enter a program.

import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.figure import Figure
from currency.downloader import download_historical_course
from currency.plotter import plot_historical_courses
from datetime import datetime


def download():
    download_historical_course()
    statusLbl.config(text='Downloaded')


def plot():
    plotAx.clear()

    historical_courses = plot_historical_courses()

    for hc_id in range(len(historical_courses)):
        x_ax = []
        y_ax = []

        for xy_ax in historical_courses[hc_id]:
            x_ax.append(datetime.fromtimestamp(int(str(xy_ax[0])[:-3])))
            y_ax.append(xy_ax[1])

        if hc_id == 0:
            plt_lbl = 'Buy'
            plt_clr = 'green'
        elif hc_id == 1:
            plt_lbl = 'Sell'
            plt_clr = 'blue'
        elif hc_id == 2:
            plt_lbl = 'NBU'
            plt_clr = 'grey'
        else:
            raise ValueError("Historical course is incorrect")

        plotAx.plot_date(x_ax, y_ax, color=plt_clr, label=plt_lbl, fmt='')

    plotAx.set_xlabel("Date", fontsize=8)
    plotAx.set_ylabel("Amount", fontsize=8)
    plotAx.legend(loc="upper left")

    plotCvs.draw()
    statusLbl.config(text='Plotted')


root = tk.Tk()
root.geometry(f"800x500+200+200")
root.title('Currency')

topFrame = tk.Frame(master=root, bg="orange")
topFrame.pack(fill=tk.BOTH)

mainFrame = tk.Frame(master=root)
mainFrame.pack(fill=tk.BOTH)

btmFrame = tk.Frame(master=root, bg='grey')
btmFrame.pack(fill=tk.BOTH)

downloadBtn = tk.Button(master=topFrame, text='Download historical course', command=download)
downloadBtn.grid(column=0, row=0, sticky='E', padx=10, pady=10)

plotBtn = tk.Button(master=topFrame, text='Plot course', command=plot)
plotBtn.grid(column=1, row=0, sticky='E', padx=10, pady=10)

plotFig = Figure(figsize=(5, 4), dpi=100)
plotAx = plotFig.add_subplot(111)

plotCvs = FigureCanvasTkAgg(plotFig, master=mainFrame)
plotCvs.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
plotCvs.draw()

statusLbl = tk.Label(master=btmFrame, text='Status', bg='grey', fg='white')
statusLbl.grid(column=0, row=0, sticky='E', padx=10, pady=10)

root.mainloop()
