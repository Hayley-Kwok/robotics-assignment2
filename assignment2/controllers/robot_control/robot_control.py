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
# feedback loop: step simulation until receiving an exit event
while robot.step(TIME_STEP) != -1:
    leftSpeed = 9.9
    rightSpeed = 9.9
    
    if leftCounter > 0:
        leftCounter -=1
        leftSpeed = 7.0
        rightSpeed = -5.0
    elif rightCounter >0:
        rightCounter-=1
        leftSpeed = -5.0
        rightSpeed = 7.0
    else:  # read sensors
        if ds[2].getValue() < 1800.0:
            gpsData.append(gps.getValues())
            if ds[0].getValue() > ds[1].getValue():    
                leftCounter = 12
                rightCounter = 0
            else: 
                leftCounter = 0
                rightCounter = 12
                     
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)
    
