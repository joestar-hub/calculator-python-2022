# -*- coding: utf-8 -*-

# @author: Elijah Ekpen Mensah



# we import python built in module
import tkinter as tk

# Get our custom module in the app folder
from app.calculate import Calculate

if __name__ == '__main__':
    master = tk.Tk()
    main = Calculate(master)
    main.start()
