#!/usr/bin/env python3
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import midi
from utils import pp
from time import sleep

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
            stuff = read(1024)
            pp(stuff)


def main():
    midi.init()
    d_id = device_discovery()

    try:
        read_device(d_id)
    except:
        pass

if __name__ == '__main__':
    main()
