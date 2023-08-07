import logging
import tkinter as tk
from tkinter import ttk
from tkinter import  Tk, Label, LabelFrame, Button, Entry, W, N, E, S, X,Y, NE, TOP, Frame, LEFT, RIGHT, CENTER, Text, messagebox, Scrollbar, StringVar, OptionMenu, PhotoImage
from tkinter import ttk
from tkinter.ttk import *
from tkinter.filedialog import askdirectory
from typing import Protocol
import threading

logger = logging.getLogger()

class Presenter(Protocol):
    
    def handle_button_click(self, event=None) -> None:
        ...



class RootViewController(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('My App title')
        self.minsize(750, 500)
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.file_count_display: int = 0
        self.geometry("900x400")
    
    def init_ui(self, presenter: Presenter) -> None:
        self.top_frame = tk.Frame(self, padx=5, pady=5, highlightbackground="blue", highlightthickness=2)
        self.top_frame.pack(side=TOP, fill=X, expand=True, anchor=N)

        self.name_label = tk.Label(self.top_frame, text='Name: ', padx=1)
        self.name_label.pack(side=LEFT, padx=10, pady=10, anchor=NE)
        
        self.first_name = tk.Entry(self.top_frame)
        self.first_name.pack(side=LEFT, padx=10, pady=10, anchor=NE)
        self.first_name.bind("<Return>", presenter.handle_button_click)

        self.add_person_button = tk.Button( self.top_frame, text='click', pady=4, width=8)
        self.add_person_button.pack(side=LEFT, anchor=NE)
        self.add_person_button.bind("<ButtonRelease>", presenter.handle_button_click)

