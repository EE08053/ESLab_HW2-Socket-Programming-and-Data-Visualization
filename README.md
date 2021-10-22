# ESLab_HW2-Socket-Programming-and-Data-Visualization

Execute "main.cpp", which is modified by mbed-os-example-sockets, on STM32 as client, and "socket.py" on laptop as server.

STM32 would send the 3d accelerator data to the laptop through wifi, and the data would be visualized by using matplotlib.pyplot.


### Step 1
Download mbed-os-example-sockets program (https://github.com/ARMmbed/mbed-os-example-sockets). 

### Step 2
Replace "main.cpp" and add BSP library folder in the program.

### Step 3
Open "mbed_app.json" in the program, fill in "nsapi.default-wifi-ssid" and "nsapi.default-wifi-password", according to the wifi that the server connects.

### Step 4
Open "main.cp"p and fill in "const char* IP" with your IP address.

### Step 5 
Run "socket.py" first and then "main.cpp", "socket.py" will collect the data and plot a line chart.
