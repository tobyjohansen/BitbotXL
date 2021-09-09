# BitbotXL - Line Following Robot
This projects uses microbit and bitbotXL to make a Line Following Robot. By using light sensor beneath the robot it can follow a dark path. Example used is black tape on a white desk. This makes it possible for the Bitbot to follow the tape to a very accurate degree. There where some shortcommings in the design and end result. However the robot was able to follow a path laid before it with greate accuracy.

## Microbit and BitBotXL
The BitbotXL uses a Microbit. Microbit is a easy to use microcontroller that is targeted to kids and teenagers to learn programming and robotics. While usually the norm is to use what is called programming blocks to program the microbit and the BitbotXL. This project used python. python was used in order to get more accuracy and already familiarity with the language. Similary result can be achieved by using block programming, however for learnign purposes python was used.

## Libraries
The libraries used in the project are Microbit and Neopixel. Microbit is a library for controlling the microbit micro controller. Its used in this project to get access to the pins on the microcontroller and the i2C device controlling the light sensor. Neopixel library was used to get access to and control the ligths on the BitbotXL.

## Light Sensor
The main logic of the robot uses the light sensor. By using a black tape on a white background the robot uses light sensor to register if the robot is turnet to much to the side or not. The tape is run underneath the robot and on each side there is a light sensor. The black tape traps the light and stops if from returning to the sensor. With this you can create a logic where if one of the sensor stops recieving light the robot will turn in that direction and align itself back to the right path. If the robot is on the right path and none of the sensor goes off the robot will move forward.
