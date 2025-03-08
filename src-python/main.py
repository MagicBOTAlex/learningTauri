# This just contains helper functions to interface with the ETVR backend. I'm not touching rust lol.

import cv2
import os
import win32api
import win32con
import win32com.client

_tauri_plugin_functions = ["greet_python", "get_list_of_system_cameras"]
def greet_python(rust_var):
    return str(rust_var) + " from python"


def get_list_of_system_cameras():
    camera_list = []
    
    # Get the device manager object
    wmi = win32com.client.Dispatch("WbemScripting.SWbemLocator")
    services = wmi.ConnectServer(".", "root\\CIMV2")
    devices = services.ExecQuery("Select * from Win32_PnPEntity where DeviceID like 'USB%'")

    for device in devices:
        if "video" in device.Description.lower():
            # Extract camera name
            camera_name = device.Description
            # Check if the camera is available
            for i in range(10):
                cap = cv2.VideoCapture(i)
                if cap.isOpened():
                    camera_list.append((i, camera_name))
                    cap.release()
                    break
    return camera_list
