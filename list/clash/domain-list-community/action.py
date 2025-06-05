import re
import requests

category_url_base = "https://raw.githubusercontent.com/v2fly/domain-list-community/refs/heads/master/data/"

category_list = [
    "apple",
    "category-ai-cn",
    "category-ai-!cn",
    "category-cas",
    "category-collaborate-cn",
    "category-communication",
    "category-container",
    "category-entertainment",
    "category-entertainment-cn",
    "category-games",
    "category-game-accelerator-cn",
    "category-game-platforms-download",
    "category-netdisk-cn",
    "category-ntp",
    "category-pt",
    "category-social-media-!cn",
    "category-social-media-cn",
    "category-speedtest",
    "docker",
    "github",
    "google",
    "microsoft",
    "steam",
]

custom_url_base = "https://raw.githubusercontent.com/Lujiang0111/Scripts/refs/heads/main/Openwrt/Clash/domain-list-community/"

custom_list = [
    "custom-cloud",
    "custom-cloud-cn",
    "custom-netdisk",
    "custom-netdisk-cn",
    "custom-porn",
]


def ConvertFromContent(category, content, file_map):
    for line in content.splitlines():
        line = re.sub(r"#.*", "", line).strip()
        if line.startswith("#"):
            continue

        line_prefix, line_domain, line_suffix = "", "", ""
        if "@" in line:
            line, line_suffix = line.rsplit("@", 1)

        if ":" in line:
            line_prefix, line_domain = line.split(":", 1)
        else:
            line_domain = line

        prefix, domain, suffix = "", "", ""
        if line_prefix:
            prefix = line_prefix.strip()
        if line_domain:
            domain = line_domain.strip()
        if line_suffix:
            suffix = line_suffix.strip()

        if suffix not in file_map:
            if suffix:
                file_map[suffix] = open(f"{category}_{suffix}.list", "w")
            else:
                file_map[suffix] = open(f"{category}.list", "w")

        if not domain:
            continue

        if prefix:
            if prefix == "include":
                if domain.startswith("category-"):
                    continue
                sub_content = RequstUrl(category, f"{category_url_base}{domain}")
                ConvertFromContent(category, sub_content, file_map)
            elif prefix == "full":
                file_map[suffix].write(f"DOMAIN,{domain}\n")
            elif prefix == "regexp":
                file_map[suffix].write(f"DOMAIN-REGEX,{domain}\n")
            else:
                continue
        else:
            file_map[suffix].write(f"DOMAIN-SUFFIX,{domain}\n")


def RequstUrl(category, url) -> str:
    retry_times = 0
    while True:
        print(f"request category={category}, url={url}...")
        try:
            response = requests.get(f"{url}")
        except Exception as e:
            if retry_times < 5:
                retry_times += 1
                print(f"request error: {e}, retry times={retry_times}")
                continue
            else:
                print(f"request error: {e}, ignore")
                break
        break
    return response.text


if __name__ == "__main__":
    for category in category_list:
        content = RequstUrl(category, f"{category_url_base}{category}")
        file_map = {}
        ConvertFromContent(category, content, file_map)
        for f in file_map.values():
            f.close()

    for category in custom_list:
        content = RequstUrl(category, f"{custom_url_base}{category}")
        file_map = {}
        ConvertFromContent(category, content, file_map)
        for f in file_map.values():
            f.close()
