import os
import requests
import urllib.parse

url_list = [
    "https://raw.githubusercontent.com/v2fly/domain-list-community/refs/heads/master/data/apple"
]


def Convert(base_name, content):
    file_map = {}
    for line in content.splitlines():
        if line.lstrip().startswith("#"):
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
            prefix = line_prefix.split()[0]
        if line_domain:
            domain = line_domain.split()[0]
        if line_suffix:
            suffix = f"_{line_suffix.split()[0]}"

        if suffix not in file_map:
            file_map[suffix] = open(f"{base_name}{suffix}.list", "w")

        if not domain:
            continue

        if prefix:
            if prefix == "full":
                file_map[suffix].write(f"DOMAIN,{domain}\n")
            else:
                continue
        else:
            file_map[suffix].write(f"DOMAIN-SUFFIX,{domain}\n")

    for f in file_map.values():
        f.close()


if __name__ == "__main__":
    for url in url_list:
        response = requests.get(url)
        parsed_url = urllib.parse.urlparse(url)
        file_name = os.path.basename(parsed_url.path)
        Convert(file_name, response.text)
