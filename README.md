# 网络相关Actions

## CN_address_list

+ 每日凌晨1点更新CN address list，提供给ros使用。
+ 已包含```10.0.0.0/8```、```172.16.0.0/12```、```192.168.0.0/16```内网IP段。
+ 文件列表：
  + ```geolite2.rsc```：使用[geolite2](https://github.com/firehol/blocklist-ipsets/tree/master/geolite2_country)源
  + ```chnroutes2.rsc```：使用[chnroutes2](https://github.com/misakaio/chnroutes2)源。
