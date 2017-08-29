# Python Microbit library and apps

This repo contains a library to make it easier to write Python
Microbit applications, and some example applications.

## Microbit Library

This classs contains some useful reusable logic for Microbit
applications. Simply create a class that extends the Microbit class
and then you can use the provided build script to create a single
Python file that can be sent to your device using uFlash.

You'll need `uFlash` installed to send the file to your Microbit
device. I recommend you use a virtualenvironment.

```bash
virtualenv venv
./venv/bin/pip install uflash
```

You can then use the build script to create an executable Microbit
program from yuor class.

```bash
./venv/bin/python build.py your-program.py
```

**NOTE:** You should not import the microbit library, since uFlash
expects a the program to be single Python file. Just create a file
that contains only yuor class and run the build script on that. The
example applications should show how this works.

## Applications

### Die

This is a simple application that simulates a 6-sided die. Press
either button to roll the die. The result will be displayed on the
Microbit's screen.

### TechnoTimer

This is a simple timer application. Pressing A will start a 30 second
timer, B will start a 60 second timer. Running timers can be cancelled
with a button press.

This is perfect for (among other things) the board game
[TechnoBowl](https://boardgamegeek.com/boardgame/194923/techno-bowl-arcade-football-unplugged).

### Dodge

This is a simple game for the Microbit. Press A and B to dodge the
incoming obstacles.

### X-Wing Dice

This application simulates the eight-sided dice used in
[Fantasy Flight Games' X Wing Miniatures Game](https://www.fantasyflightgames.com/en/products/x-wing/).
Pressing the A button will simulate the roll of a red attack die, the
B button will the roll a green defence die.
