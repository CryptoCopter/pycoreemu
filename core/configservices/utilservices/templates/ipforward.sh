#!/bin/sh
# auto-generated by IPForward service (utility.py)
sysctl -w net.ipv4.conf.all.forwarding=1
sysctl -w net.ipv4.conf.default.forwarding=1
sysctl -w net.ipv6.conf.all.forwarding=1
sysctl -w net.ipv6.conf.default.forwarding=1
sysctl -w net.ipv4.conf.all.send_redirects=0
sysctl -w net.ipv4.conf.default.send_redirects=0
sysctl -w net.ipv4.conf.all.rp_filter=0
sysctl -w net.ipv4.conf.default.rp_filter=0
# setup forwarding for node interfaces
% for devname in devnames:
sysctl -w net.ipv4.conf.${devname}.forwarding=1
sysctl -w net.ipv4.conf.${devname}.send_redirects=0
sysctl -w net.ipv4.conf.${devname}.rp_filter=0
% endfor
