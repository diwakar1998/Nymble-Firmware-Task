The repo contains my implementation of the firmware task. https://nymblelabs.notion.site/Firmware-Task-5177116a6cb94643871d8cf39c1f345f

main.c :
Firmware for the controller. Receives the message sent from PC. After receiving is completed is able to transmit the message back to the PC via uart.
This file is part of stm32 project. In order to see the code work create a stm32 project and setup all the required pins.

uart.py:
Pc side code is written using pyserial. Message is transmitted and received. During transmission and reception the speed of data transfer is printed on the console.

*The EEPROM part is still pending but the uart transmission and receiving to and from PC are completed.
