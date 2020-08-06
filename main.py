#!/usr/bin/env python3
import os
from utils import pp
from time import sleep
from collections import namedtuple

# Keeps PyGame from opening it's big dumb mouth.
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import midi

def device_discovery():
    dev_count = midi.get_count()
    if dev_count:
        for ID in range(0,dev_count):
            device = midi.get_device_info(ID)
            if device[1] == b'WORLDE easy control' and device[2]:
                return ID



def read_device(d_id):
    handle = midi.Input(d_id)
    poll = handle.poll
    read = handle.read

    while(True):
        events = poll()
        if events:
            message = read(1024)
            if message[0][0][0] == 176:
                message = message[0][0]
                message = (message[1],message[2])

            # This covers the weird proprietary/special 'BANK' key.
            else:
                message = (0, message[-1][0][1])

            # Clear as mud
            print('[{}]'.format('|'*int(( int(message[1])/2 ))))

def main():
    midi.init()
    d_id = device_discovery()

    read_device(d_id)

if __name__ == '__main__':
    main()
