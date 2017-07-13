#!/bin/sh

HOSTNAME="$(hostname)"
ADDRESS="$(dig +short $HOSTNAME.node.consul)"
mitmproxy -b $ADDRESS -s filter.py
