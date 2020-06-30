#Test libxcomfort in python
#make libary with gcc -Wall -shared -o libxcomfort.so -fPIC libxcomfort.c -lusb-1.0
import ctypes

libxcomfort = ctypes.CDLL('./libxcomfort.so')

libxcomfort.lxc_init()

lxc_dev = libxcomfort.lxc_open()
print(libxcomfort.lxc_get_dim_level(lxc_dev, 2))
libxcomfort.lxc_set_dim_level(lxc_dev, 2, 0)