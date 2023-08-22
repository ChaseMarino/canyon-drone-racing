from tkinter import *
from tkinter import ttk


def createButtonTable(ws):
    tableFrame2 = Frame(ws)
    tableFrame2.grid(row=1, column=1, columnspan=1, rowspan=1, sticky="NSEW")
    buttonTable = ttk.Treeview(tableFrame2)
    return buttonTable


def createButtons(buttonTable, ws):
    s = ttk.Style()
    s.configure('TButton', font=('Helvetica', 22), padding=20)
    gotoButton = ttk.Button(buttonTable, text="Goto", command=ws.destroy)
    loiterButton = ttk.Button(buttonTable, text="Loiter")
    rtbButton = ttk.Button(buttonTable, text="RTB")
    gotoButton.pack(side="top")
    loiterButton.pack(side="top")
    rtbButton.pack(side="top")


def change_map(self, new_map: str):
    if new_map == "OpenStreetMap":
        self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
    elif new_map == "Google normal":
        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",
                                      max_zoom=22)
    elif new_map == "Google satellite":
        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga",
                                        max_zoom=22)
