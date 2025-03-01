import socket
import math
from d_calc import calculate_distance  #--------------------------------------------------------------------------------------> Import the game logic from d_calc.py


def start_client():                                 #----------------------\  
    host = input("Enter the server's IP address: ")                       # \
    port = int(input("Enter the server's port: "))                        #  |------------------------------------------------>  Client setup
                                                                          #  |
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # /
    client_socket.connect((host, port))             #----------------------/

    
    angle = float(input("Who can throw a paper airplane farther?\nEnter the throwing angle (in degrees): "))  #----/---------->  Player enters their throwing power and throwing angle
    power = float(input("Enter the throwing power (as a percentage): ")) / 100  #---------------------------------/              Throwing power is converted into a fraction

    
    angle = math.floor(angle)  #---------------------------------------------------------------------------------------------->  Floor the angle
    power = math.floor(power * 100) / 100  #---------------------------------------------------------------------------------->  Reconverts power to a percentage, and is floored

    print(f"Client entered an angle of: {angle}° and a power of: {power * 100}%") #------------------------------------------->  Prints the inputted angle and throwing power
    
    
    client_socket.send(f"{angle},{power}".encode())  #------------------------------------------------------------------------>  Sends the data to the server

    
    server_distance = float(client_socket.recv(1024).decode()) #------------------/------------------------------------------->  Multiplies the server's distance by 3.28084 to convert meters into feet, and prints it
    print(f"Server's distance: {server_distance:.2f} feet")  #-------------------/

    
    client_distance = calculate_distance(power, angle) #---------------/------------------------------------------------------>  Multiplies the client's distance by 3.28084 to convert meters into feet, and prints it
    print(f"Client's distance: {client_distance:.2f} feet") #-------------------/

    if client_distance > server_distance: #--------------\
        print("Client wins!")                    #        \
    elif client_distance < server_distance:      #         |------------------------------------------------------------------>  Determines a winner, and prints it
        print("Server wins!")                    #         |
    else:                                        #        /
        print("It's a tie!")              #--------------/

    
    client_socket.close() #--------------------------------------------------------------------------------------------------->  Closes the connection


if __name__ == "__main__": #-------------------------------------------------------------------------------------------------->  Runs the client
    start_client()
