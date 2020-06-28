## Usb python

import usb.core
import usb.util

class USBCKOZ:
    """Definition of controlling ckoz3"""
    LXC_MAX_OUT_PACKET_SIZE = 9
    LXC_MAX_IN_PACKET_SIZE = 19
    LXC_SEND_TIMEOUT = 1000
    LXC_RECV_TIMEOUT = 1000
    LXC_USB_VENDOR = 0x188a # Moeller 0x188a
    LXC_USB_PRODUCT = 0x1101 # USB gateway interface 0x1101
    LXC_USB_INTERFACE = 0
    LXC_USB_ENDPOINT_IN = 0x81 #// EP 1 IN
    LXC_USB_ENDPOINT_OUT = 0x02 #// EP 2 OUT

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

ckoz3 = USBCKOZ()

ckoz3.connectToDevice() 