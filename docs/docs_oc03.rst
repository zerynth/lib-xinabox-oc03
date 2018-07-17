.. module:: OC03

***************
 OC03 Module
***************

This is a Module for the OC03 Relay Out Low Voltage.
The board is based off the PCA9554A I/O expander manufactured by Texas Instruments.
The Module implements the PCA9554A to drive a solid state relay utilizing the `OC03 xChip <https://wiki.xinabox.cc/OC03_-_Relay_Out>`_.
The board uses I2C for communication.

Data Sheets:

-  `PCA9554A <http://www.ti.com/lit/ds/symlink/pca9554a.pdf>`_
-  `TLP241A <https://toshiba.semicon-storage.com/info/docget.jsp?did=14237&prodName=TLP241A>`_

    
===============
OC03 class
===============

.. class:: OC03(self, drvname, addr=PCA9554A_I2C_ADDRESS, clk=100000)

        Create an instance of the OC03 class.

        :param drvname: I2C Bus used '( I2C0, ... )'
        :param addr: Slave address, default 0x38
        :param clk: Clock speed, default 100kHz

    
.. method:: init(self, pins = PCA9554A_ALL_OUTPUTS_OFF)

        Configures PCA9554A and sets all outputs False by default

        :param pins: initializes the relay state. Accepts True (relay closed) and False (relay open)

        
.. method:: writePin(self, state)

        Determines the status of the relay output

        :param state: accepts True (relay closed) and False (relay open)

        
.. method:: getStatus(self)

        Reads the status of the relay.

        returns the status of the relay.

        
