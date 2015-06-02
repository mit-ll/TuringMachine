# A Turing Machine by MIT Lincoln Laboratory and the Community Charter School of Cambridge

During the spring semester in 2015, a team of MIT Lincoln Laboratory (http://www.ll.mit.edu/) staff volunteered there time to build a Turing machine with two high school seniors from the Community Charter School of Cambridge (http://www.ccscambridge.org/). This project helped the two seniors satisfy their internship requirement. The Turing machine was conceptualized by Alan Turing in 1936, but has been implemented in a more modern form.  The design uses 35mm film as memory, on which bits are physically written, read, and erased with a marker, camera, and mechanical eraser respectively.  These mechanisms are used to control the evolution of a state machine; fulfilling Turing's requirements for arbitrary computation.  The machine is controlled by embedded micro controllers, numerous motors and sensors, and code that was developed with the students.  The entire design for the machine, as well as the manufacturing and assembly, was created throughout the internship. The technical team from Lincoln Laboratory consisted of Chad Spensky, Benjamin Nahill, Timothy Greer, Matthew Harger, Stuart Baker, and Jack Lepird.  

## Contents
This repository contains all of the models, code, and bill of materials used to create our turing machine.

## Resources
  - [A Turing Machine](http://aturingmachine.com/)
  - [Turing Machine Emulator](http://www.turing.org.uk/turing/scrapbook/tmjava.html)
  - [Dimensions of 35mm film](http://www.brianpritchard.com/Fig%202.jpg)
  - [Dimensions of 35mm film (alt)](https://www.stereoscopy.com/faq/standard35ansi.gif)
  - [Robotic Calligraphy](http://calligraphybyherald.wix.com/herald#!gallery/c1zy6)

## Raspberry Pi
 - [Touchscreen Drivers] (http://engineering-diy.blogspot.com/2013/01/adding-7inch-display-with-touchscreen.html)
 - [Modifying the Pi SD card on a Mac](http://pi.gbaman.info/?p=328)

### Setting up the console cable
 - The following [tutorial](https://learn.adafruit.com/downloads/pdf/adafruits-raspberry-pi-lesson-5-using-a-console-cable.pdf) worked perfectly.  Screen should be able connect to the serial port after you install the driver.

 >screen /dev/tty.usbserial 115200
