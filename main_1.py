import time
from machine import Pin, PWM
import sys
import time

# led = PWM(2)
MOTOR_ON = 32512
MOTOR_OFF = 0
power_pin = Pin(25, Pin.OUT)
pwm_1 = PWM(2, duty_u16=MOTOR_OFF)
invert_pwm_1 = Pin(6, Pin.OUT)
pwm_2 = PWM(3, duty_u16=MOTOR_OFF)
invert_pwm_2 = Pin(7, Pin.OUT)
pwm_3 = PWM(4, duty_u16=MOTOR_OFF)
invert_pwm_3 = Pin(8, Pin.OUT)
pwm_4 = PWM(5, duty_u16=MOTOR_OFF)
invert_pwm_4 = Pin(9, Pin.OUT)
power_pin.value(1)

# pwm_1.duty_u16(32512)

def set_frequency(motor:int, frequency:int):
    if motor == 1:
        pwm_1.freq(frequency)
    elif motor == 2:
        pwm_2.freq(frequency)
    elif motor == 3:
        pwm_3.freq(frequency)
    elif motor == 4:
        pwm_4.freq(frequency)

def motor_power(motor:int, state:bool):
    if motor == 1:
        if state:
            pwm_1.duty_u16(MOTOR_ON)
        else:
            pwm_1.duty_u16(MOTOR_OFF)
    elif motor == 2:
        if state:
            pwm_2.duty_u16(MOTOR_ON)
        else:
            pwm_2.duty_u16(MOTOR_OFF)
    elif motor == 3:
        if state:
            pwm_3.duty_u16(MOTOR_ON)
        else:
            pwm_3.duty_u16(MOTOR_OFF)
    elif motor == 4:
        if state:
            pwm_4.duty_u16(MOTOR_ON)
        else:
            pwm_4.duty_u16(MOTOR_OFF)
    print(pwm_1.duty_u16())

def invert_motor(motor:int, invert:bool):
    if motor == 1:
        invert_pwm_1.value(invert)
    elif motor == 2:
        invert_pwm_2.value(invert)
    elif motor == 3:
        invert_pwm_3.value(invert)
    elif motor == 4:
        invert_pwm_4.value(invert)

while True:
    # read a command from the host
    input = sys.stdin.readline(15).split(';')
    try:
        if input[1] == 'start':
            motor = int(input[0])
            motor_power(motor, True)
        elif input[1] == 'stop':
            motor = int(input[0])
            motor_power(motor, False)
        elif input[1] == 'invert':
            motor = int(input[0])
            invert = bool(int(input[2]))
            invert_motor(motor, invert)
        else:
            motor = int(input[0])
            frequency = int(input[1])
            set_frequency(motor, frequency)
    except:
        pass
    time.sleep(0.5)

