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


gps= robot.getGPS('gps')
gps.enable(TIME_STEP)

leftCounter = 0
rightCounter = 0
backCounter = 0
# feedback loop: step simulation until receiving an exit event
while robot.step(TIME_STEP) != -1:
    print('right', ds[0].getValue())
    print('left', ds[1].getValue())
    print('front', ds[2].getValue())
    leftSpeed = 7
    rightSpeed = 7
    
    if backCounter > 0:
        backCounter -=1
        leftSpped = -9.9
        rightSpeed = -9.9
        
    elif leftCounter > 0:
        leftCounter -=1
        leftSpeed = 5.3
        rightSpeed = -3.8
        
    elif rightCounter >0:
        rightCounter-=1
        leftSpeed = -3.8
        rightSpeed = 5.3
        
    else:  # read sensors
        
        if ds[2].getValue() < 2000.0:
            gpsData.append(gps.getValues())
            if ds[0].getValue() > ds[1].getValue():    
                leftCounter = 8
                rightCounter = 0
                backCounter = 2
                
            else: 
                leftCounter = 0
                rightCounter = 8
                backCounter = 2
                
        elif ds[0].getValue() < 1400.0:
            leftCounter = 0
            rightCounter = 1
            
        elif ds[1].getValue() < 1400.0:
            leftCounter = 1
            rightCounter = 0
     
        
   
                                 
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)
    

