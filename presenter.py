from __future__ import annotations
from typing import Protocol, Dict
from model import Model


class View(Protocol):
    
    def init_ui(self) -> None:
        ...



class Presenter:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
    

    def handle_button_click(self, event=None) -> None:
        print(f'Button clicked')

    def run(self) -> None:
        self.view.init_ui(self)
        #self.update_db_table()
        self.view.mainloop()