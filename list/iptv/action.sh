#!/bin/bash

# update IPTV address from Beijing-IPTV
curl -s https://raw.githubusercontent.com/qwerttvv/Beijing-IPTV/master/IPTV-Unicom.m3u \
| sed -e 's/192.168.123.1/192.168.8.5/g' \
> beijing_unicom.m3u
