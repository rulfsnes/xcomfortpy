## Usb python
import usb.core
class USBCKOZ:
    """Definition of controlling ckoz3"""
    LXC_MAX_OUT_PACKET_SIZE = 9
    LXC_MAX_IN_PACKET_SIZE = 19
    LXC_SEND_TIMEOUT = 1000
    LXC_RECV_TIMEOUT = 1000
    LXC_USB_VENDOR = "0x188a" # Moeller 0x188a
    LXC_USB_PRODUCT = "0x1101" # USB gateway interface 0x1101
    LXC_USB_INTERFACE = 0
    LXC_USB_ENDPOINT_IN = "0x81" #// EP 1 IN
    LXC_USB_ENDPOINT_OUT = "0x02" #// EP 2 OUT


print("Testing usb connectivity")
interface = USBCKOZ()
print(interface.LX)