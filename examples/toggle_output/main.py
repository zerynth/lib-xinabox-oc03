##############################################
#   This is an example for the OC01 module
#
#   The relay is toggled at 500 ms and the
# 	state printed to the console.
##############################################
# imports
import streams
from xinabox.oc03 import oc03

streams.serial()

# instantiate OC03 class
OC03 = oc03.OC03(I2C0)

# begin i2c bus
OC03.start()

# start OC03
OC03.init()

# sleep time
DELAY = 500

# infinite loop
while True:

    # close relay
    OC03.writePin(True)		
    print(OC03.getStatus()) # return state of relay to console
    sleep(DELAY)
    
    # open relay
    OC03.writePin(False)
    print(OC03.getStatus()) # return state of relay to console
    sleep(DELAY)