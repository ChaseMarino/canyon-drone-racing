import os
import tkinter
from tkintermapview import TkinterMapView


def createMap(ws):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    database_path = os.path.join(script_directory, "offline_tiles_Rochester.db")
    map_widget = TkinterMapView(ws, width=ws.winfo_screenwidth(), height=ws.winfo_screenheight()*.5,
                                corner_radius=0, use_database_only=True, max_zoom=22, database_path=database_path)
    map_widget.set_address("Rochester")
    map_widget.grid(row=0, column=0, columnspan=2, rowspan=1, sticky="NSEW")
    # map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
    # map_option_menu = customtkinter.CTkOptionMenu(ws, values=["OpenStreetMap", "Google normal", "Google satellite"],
    #                                               command=change_map)

    return map_widget


def setPositions(mapWidget, positions, markers):
    for position in positions:
        mapWidget.set_position(position[0], position[1], marker=False)
    markers.append(positions[0])
    # print(markers)
    mapWidget.set_path(markers)


def change_map(mapWidget, new_map: str):
    if new_map == "OpenStreetMap":
        mapWidget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
    elif new_map == "Google normal":
        mapWidget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",
                                        max_zoom=22)
    elif new_map == "Google satellite":
        mapWidget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga",
                                        max_zoom=22)
