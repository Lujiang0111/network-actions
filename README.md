# 网络相关Actions

## list

+ 每日凌晨1点更新所有list

### cn_address

+ 提供给ros使用的中国地址列表。
+ 已包含```10.0.0.0/8```、```172.16.0.0/12```、```192.168.0.0/16```、```组播```IP段。
+ 文件列表：
  + ```geolite2.rsc```：使用[geolite2](https://github.com/firehol/blocklist-ipsets/tree/master/geolite2_country)源。
  + ```chnroutes2.rsc```：使用[chnroutes2](https://github.com/misakaio/chnroutes2)源。

### iptv

+ 提供udpxy转换后的IPTV播放列表（端口23234）。
+ 文件列表：
  + ```beijing_unicom.m3u```：北京联通。

### clash

+ 提供转换后的clash list
