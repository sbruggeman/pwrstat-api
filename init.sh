#!/bin/bash

/etc/init.d/pwrstatd start
/bin/sleep 3
/usr/sbin/pwrstat -pwrfail -shutdown off
/usr/sbin/pwrstat -lowbatt -shutdown off
/src/pwrstat-api.py
