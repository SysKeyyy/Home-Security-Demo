# Home-Security-Demo
__________________________________________________________________________________________________________
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
__________________________________________________________________________________________________________

A facial recognition program that plays a alarm (mp3 file) when a person is seen in the room. A basic theif using Python and OpenCV.

# Setup
__________________________________________________________________________________________________________

To run this, you will need a windows machine to be available to hear the alarm, if you want to run it on linux,
for a RaspberryPI then you will need to chnage the line:
``os.system("start alarm.mp3")``
to:
``os.system("nvlc alarm.mp3")``
Keep in mind that the Linux command requires you to have VLC installed in the system.

__________________________________________________________________________________________________________


# Alternatives
__________________________________________________________________________________________________________

This script uses "haar cascades" to identify objects, by replacing the existing one with another one, like car, or smile
the script is going to get notifyed in case of that event instead.


.:: Have fun ! And have a good day !! ::.
