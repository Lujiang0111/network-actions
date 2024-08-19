#!/bin/bash

ori_urls=(
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Lan/Lan.list"
)

for url in "${ori_urls[@]}"; do
    file_name=$(basename "${url}")
    curl -s "${url}" >"${file_name}"
done

del_ip_cidr_urls=(
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/AmazonCN/AmazonCN.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Cloudflarecn/Cloudflarecn.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Game/GameDownloadCN/GameDownloadCN.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/GovCN/GovCN.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/SteamCN/SteamCN.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Cloud/CloudCN/CloudCN.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/GoogleFCM/GoogleFCM.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/OpenAI/OpenAI.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Copilot/Copilot.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Blizzard/Blizzard.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Epic/Epic.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Origin/Origin.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Sony/Sony.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Steam/Steam.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Nintendo/Nintendo.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Telegram/Telegram.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/OneDrive/OneDrive.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Microsoft/Microsoft.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Apple/Apple.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/AppleProxy/AppleProxy.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/ChinaMedia/ChinaMedia.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/GlobalMedia/GlobalMedia.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/China/China.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/GitHub/GitHub.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Google/Google.list"
    "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Docker/Docker.list"
)

for url in "${del_ip_cidr_urls[@]}"; do
    file_name=$(basename "${url}")
    curl -s "${url}" |
        sed -e '/^IP-CIDR/d' \
            -e '/^IP-ASN/d' \
            >"${file_name}"
done

# GameDownloadCN.list Setting
sed -i '/microsoft.com/d' GameDownloadCN.list
echo 'DOMAIN-SUFFIX,patch-dl.ffxiv.com' >>GameDownloadCN.list

game_urls=(
    "https://raw.githubusercontent.com/FQrabbit/SSTap-Rule/master/rules/DiabloIV-HK.rules"
    "https://raw.githubusercontent.com/FQrabbit/SSTap-Rule/master/rules/FINAL-FANTASY-XIV-cn.rules"
    "https://raw.githubusercontent.com/FQrabbit/SSTap-Rule/master/rules/Final-Fantasy-XIV.rules"
    "https://raw.githubusercontent.com/FQrabbit/SSTap-Rule/master/rules/PathOfexile.rules"
)

for url in "${game_urls[@]}"; do
    file_name=$(basename "${url}")
    curl -s "${url}" |
        sed -e '/^[[:space:]]*#/d' |
        sed -e 's/^[[:space:]]*/IP-CIDR,/' \
            -e 's/[[:space:]]*$/,no-resolve/' \
            >"game/${file_name}"
done
