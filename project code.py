# Type help("robolink") or help("robodk") for more information
# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/index.html
# Note: It is not required to keep a copy of this file, your python script is saved with the station

from robolink import *
from robodk import *

path = getOpenFile(r"Desktop") # open a window on at desktop to pick the csv file
data = LoadList(path) #Loading the (x,y,z) list
RDK = Robolink() # referring to the robot 
robot = RDK.Item('', ITEM_TYPE_ROBOT) #apply the program on the picked robot.
target = RDK.Item('Target 1') #declearing target 1 point as target
position = target.Pose() #the robot move to the target point
program_name = getFileName(path)#open the file that we have picked its path
program = RDK.AddProgram(program_name, robot)# Add a new program to the robot
RDK.Render(False) # Turn off rendering (faster)

 # Iterate through all the points
    for i in range(len(data)):
        pi = pose_ref
        pi.setPos(data[i])

        # Update speed if there is a 4th column
        if len(data[i]) >= 3:
            speed = data[i][3]
            # Update the program if the speed is different than the previously set speed
            if type(speed) != str and speed != current_speed:
                program.setSpeed(speed)
                current_speed = speed

        target = RDK.AddTarget('T%i' % i, frame)
        target.setPose(pi)
        pi = target

