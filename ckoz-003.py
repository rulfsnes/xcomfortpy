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

ckoz3 = USBCKOZ()
print("Testing usb connectivity")
print("Opening device Vendor: " + ckoz3.LXC_USB_VENDOR + ", Product: " + ckoz3.LXC_USB_PRODUCT)

usbDevice = usb.core.find(idVendor = ckoz3.LXC_USB_VENDOR, idProduct = ckoz3.LXC_USB_PRODUCT)

if usbDevice is None:
    raise ValueError("Device not found")

print("Device opened successfully")