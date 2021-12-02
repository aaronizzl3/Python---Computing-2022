# Imports
import tkinter as tk
import socket
import sys
from tkinter import ttk
from threading import *


# Functions
def port_scan():
    remoteServer = "127.0.0.1"
    remoteServerIP = socket.gethostbyname(remoteServer)

    print("Please wait, scanning remote host", remoteServerIP)
    try:
        for port in range(1,1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("Port {}: 	 Open".format(port))
            sock.close()

    # If this doesn't work CTRL + F2 will stop PyCharm (or the little stop button in the bottom left)
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    # GAI = Get Address Info (getaddrinfo()) and gives errors specific to the remote host
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    # General socket errors
    except socket.error:
        print("Couldn't connect to server")
        sys.exit()


def say_hello():
    print("Hello World!")


# Setup Threads
t1 = Thread(target=port_scan)

# GUI - Main Window
root = tk.Tk()
root.geometry("200x100")
root.title("Port Scanner")

# GUI Widgets
btn_portScan = ttk.Button(root, text="Port Scan", command=lambda: t1.start())
btn_SayHello = ttk.Button(root, text="Say Hello!", command=say_hello)

btn_portScan.pack(side="left", padx=(10,10))
btn_SayHello.pack(side="left", padx=(10,10))

# Run
root.mainloop()

