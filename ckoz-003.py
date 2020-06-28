## Usb python

import usb.core
import usb.util
import usb.backend.libusb1

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
print("Opening device Vendor: " + str(ckoz3.LXC_USB_VENDOR) + ", Product: " + str(ckoz3.LXC_USB_PRODUCT))

usbDevice = usb.core.find(idVendor = ckoz3.LXC_USB_VENDOR, idProduct = ckoz3.LXC_USB_PRODUCT)
USBBackend = usb.backend.libusb1.get_backend()
if usbDevice is None:
    raise ValueError("Device not found")

print("Device opened successfully")
#set kernel driver mode
ret = USBBackend.lib.libusb_kernel_driver_active(usbDevice, ckoz3.LXC_USB_INTERFACE)
if ret == 1:
    ret = USBBackend.lib.libusb_detach_kernel_driver(usbDevice, ckoz3.LXC_USB_INTERFACE)
    if ret != 0:
        USBBackend.lib.libusb_close(usbDevice)
        raise ValueError("Cannot detach device kernel driver")