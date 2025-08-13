#!/bin/bash

# update IPTV address from Beijing-IPTV
curl -s https://raw.githubusercontent.com/qwerttvv/Beijing-IPTV/master/IPTV-Unicom.m3u |
    sed -e 's/192.168.123.1/172.28.8.21/g' \
        >beijing_unicom.m3u

curl -s https://raw.githubusercontent.com/qwerttvv/Beijing-IPTV/refs/heads/master/IPTV-Unicom-Multicast.m3u \
    >beijing_unicom_multicast.m3u
