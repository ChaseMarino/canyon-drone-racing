from tkinter import *
from tkinter import ttk
from data import *
import components.map as map

metricsList = []
# metricNames = ["Latitude (m)", "Longitude (m)", "Altitude (m)", "Yaw (θ)", "Pitch (θ)", "Tilt (θ)",
#                "Velocity_North (m/s)", "Velocity_East (m/s)", "Velocity_Upwards (m/s)"]
metricNames = ["Name", "Location(lat, long, alt)", "Velocity(x, y, z)", "Attitude(pitch, yaw, roll)", "Mission Status",  "Health Status"]
root = None
numDrones = 1
locationHistory = []


class Metric:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def updateValue(self, value):
        self.value = value


def createMetrics():
    for index in range(numDrones):
        metrics = []
        for name in metricNames:
            # if name == "Latitude":
            #     metrics.append(Metric(name, [Metric("Lat", 0), Metric("Long", 0), Metric("Alt", 0)]))
            # if name == "Name":
            #     metrics.append(Metric(name, "Drone #" + str(index+1)))
            # else:
            metrics.append(Metric(name, ''))
        metricsList.append(metrics)
    return metricsList


def setHeaders(statusTable, ws):
    statusTable.column("#0", width=0, stretch=NO)
    statusTable.heading("#0", text="", anchor=CENTER)
    for name in metricNames:
        statusTable.column(name, anchor=CENTER, minwidth=100, width=int(ws.winfo_screenwidth()/(1.5*len(metricNames))))
        statusTable.heading(name, text=name, anchor=CENTER)


def createTable(ws):
    tableFrame1 = Frame(ws)
    statusTable = ttk.Treeview(tableFrame1, style=setStyling())
    tableFrame1.grid(row=1, column=0, columnspan=1, rowspan=1, sticky="NSEW")
    statusTable['columns'] = [name for name in metricNames]
    setHeaders(statusTable, ws)
    createMetrics()
    for index in range(numDrones):
        statusTable.insert(parent='', index='end', text='',
                           values=[metric.value for metric in metricsList[index]])
    setStyling()
    return statusTable


def updateMetrics(statusTable, mapWidget):
    data = getVehicleData()
    if data != "initial":
        for droneIndex in range(len(metricsList)):
            updatedValues = getStatusValues(data, droneIndex)
            # print(updatedValues)
            for metricIndex in range(len(metricsList[droneIndex])):
                if metricIndex < len(updatedValues[droneIndex]):
                    metricsList[droneIndex][metricIndex].updateValue(updatedValues[droneIndex][metricIndex])
            statusTable.item(statusTable.get_children()[droneIndex], values=[metric.value for metric in metricsList[droneIndex]])
            # print(locationHistory)
            map.setPositions(mapWidget, [[data.location.lat, data.location.long]], locationHistory)
    return metricsList


def getStatusValues(data, numDrone):
    locationStr = str(data.location.lat) + '\n' + str(data.location.long) + '\n' + str(data.location.alt)
    velocityXYZ = str(data.velocityXYZ.x) + '\n' + str(data.velocityXYZ.y) + '\n' + str(data.velocityXYZ.z)
    attitude = str(data.attitude.pitch) + '\n' + str(data.attitude.yaw) + '\n' + str(data.attitude.roll)
    status = data.status
    name = "Drone #" + str(numDrone+1)
    return [[name, locationStr, velocityXYZ, attitude, status, " N/A"]]



def setStyling():
    return ttk.Style().configure('.',
                          # every class of object TODO this is old there is other style widget to be researched and used.
                          relief='flat',  # flat ridge for separator
                          borderwidth=0,  # zero width for the border
                          font=('Helvetica', 16),
                          background="#282828"
                          )


def updateTable(statusTable, mapWidget):
    # getVehicleData().location.lat
    # while(getVehicleData() == "initial"):
    #     doNothing = "NOthing"
        #Wait

    for i in range(0, 25000):
        statusTable.after(333 * (i + 1), updateMetrics, statusTable, mapWidget) # no idea what the array here is for it was for incrementing values but idk y
        # [[num + (i * 10) + 1000 for num in range(0, 10)]]]
