import RPi.GPIO as GPIO
import time

class StepperControl:
    def __init__(self, control_pins, enable_pin):
        self.control_pins = control_pins
        self.enable_pin = enable_pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(self.enable_pin, GPIO.OUT)

        for i in range(0, len(control_pins)):
            GPIO.setup(control_pins[i], GPIO.OUT)

    def setStep(self, values):
        if len(values) != len(self.control_pins):
            return False

        for i in range(0, len(values)):
            GPIO.output(self.control_pins[i], values[i])

        return True

    def forward(self, steps, delay):
        for i in range(0, steps):
            self.setStep([1,0,1,0])
            time.sleep(delay)
            self.setStep([0,1,1,0])
            time.sleep(delay)
            self.setStep([0,1,0,1])
            time.sleep(delay)
            self.setStep([1,0,0,1])
            time.sleep(delay)

    def backward(self, steps, delay):
        for i in range(0, steps):
            self.setStep([1,0,0,1])
            time.sleep(delay)
            self.setStep([0,1,0,1])
            time.sleep(delay)
            self.setStep([0,1,1,0])
            time.sleep(delay)
            self.setStep([1,0,1,0])
            time.sleep(delay)

    def enable(self):
        GPIO.output(self.enable_pin, True)

    def disable(self):
        GPIO.output(self.enable_pin, False)