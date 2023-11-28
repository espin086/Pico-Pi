from machine import Pin
from time import sleep


DOT_PAUSE = 0.5
LINE_PAUSE = 0.2
WORD_PAUSE = 1.5
LETTER_PAUSE = 1

redLED = Pin(15, Pin.OUT)
redLED.value(1)


def dot(pause=DOT_PAUSE):
    """Turns on the red LED for a short period of time, then turns it off."""
    redLED.value(1)
    sleep(pause)
    redLED.value(0)
    sleep(pause)
    return None


def line(pause=LINE_PAUSE):
    """Turns on the red LED for a long period of time, then turns it off."""
    redLED.value(1)
    sleep(pause)
    redLED.value(0)
    sleep(pause)
    return None


def s():
    """Sends the letter 'S' in Morse code."""
    dot()
    dot()
    dot()
    return None


def o():
    """Sends the letter 'O' in Morse code."""
    line()
    line()
    line()
    return None
