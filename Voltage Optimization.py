from machine import Pin, PWM, ADC
import time

# Hardware

SERVO_PIN = 15
VOLTAGE_PIN = 26

servo = PWM(Pin(SERVO_PIN))
servo.freq(50)

adc = ADC(VOLTAGE_PIN)

# Settings

MIN_ANGLE = 0
MAX_ANGLE = 40

START_ANGLE = 0
STEP = 5

SETTLE_TIME = 1.0

SAMPLES = 10
SAMPLE_DELAY = 0.05

# Voltage divider
VOLTAGE_SCALE = 1.0


# SERVO CONTROL

def set_angle(angle):

    angle = max(MIN_ANGLE, min(MAX_ANGLE, angle))

    min_duty = 1000
    max_duty = 9000

    duty = min_duty + (angle / 180) * (max_duty - min_duty)

    servo.duty_u16(int(duty))


# Reads the voltage from the ADC
# Converts the reading from the raw reading to the proportional voltage
# Averages all the samples read to get a more accurate overall reading

def read_voltage():

    total = 0

    for i in range(SAMPLES):

        raw = adc.read_u16()

        voltage = (raw / 65535) * 3.3

        total += voltage

        time.sleep(SAMPLE_DELAY)

    voltage = total / SAMPLES

    return voltage * VOLTAGE_SCALE


# Initialization

angle = START_ANGLE

set_angle(angle)
time.sleep(SETTLE_TIME)

current_voltage = read_voltage()

print("========================")
print("  TURBINE OPTIMIZER")
print("========================")
print("Starting angle:", angle)
print("Starting voltage:", round(current_voltage, 3), "V")

# Optimization function

direction = 1

while True:

    # Try moving in the current direction
    test_angle = angle + (STEP * direction)

    # Don't go outside our allowed range
    if test_angle > MAX_ANGLE or test_angle < MIN_ANGLE:

        direction *= -1
        continue

    print()
    print("Testing:", test_angle, "degrees")

    set_angle(test_angle)

    time.sleep(SETTLE_TIME)

    test_voltage = read_voltage()

    print("Voltage:", round(test_voltage, 3), "V")


    # If the voltage improved set the angle and voltage to current best data, and allow continuation in direction

    if test_voltage > current_voltage:
        
        angle = test_angle
        current_voltage = test_voltage

        print("IMPROVED")
        print("Best angle:", angle)
        print("Best voltage:", round(current_voltage, 3), "V")

    # Reverse direction if the voltage is getting worse in this direction

    else:
        print("WORSE — reversing direction")

        set_angle(angle)

        time.sleep(SETTLE_TIME)

        # Reverse search direction
        direction *= -1