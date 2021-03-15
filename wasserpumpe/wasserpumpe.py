from machine import Pin
import time

# define output
p21 = Pin(21, Pin.OUT)

# start pump
p21.value(1)
p21.on()
time.sleep(5)
print(p21.value())
#p21.value(0)