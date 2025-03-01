import socket
import math
from d_calc import calculate_distance  #--------------------------------------------------------------------------------------->  Imports the distance calculator from d_calc.py
import logging

logging.basicConfig(                        #--------------------\
    level=logging.DEBUG,                                        # \
    format='%(asctime)s - %(levelname)s - %(message)s',         #  |----------------------------------------------------------->  Sets up logging
    filename='app.log'                                          # /
)                                           #--------------------/

def start_client():                                             #-----------------\
    try:                                                                      #    \
        host = input("Enter the server's IP address: ")                       #     \
        port = int(input("Enter the server's port: "))                        #      |----------------------------------------->  Client setup
                                                                              #      |                                            User enters the IP address and port chosen by the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #     /
        client_socket.connect((host, port))                                   #    /
        logging.info(f"Connected to server at {host}:{port}")   #-----------------/

        angle = float(input("Who can throw a paper airplane farther?\nEnter the throwing angle (in degrees): "))  #----/------->  Player enters their throwing power and throwing angle
        power = float(input("Enter the throwing power (as a percentage): ")) / 100  #---------------------------------/           Throwing power is converted into a fraction

        
        angle = math.floor(angle)  #------------------------------------------------------------------------------------------->  Floors the angle
        power = math.floor(power * 100) / 100  #------------------------------------------------------------------------------->  Reconverts power to a percentage, and is floored

        logging.info(f"Client entered an angle of: {angle}° and a power of: {power * 100}%")  #-------------------------------->  Logs the player input
        
        
        client_socket.send(f"{angle},{power}".encode())  #--------------------------------------------------------------------->  Sends the data to the server

        
        server_distance = float(client_socket.recv(1024).decode()) #----------------------------------------------------------->  Receives the server's calculated distance
        logging.info(f"Server's distance: {server_distance:.2f} feet")  #------------------------------------------------------>  Logs the server's distance

        
        client_distance = calculate_distance(power, angle) #------------------------------------------------------------------->  Client calculates their own distance
        logging.info(f"Client's distance: {client_distance:.2f} feet")  #------------------------------------------------------>  Logs the client's distance

        if client_distance > server_distance: #--------------\
            print("Client wins!")                    #        \
            logging.info("Client wins!")             #         \
        elif client_distance < server_distance:      #          |
            print("Server wins!")                    #          |------------------------------------------------------------->  Determines a winner, and prints it
            logging.info("Server wins!")             #          |                                                                Logs the result
        else:                                        #         / 
            print("It's a tie!")                     #        /
            logging.info("It's a tie!")       #--------------/

    except Exception as Start_Error:
        logging.error(f"Error in start_client: {Start_Error}")  #------------------------------------------------------------->  Log error message
    finally:
        client_socket.close() #----------------------------------------------------------------------------------------------->  Closes the connection
        logging.info("Client socket closed.")  #------------------------------------------------------------------------------>  Logs the client socket closure

if __name__ == "__main__": #-------------------------------------------------------------------------------------------------->  Runs the client
    start_client()
