from controller import Robot
import math

robot = Robot()

timestep = int(robot.getBasicTimeStep())

left_motor = robot.getDevice("left wheel motor");
left_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)

right_motor = robot.getDevice("right wheel motor");
right_motor.setPosition(float('inf'))
right_motor.setVelocity(0.0)

imu= robot.getDevice("inertial unit")
imu.enable(timestep)

ds_front = robot.getDevice("ds_front")
ds_front.enable(timestep)
ds_left = robot.getDevice("ds_left")
ds_left.enable(timestep)
ds_right= robot.getDevice("ds_right")
ds_right.enable(timestep)

def move(left_speed,right_speed):
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)  

def turn_towards_angle(target_angle):
    if(target_angle != yaw_current):
        move(-1,1) 
    else:
        move(0,0)
        
def move_forward_till_wall_detection():
    if(ds_front_value>300):
        move(15,15)
    else:
        move(0,0)
            
while robot.step(timestep) != -1:

    angle=imu.getRollPitchYaw()
    
    ds_front_value= ds_front.getValue()
    
    yaw_current= round(math.degrees(angle[2]))+180
    
    print(yaw_current)
    
    move_forward_till_wall_detection()