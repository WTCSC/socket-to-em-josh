import math
import logging


logging.basicConfig(                               #-----------------------\
    level=logging.DEBUG,                                                #   \
    format='%(asctime)s - %(levelname)s - %(message)s',                 #    |--------------------------->  Set up logging
    filename='app.log'                                                  #   /
)                                                  #-----------------------/

g = 9.8  #----------------------------------------------------------------------------------------------->  Gravitational acceleration in m/s^2

def calculate_distance(power, angle):  #----------------------------------------------------------------->  Function to calculate the throwing distance
    try:
        logging.debug(f"Calculating distance with power={power}, angle={angle}")  #---------------------->  Log calculation parameters
        angle_rad = math.radians(angle)  #--------------------------------------------------------------->  Convert angle to radians
        distance = (power ** 2) * math.sin(2 * angle_rad) / g   #---------------------------------------->  Calculate the distance using projectile motion formula
        distance = distance * 3.28084   #---------------------------------------------------------------->  Converts meters into feet
        logging.debug(f"Calculated distance: {distance} feet")  #---------------------------------------->  Log calculated distance
        return distance
    except Exception as Calculation_Error:
        logging.error(f"Error in calculate_distance: {Calculation_Error}")  #---------------------------->  Log error message
        return 0  #-------------------------------------------------------------------------------------->  Return 0 in case of error
