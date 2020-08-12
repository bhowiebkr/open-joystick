# Open Joystick

This is a 3d printed open source joystick in the works.

## Mechanical features
-  dual cams per axis.
- A twist axis that is also dual cam actuated.
- Force feedback using electromagnetic induction.
- All axis, and cam assemblies will be moving on ball bearings.
- Stick will have left and right variants. (I’m left handed so will be working on the left one. Right will be a mirror of the left)


## Electrical feature
- Because of the electromagnets, I don’t think hall effect angle sensors would work and will look at using potentiometers instead. 
- Microcontroller using the Arduino ecosystem.

## Software features
- Arduino based joystick implementation.


![CAD](publish/joystick_gimbal_v1.02.png)

## Media

### Video 2 - Twist axis and force feedback using electromagnetic coils.

The grip attaches to the upper twist assembly through 2 bearings (the big and small one). This should give enough contact for the grip to not wobble around. 

I have used the cams way of adding tension to the twist and it has added alot of bulk to the entire mechanism. Not sure if it’s entirely worth doing. The profile of the cams for the twist axis will need further adjusting as the tension doesn’t look like it’ll ramp up enough. The twist cams are meant to be tensioned by a spring that connects below.

[![3d printed Joystick gimbal design and assembly motion.](http://img.youtube.com/vi/51jVKvQhhOk/0.jpg)](https://www.youtube.com/watch?v=51jVKvQhhOk "3d printed Joystick gimbal design and assembly motion.")

### Video 1 - initial design
This video shows basically the full assembly of the original design by olukelo. Some minor changes were made where parts had interference with each other. Cam springs/elastic bands not visualized in this assembly.
- He has a github repo for that [project found here](https://github.com/o-devices/o-joystick-hdk) that includes STL and Solidworks source files.
- And the [Thingiverse page](https://www.thingiverse.com/thing:2496028#How%20I%20Designed%20This)
- A working 3d print of the [Olukelo's design by Slarti Bartfast](https://www.youtube.com/watch?v=H3n42BAMKc0)

[![3d printed Joystick gimbal design and assembly motion.](http://img.youtube.com/vi/erjnODXnVpg/0.jpg)](https://www.youtube.com/watch?v=erjnODXnVpg "3d printed Joystick gimbal design and assembly motion.")

