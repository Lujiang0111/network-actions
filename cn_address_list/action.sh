#!/bin/bash

# update from geolite2
curl -s https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/geolite2_country/country_cn.netset \
| sed -e '/^#/d'\
| sed -e 's/^/add address=/g' -e 's/$/ list=CNIP/g' \
| sed -e '1i/ip firewall address-list' -e '1iremove [/ip firewall address-list find list=CNIP]' -e '1iadd address=10.0.0.0/8 list=CNIP comment=private-network' -e '1iadd address=172.16.0.0/12 list=CNIP comment=private-network' -e '1iadd address=192.168.0.0/16 list=CNIP comment=private-network' \
> geolite2.rsc

# update from chnroutes2
curl -s https://raw.githubusercontent.com/misakaio/chnroutes2/master/chnroutes.txt \
| sed -e '/^#/d'\
| sed -e 's/^/add address=/g' -e 's/$/ list=CNIP/g' \
| sed -e '1i/ip firewall address-list' -e '1iremove [/ip firewall address-list find list=CNIP]' -e '1iadd address=10.0.0.0/8 list=CNIP comment=private-network' -e '1iadd address=172.16.0.0/12 list=CNIP comment=private-network' -e '1iadd address=192.168.0.0/16 list=CNIP comment=private-network' \
> chnroutes2.rsc
