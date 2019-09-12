#!/usr/bin/env python

import argparse
import atexit
import sh
import sys

PARSER = argparse.ArgumentParser()
PARSER.add_argument('disks', metavar='disk', nargs='+')
ARGS = PARSER.parse_args()

def init():
    sh.sudo.zpool('create', 'tank', ARGS.disks)
    sh.sudo.zfs('create', 'tank/fish')

def fini():
    try:
        # Dump some pool history when exiting...
        history = sh.sudo.zpool('history', '-i', 'tank').stdout
        for line in history.split('\n')[-10:]:
            print(line)

        sh.sudo.zpool('destroy', 'tank')
    except sh.ErrorReturnCode:
        pass

def repro():
    sh.sudo.zfs('set', 'sharenfs=on', 'tank/fish')

    one = sh.sudo.zfs('set', 'sharenfs=off', 'tank/fish', _bg=True)
    two = sh.sudo.zfs('set', 'sharenfs=off', 'tank/fish', _bg=True)

    one.wait()
    two.wait()

if __name__ == '__main__':
    atexit.register(fini)
    init()

    i = 0
    while True:
        i += 1
        sys.stdout.write("\rIteration: %i" % i)
        sys.stdout.flush()
        repro()
