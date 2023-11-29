"""A program for converting decimal to binary and vice versa."""
from machine import Pin
from time import sleep


led0 = Pin(16, Pin.OUT)
led1 = Pin(15, Pin.OUT)
led2 = Pin(14, Pin.OUT)
led3 = Pin(13, Pin.OUT)
led4 = Pin(12, Pin.OUT)


def decimal_to_binary(l0=0, l1=0, l2=0, l3=0, l4=0, pause=0.5):
    """Converts decimal to binary."""
    led0.value(l0)
    led1.value(l1)
    led2.value(l2)
    led3.value(l3)
    led4.value(l4)

    sleep(pause)

    led0.value(0)
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    sleep(pause)
    return None


decimal_to_binary(l0=1, l1=1, l2=1, l3=1, l4=1)


while True:
    num = 5
    for i in range(0, 1000):
        num = num * (1 + 0.01) ** 2
        inverse = 1 / num
        decimal_to_binary(l0=1, l1=1, l2=1, l3=1, l4=1, pause=inverse)
