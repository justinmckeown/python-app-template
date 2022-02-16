import logging
import tkinter as tk
from tkinter import ttk
from tkinter import  Tk, Label, LabelFrame, Button, Entry, W, N, E, S, X,Y, Frame, LEFT, RIGHT, CENTER, Text, messagebox, Scrollbar, StringVar, OptionMenu, PhotoImage
from tkinter import ttk
from tkinter.ttk import *
from tkinter.filedialog import askdirectory
import threading

logger = logging.getLogger()

class RootViewController(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('My App title')
        self.minsize(750, 500)
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.file_count_display: int = 0