from machine import Pin
import time
from font import font #font data can be accessed directly as font['A'] etc
Test

row1 = Pin(0, Pin.OUT)
row2 = Pin(1, Pin.OUT)
row3 = Pin(2, Pin.OUT)
row4 = Pin(3, Pin.OUT)
row5 = Pin(4, Pin.OUT)
row6 = Pin(5, Pin.OUT)
row7 = Pin(6, Pin.OUT)
row8 = Pin(7, Pin.OUT)
row9 = Pin(17, Pin.OUT)
row10 = Pin(16, Pin.OUT)
row11 = Pin(15, Pin.OUT)
row12 = Pin(14, Pin.OUT)
row13 = Pin(10, Pin.OUT)
row14 = Pin(11, Pin.OUT)
row15 = Pin(12, Pin.OUT)
row16 = Pin(13, Pin.OUT)
data = Pin(18, Pin.OUT)
clk = Pin(8, Pin.OUT)
update = Pin(9, Pin.OUT)

frameData = [16,0,8,0,4,0,2,0,1] + [0 for i in range(320-9)]


def rowTest():
    while True:
        data.off()
        clk.on()
        clk.off()
        data.on()
        update.on()
        update.off() #now rightmost column selected
        for column in range(319,-1,-1):
            row1.value(frameData[column] & 1)
            row2.value(frameData[column] & 2)
            row3.value(frameData[column] & 4)
            row4.value(frameData[column] & 8)
            row5.value(frameData[column] & 16)
            row6.value(frameData[column] & 32)
            row8.value(frameData[column] & 64)
            row9.value(frameData[column] & 128)
            row10.value(frameData[column] & 256)
            row11.value(frameData[column] & 512)
            row12.value(frameData[column] & 1024)
            row13.value(frameData[column] & 2048)
            row14.value(frameData[column] & 4096)
            row15.value(frameData[column] & 8192)
            row16.value(frameData[column] & 16384)
            time.sleep_us(1) #data displayed, wait
            clk.on()
            clk.off()
            update.on()
            update.off() #clock to next column


rowTest()
