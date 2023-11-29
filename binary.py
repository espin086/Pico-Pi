"""A program for converting decimal to binary and vice versa."""
from machine import Pin
from time import sleep

led1 = Pin(15, Pin.OUT)
led2 = Pin(14, Pin.OUT)
led3 = Pin(13, Pin.OUT)
led4 = Pin(12, Pin.OUT)


def decimal_to_binary(l1=0, l2=0, l3=0, l4=0, pause=0.5):
    """Converts decimal to binary."""
    led1.value(l1)
    led2.value(l2)
    led3.value(l3)
    led4.value(l4)

    sleep(pause)

    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    sleep(pause)
    return None


while True:
    decimal_to_binary(l1=1, l2=0, l3=0, l4=0)
    decimal_to_binary(l1=0, l2=1, l3=0, l4=0)
    decimal_to_binary(l1=1, l2=1, l3=0, l4=0)
    decimal_to_binary(l1=0, l2=0, l3=1, l4=0)
    decimal_to_binary(l1=1, l2=0, l3=1, l4=0)
    decimal_to_binary(l1=0, l2=1, l3=1, l4=0)
    decimal_to_binary(l1=1, l2=1, l3=1, l4=0)
    decimal_to_binary(l1=0, l2=0, l3=0, l4=1)
    decimal_to_binary(l1=1, l2=0, l3=0, l4=1)
    decimal_to_binary(l1=0, l2=1, l3=0, l4=1)
    decimal_to_binary(l1=1, l2=1, l3=0, l4=1)
    decimal_to_binary(l1=0, l2=0, l3=1, l4=1)
    decimal_to_binary(l1=1, l2=0, l3=1, l4=1)
    decimal_to_binary(l1=0, l2=1, l3=1, l4=1)
    decimal_to_binary(l1=1, l2=1, l3=1, l4=1)
    for _ in range(3):
        decimal_to_binary(l1=1, l2=1, l3=1, l4=1, pause=0.3)
