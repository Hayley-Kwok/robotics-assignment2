from controller import Robot,Camera,GPS

TIME_STEP = 64
robot = Robot()


#Distance Sensors (initialize)
ds = []
dsNames = ['ds_right', 'ds_left','ds_front','ds_frontleft','ds_frontright']

for i in range(5):
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
camera1 = robot.getCamera('camera1')
#camera1.enable(TIME_STEP)
camera0.recognitionEnable(TIME_STEP)
camera1.recognitionEnable(TIME_STEP)


#gps= robot.getGPS('gps')
#gps.enable(TIME_STEP)
#def colorRecognise(image,w,x,y)

c=0

# feedback loop: step simulation until receiving an exit event
while robot.step(TIME_STEP) != -1:
    if c==0:
      
        color1=(camera1.getRecognitionObjects())[0].get_colors()
        camera1.recognitionDisable()
    c+=1
    
    #print('right', ds[0].getValue())
    #print('left', ds[1].getValue())
    #print('front', ds[2].getValue())
    #print('frontleft', ds[3].getValue())
    #print('frontright', ds[4].getValue())

    

    # avoid obstacle from left and front        
    if ds[0].getValue() < 1100 or ds[2].getValue() < 1500 or ds[3].getValue()<1500 or  ds[4].getValue()<1500: 
        leftSpeed = -10
        rightSpeed = 2.2
        
    # without obstacle
    else:
        leftSpeed = 10
        rightSpeed = 6
    
    # for u-turn
    if ds[0].getValue()>3500 and ds[2].getValue()>2000:
        leftSpeed = 10
        rightSpeed = 1
        #print("56000000000000000000000000000000000") 
        
    # escape from "narrowing" paths
    if ds[0].getValue()<1500 and ds[1].getValue()<1500 and ds[3].getValue()<1500 and  ds[4].getValue()<1500:   
        leftSpeed = -3
        rightSpeed = 8
        #print("narrowwwwwwwwwwwwwwwwwwwwwwwwwwww")  
                         
                    
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)
    
    
    if camera0.getRecognitionNumberOfObjects()!=0:
        color0=(camera0.getRecognitionObjects())[0].get_colors()
        #print(color0)
        #print(color1,"ffffffffffffffffffffff")\
        if color0 == color1 and ds[2].getValue() < 1500:
                wheels[0].setVelocity(0)
                wheels[1].setVelocity(0)
                wheels[2].setVelocity(0)
                wheels[3].setVelocity(0)
                break 
          
    
    
    
    



