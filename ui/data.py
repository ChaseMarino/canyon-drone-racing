global vehicleStatusData #You can make this an object of the protobuf and just display the properties of the proto
vehicleStatusData = "initial"
"""
point of this python file is to track the current vehicle message data recieved from the drone.
"""

def setTestData(val):
    global vehicleStatusData
    vehicleStatusData = val
   
def getVehicleData():
    return vehicleStatusData