import re
import requests

url_base = "https://raw.githubusercontent.com/v2fly/domain-list-community/refs/heads/master/data/"

category_list = [
    "115",
    "alibaba",
    "amazon",
    "category-ai-!cn",
    "category-ai-cn",
    "category-bank-cn",
    "category-communication",
    "category-entertainment",
    "category-entertainment-cn",
    "category-games",
    "category-netdisk-cn",
    "category-ntp",
    "category-porn",
    "category-pt",
    "category-social-media-!cndocker",
    "google",
    "jd",
    "microsoft",
    "mikrotik",
    "pikpak",
    "tencent",
    "yandex",
]

parsed_category_list = []


def ConvertFromContent(category, content):
    file_map = {}
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
                ConvertFormCategory(domain)
            elif prefix == "full":
                file_map[suffix].write(f"DOMAIN,{domain}\n")
            else:
                continue
        else:
            file_map[suffix].write(f"DOMAIN-SUFFIX,{domain}\n")

    for f in file_map.values():
        f.close()


def ConvertFormCategory(category):
    if category in parsed_category_list:
        return
    parsed_category_list.append(category)

    while True:
        print(f"convert category {category} ...")
        try:
            response = requests.get(f"{url_base}{category}")
        except Exception as e:
            print(f"request error: {e}, retry")
            continue

        ConvertFromContent(category, response.text)
        break


if __name__ == "__main__":
    for category in category_list:
        ConvertFormCategory(category)
