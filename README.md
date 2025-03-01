Python Paper Airplane Throwing Distance Game:

This program simulates a throwing distance game between a client and a server. The client sends a throwing angle and power to the server, which calculates a distance. The client also calculates its own distance, and the winner is based on who threw the furthest.

Files:

client.py – Handles the client-side logic. The client sends the throwing angle and power to the server, receives the server's distance, and determines the winner.

server.py – Handles the server-side logic. The server waits for the client's connection, calculates its distance, and sends it back to the client.

d_calc.py – Contains the calculate_distance function to calculate the throwing distance based on the power and angle.

Setup:
1. Install Python
Ensure Python 3.x is installed on your machine. Download it from python.org.

2. Running the Program
    Start the Server:

    Open a terminal and navigate to the program directory.

    Run the server:

    In Bash, enter

        python server.py

    The server will ask for an IP address and port to listen on.

    Start the Client:

    Open another terminal and navigate to the same directory.

    Run the client:

    In Bash, enter
    
        python client.py

    The client will ask for the server's IP address, port, throwing angle (in degrees), and throwing power (as a percentage).

How It Works:

The client and server both calculate their throwing distances based on the angle and power.
The winner is determined by comparing the two distances: the furthest throw wins.
Results are printed on both the client and server terminals, and actions are logged in app.log.
Logging
All important events, such as connections, data received, and results, are logged to a file called app.log.

Notes:

Distances are calculated in meters but displayed in feet (conversion factor: 1 meter = 3.28084 feet).
If any errors occur, they are logged in the app.log file.