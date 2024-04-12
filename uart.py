import serial,time
from timeit import default_timer as timer

uartPort = serial.Serial('/dev/ttyUSB0')
uartPort.baudrate = 2400
print('Port Details:{0}\n'.format(uartPort))

message = "Finance Minister Arun Jaitley Tuesday hit out at former RBI governor Raghuram Rajan for predicting that the next banking crisis would be triggered by MSME lending, saying postmortem is easier than taking action when it was required. Rajan, who had as the chief economist at IMF warned of impending financial crisis of 2008, in a note to a parliamentary committee warned against ambitious credit targets and loan waivers, saying that they could be the sources of next banking crisis. Government should focus on sources of the next crisis, not just the last one.\
In particular, government should refrain from setting ambitious credit targets or waiving loans. Credit targets are sometimes achieved by abandoning appropriate due diligence, creating the environment for future NPAs,\" Rajan said in the note.\" Both MUDRA loans as well as the Kisan Credit Card, while popular, have to be examined more closely for potential credit risk. Rajan, who was RBI governor for three years till September 2016, is currently.*"

message_Bytes = bytes(message,'utf-8')

# while(True):
#     condition = input("Enter y or n :")
#     if(condition == 'n'):
#         break
transmit_Start = timer()
uartPort.write(message_Bytes)
transmit_End = timer()

# print('Time Elapsed to send data\n', transmit_End - transmit_Start)
print('Transmit Speed bits/sec: {0}\n'.format(len(message_Bytes)*8/(transmit_End - transmit_Start)))
# time.sleep(2)

receivedMessage=''

timeDiff=0
start = timer()
prevlen = 0

while(True):
    curTime = timer()
    tmp = uartPort.read()
    tmp_str = str(tmp.decode('utf-8'))
    #time difference between start and curtime measurement. If it is >= 1 then transmission speed is printed on screen
    timeDiff = curTime-start
    if(timeDiff >= 1):
        curlen = len(receivedMessage)
        speed = ((curlen - prevlen ) / timeDiff)*9
        print('Receive Speed bits/sec: {0}\n'.format(speed))
        prevlen = curlen
        start = timer()
    #Exit loop when this character is received
    if(tmp_str == '*'):
        curlen = len(receivedMessage)
        speed = ((curlen - prevlen ) / timeDiff)*9
        print('Receive Speed bits/sec: {0}\n'.format(speed))
        break
    receivedMessage+=tmp_str
print('Data Received: \n{0}\n'.format(receivedMessage))

uartPort.close()  