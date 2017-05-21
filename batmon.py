#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
batmon.py - Monitor laptop battery state

The only command line argument is a path
to the config file.
This is optional, default is '/etc/batmon.conf'
"""


import sys
import os
import glob
import signal
import psutil
import time
import dbus
import configparser


def main(cfg):
    while True:

        # read current battery values
        energy_now = 0
        power_now = 0
        for bat in glob.glob(cfg['matchbat']):
            # read current energy level
            energy_now += file_to_int(bat + '/energy_now')
            # read current power drain
            power_now += file_to_int(bat + '/power_now')

        # calc runtime
        minutes = -1
        if power_now > 0:
            minutes = int((energy_now / power_now) * 60)

        # write text to state file for i3blocks and co
        write_file(cfg['statefile'], ("%i" % (minutes)))

        # notify i3blocks if present
        notify_process(cfg['notify_proc'], cfg['notify_sig'])

        # hibernate on low bat
        if minutes != -1:
            # check low bat
            if minutes < cfg['lowbat_limit']:
                if cfg['lowbat_action'] == 'hibernate':
                    hibernate()
                if cfg['lowbat_action'] == 'suspend':
                    suspend()

        # sleep until next cycle
        time.sleep(int(cfg['cycletime']))


def file_to_int(file):
    res = 0
    try:
        with open(file) as fp:
            res = int(fp.read())
            fp.close();
    except:
        pass
    return res


def write_file(fname, content):
    try:
        with open(fname, 'w') as fp:
            fp.write(content)
            fp.close()
    except:
        eprint('Error writing to: ' + fname)
        eprint(sys.exc_info()[0])


def notify_process(procname, sig):
    for proc in psutil.process_iter():
        if proc.name() == procname:
            os.kill(proc.pid, sig)


def hibernate():
    sysbus = dbus.SystemBus()
    logind = sysbus.get_object('org.freedesktop.login1', '/org/freedesktop/login1')
    manager = dbus.Interface(logind, 'org.freedesktop.login1.Manager')
    manager.Hibernate(True)
    time.sleep(10)


def suspend():
    sysbus = dbus.SystemBus()
    logind = sysbus.get_object('org.freedesktop.login1', '/org/freedesktop/login1')
    manager = dbus.Interface(logind, 'org.freedesktop.login1.Manager')
    manager.Suspend(True)
    time.sleep(10)


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def signal_handler(signal, frame):
    eprint('recevied SIGINT, bye bye')
    # TODO: cleanup statefile
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)

    # config file
    config_file = '/etc/batmon.conf'
    if len(sys.argv) > 1:
        if os.path.isfile(sys.argv[1]):
            config_file = sys.argv[1]

    # parse config
    config = configparser.RawConfigParser()
    config.read(config_file)

    cfg = {}
    try:
        cfg = {
            'cycletime':     config.get('general', 'cycletime'),
            'matchbat':      config.get('general', 'matchbat'),
            'statefile':     config.get('process_notify', 'statefile'),
            'notify_sig':    config.get('process_notify', 'notify_sig'),
            'notify_proc':   config.get('process_notify', 'notify_proc'),
            'lowbat_limit':  config.get('action', 'lowbat_limit'),
            'lowbat_action': config.get('action', 'lowbat_action')
        }
    except:
        eprint('Error parsing config: ' + config_file)
        eprint(sys.exc_info()[0])
        sys.exit(1)

    # execute
    main(cfg)
    sys.exit(0)

