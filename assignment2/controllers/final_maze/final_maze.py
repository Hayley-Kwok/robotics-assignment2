import math
from controller import Robot,Camera,GPS

TIME_STEP = 64
robot = Robot()

#gps data
gpsData=[]

#Distance Sensors (initialize)
ds = []
dsNames = ['ds_right', 'ds_left','ds_front']

for i in range(3):
    ds.append(robot.getDistanceSensor(dsNames[i]))
    ds[i].enable(TIME_STEP)
    
#Wheels Initialize    
wheels = []
wheelsNames = ['tlwheel', 'trwheel', 'blwheel', 'brwheel']
for i in range(4):
    wheels.append(robot.getMotor(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)

#Camera Initialize
camera0 = robot.getCamera('camera0')
camera0.enable(TIME_STEP)


#gps= robot.getGPS('gps')
#gps.enable(TIME_STEP)

leftCounter = 0
rightCounter = 0
backCounter = 0
# feedback loop: step simulation until receiving an exit event
while robot.step(TIME_STEP) != -1:
 
    #print('right', ds[0].getValue())
    #print('left', ds[1].getValue())
    # print('front', ds[2].getValue())

    
    
    if ds[0].getValue()<1300 and ds[1].getValue()<1300:   
        leftSpeed =2
        rightSpeed=0
        print("f")          
    if ds[2].getValue()<1100:
        leftSpeed = 2
        rightSpeed = -10
    elif ds[1].getValue()<900:
        leftSpeed = 2.2
        rightSpeed = -3
    else:
        leftSpeed = 1
        rightSpeed = 10
    
    
    
    
    
                                 
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)
    

