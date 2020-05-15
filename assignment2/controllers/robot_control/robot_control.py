from controller import Robot,Camera,GPS

TIME_STEP = 64

robot = Robot()

#gps data
gpsData=[]

#Distance Sensors (initialize)
ds = []
dsNames = ['ds_right', 'ds_left']

for i in range(2):
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

avoidObstacleCounter = 0

# feedback loop: step simulation until receiving an exit event
while robot.step(TIME_STEP) != -1:
    leftSpeed = 1.0
    rightSpeed = 1.0
    
    if avoidObstacleCounter > 0:
        avoidObstacleCounter -= 1
        leftSpeed = 1.0
        rightSpeed = -0.8
    else:  # read sensors
        for i in range(2):
            if ds[i].getValue() < 950.0:
                avoidObstacleCounter = 30
                gpsData.append(gps.getValues())
                print(gpsData)     
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)
    
