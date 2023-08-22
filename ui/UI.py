from tkinter import *
from tkinter import ttk

import components.button as button
import components.map as map
import components.status as status

ws = Tk()
def init_ui():
    
    ws.title('Drone Ui')

    screen_width = ws.winfo_screenwidth()
    screen_height = ws.winfo_screenheight()
    ws.geometry(f'{screen_width}x{screen_height}')
    ws['bg'] = '#282828'

    ws.columnconfigure(0, weight=3)
    ws.columnconfigure(1, weight=1)
    ws.rowconfigure(0, weight=1)
    ws.rowconfigure(1, weight=1)

    buttonTable = button.createButtonTable(ws)
    button.createButtons(buttonTable, ws)

    # positions = [[43.08491262, -77.679589], [43.08391262, -77.679589], [43.08281262, -77.679589]] #
    mapWidget = map.createMap(ws)
    # markers = []
    # for index, position in enumerate(positions):
    #     mapWidget.after(3333 * (index + 1), map.setPositions, mapWidget, [positions[index]], markers)

    statusTable = status.createTable(ws)
    status.updateTable(statusTable, mapWidget)

    statusTable.pack()
    buttonTable.pack()


def color_scheme(self, mode):
    if mode == 'dark':
        self.bg, self.fg, self.ac1, self.ac2 = ('#282828', 'white', '#404040y', '#B3B3B3')
    if mode == 'light':
        self.bg, self.fg, self.ac1, self.ac2 = ('#FBF8F1', 'black', '#F7ECDE', '#E9DAC1')

def run_ui():
    ws.mainloop()

