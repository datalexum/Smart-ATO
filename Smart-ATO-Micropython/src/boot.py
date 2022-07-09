# boot.py - - runs on boot-up
from os.path import exists
from update import update

if exists('UPDATE'):
    update.update_device()