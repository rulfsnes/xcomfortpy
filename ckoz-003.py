## Usb python

import usb.core
import usb.util
import struct

class ckoZ3Data:
    size = 6
    #Format:size  pktType  dataPoint opcode value   unused
    #        06    b1       01        0c    28    00 00 00 00         
    def __init__(self, dataPoint, opCode, packetType, value):
        self.dataPoint = dataPoint
        self.opCode = opCode
        self.value = value 
        self.packetType = packetType
        self.data = struct.pack('BBBBBBBBB',self.size, self.packetType, self.dataPoint, self.opCode, self.value, 0x00,0x00,0x00,0x00)
  
    


class CKOZ3:
    """Definition of controlling ckoz3"""
    LXC_MAX_OUT_PACKET_SIZE = 9
    LXC_MAX_IN_PACKET_SIZE = 19
    LXC_SEND_TIMEOUT = 1000
    LXC_RECV_TIMEOUT = 1000
    LXC_USB_VENDOR = 0x188a # Moeller 0x188a
    LXC_USB_PRODUCT = 0x1101 # USB gateway interface 0x1101
    LXC_USB_INTERFACE = 0
    LXC_USB_ENDPOINT_IN = 0x81 ## EP 1 IN
    LXC_USB_ENDPOINT_OUT = 0x02 ## EP 2 OUT

    LXC_PKT_TYPE_OUT = 0xb1
    LXC_PKT_TYPE_IN = 0xc1
    LXC_PKT_TYPE_ACK = 0xc3

    LXC_OPCODE_ON_OFF = 0x0a # value = 0 means off, 1 means on
    LXC_OPCODE_DIM_GET = 0x0b # Get current value from actuator
    LXC_OPCODE_DIM_SET = 0x0c # Percent value 0-100
    LXC_OPCODE_DIM_GRADUAL_STOP = 0x0d # aka OFF BUTTON RELEASE (works for stopping both directions)
    LXC_OPCODE_DIM_GRADUAL_START = 0x0e # aka OFF/ON BUTTON HOLD: Start gradual dim up or down, value = 0 is down/off, 1 is up/on
    LXC_OPCODE_ON_OFF2 = 0x0f # seems identical to LXC_OPCODE_ON_OFF.

    LXC_OPCODE_SEND_MEASUREMENT_VALUE = 0x11
    LXC_OPCODE_SEND_MEASUREMENT_VALUE2 = 0x1a
    LXC_OPCODE_UNKNOWN1 = 0x2a
    LXC_OPCODE_UNKNOWN2 = 0x2b
    LXC_OPCODE_SEND_TEMPERATURE = 0x2c # Some kind of temperature
    LXC_OPCODE_SEND_MEASUREMENT_VALUE3 = 0x30 # Has zero decimals?
    LXC_OPCODE_SEND_MEASUREMENT_VALUE4 = 0x31 # Has one decimals?
    LXC_OPCODE_SEND_MEASUREMENT_VALUE5 = 0x32 # Has two decimals?
    LXC_OPCODE_SEND_MEASUREMENT_VALUE6 = 0x33 # Has three decimals?
    LXC_OPCODE_SEND_MEASUREMENT_VALUE7 = 0x40 # Has zero decimals?
    LXC_OPCODE_SEND_MEASUREMENT_VALUE8 = 0x41 # Has one decimals?
    LXC_OPCODE_SEND_MEASUREMENT_VALUE9 = 0x42 # Has two decimals?
    LXC_OPCODE_SEND_MEASUREMENT_VALUE10 = 0x43 # Has three decimals?
    LXC_OPCODE_SEND_TEMPERATURE2 = 0x44
    LXC_OPCODE_SEND_TEMPERATURE3 = 0x45

    def connectToDevice(self):
        print("Opening device Vendor: " + str(self.LXC_USB_VENDOR) + ", Product: " + str(self.LXC_USB_PRODUCT))
        self.device = usb.core.find(idVendor = self.LXC_USB_VENDOR, idProduct = self.LXC_USB_PRODUCT)
        if self.device is None:
            raise ValueError("Device not found")
        kernelActive = self.device.is_kernel_driver_active(self.LXC_USB_INTERFACE)
        if  kernelActive == True:
           self.device.detach_kernel_driver(self.LXC_USB_INTERFACE)

        self.device.set_configuration(1)      
        usb.util.claim_interface(self.device, self.LXC_USB_INTERFACE)
        print("Connected to device")
    
    def setDimLevel(self, dataPoint, level):
        data = ckoZ3Data(dataPoint=dataPoint, opCode=self.LXC_OPCODE_DIM_SET, value=level, packetType=self.LXC_PKT_TYPE_OUT)
        print(data.data)    
        out = self.device.write(self.LXC_USB_ENDPOINT_OUT, data.data , self.LXC_SEND_TIMEOUT)
        print(out)


ckoz = CKOZ3()
ckoz.connectToDevice()
ckoz.setDimLevel(2, 100)
