# Pico-Pi

MicroPython scripts for a Raspberry Pi Pico W wired to a few LEDs. Each file is a standalone
program you copy onto the board and run. They blink LEDs in patterns: a 4-bit binary counter,
an accelerating 5-LED flash loop, and a set of Morse code helper functions.

## Projects

### binary.py

Counts from 1 to 15 in binary on four LEDs, then flashes all four three times at a faster rate
and repeats forever. The `decimal_to_binary()` function takes the four bit values plus a `pause`
in seconds, drives the pins high for that long, then drives them all low for the same amount of
time. The counting order in the loop is written little-endian: `led1` is the low bit.

Pins used, all set as outputs:

| Variable | GPIO pin |
|---|---|
| `led1` | GP15 |
| `led2` | GP14 |
| `led3` | GP13 |
| `led4` | GP12 |

Wire each GPIO pin through a current-limiting resistor to an LED anode, with the LED cathode to a
ground pin. The resistor value is not specified in the code.

Run it by copying `binary.py` to the board and executing it. The loop never exits, so stop it with
a keyboard interrupt from the REPL or by resetting the board.

### ledshow.py

Flashes five LEDs together with a pause that shrinks on every iteration. It starts at `num = 5`,
multiplies `num` by `1.01 ** 2` a thousand times, and uses `1 / num` as the on/off delay, so the
flashing speeds up as the loop runs. The outer `while True` resets `num` back to 5 each pass, so
the effect repeats.

Pins used, all set as outputs:

| Variable | GPIO pin |
|---|---|
| `led0` | GP16 |
| `led1` | GP15 |
| `led2` | GP14 |
| `led3` | GP13 |
| `led4` | GP12 |

Same wiring as `binary.py`, with one more LED on GP16. Copy the file to the board and run it; the
loop does not terminate on its own.

### sos.py

Morse code helpers for a single red LED on GP15. It defines `dot()` and `line()` to blink the LED,
and `s()` and `o()` which call them three times each. The file sets `redLED.value(1)` at import
time, so the LED turns on as soon as the script runs.

This one has no main loop. Importing or running it defines the functions and turns the LED on, but
nothing sends an SOS until you call `s()`, `o()`, `s()` yourself, for example from the REPL after
`import sos`.

Two things in the code are worth knowing before you use it. `DOT_PAUSE` is 0.5 and `LINE_PAUSE`
is 0.2, so a dash is currently shorter than a dot, which is backwards from standard Morse timing.
`WORD_PAUSE` and `LETTER_PAUSE` are defined but never used.

Pin used:

| Variable | GPIO pin |
|---|---|
| `redLED` | GP15 |

## Requirements

- Raspberry Pi Pico W
- MicroPython firmware flashed onto the board
- LEDs and current-limiting resistors, plus a breadboard and jumper wires
- A micro USB cable
- An editor or tool that can copy files to the board and open the REPL, such as Thonny or `mpremote`

The scripts import only `machine` and `time`, both part of the MicroPython standard build. There
are no third-party dependencies and nothing to install with pip.

## Setup

1. Flash MicroPython onto the Pico W: hold BOOTSEL, plug in the USB cable, and drag the MicroPython
   `.uf2` file onto the drive that appears. The board reboots into MicroPython.
2. Wire the LEDs to the GPIO pins listed for the script you want to run, each through a resistor,
   with the cathodes tied to a ground pin.
3. Copy the script to the board and run it.

With Thonny, open the file, set the interpreter to MicroPython (Raspberry Pi Pico), and press Run.

With `mpremote`:

```
mpremote cp binary.py :main.py
mpremote reset
```

Copying a file to `main.py` makes it run automatically on every power-up. To run a script once
without making it permanent, use `mpremote run binary.py` instead.

## License

No LICENSE file is present in this repository.
