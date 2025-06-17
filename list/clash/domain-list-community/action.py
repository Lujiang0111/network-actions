import re
import sys
import urllib.parse
import requests
import urllib


class Action:
    __category_url_base = "https://raw.githubusercontent.com/v2fly/domain-list-community/refs/heads/master/data/"
    __category_list = [
        "steam",
        "category-ai-cn",
        "category-ai-!cn",
        "category-collaborate-cn",
        "category-communication",
        "category-dev",
        "category-container",
        "category-entertainment",
        "category-entertainment-cn",
        "category-game-platforms-download",
        "category-games",
        "category-pt",
        "category-social-media-cn",
        "category-social-media-!cn",
        "docker",
        "github",
        "microsoft",
        "apple",
        "google",
        "nvidia",
    ]

    __custom_url_base = "https://raw.githubusercontent.com/Lujiang0111/Scripts/refs/heads/main/Openwrt/Clash/domain-list-community/"
    __custom_list = [
        "custom-cloud",
        "custom-cloud-cn",
        "custom-porn",
    ]

    __url_dic = {}

    def main(self, args) -> None:
        for category in self.__category_list:
            self.parse_head_category(self.__category_url_base, category)
        for category in self.__custom_list:
            self.parse_head_category(self.__custom_url_base, category)

    def request_url(self, url_base, category) -> str:
        url = urllib.parse.urljoin(url_base, category)
        if url in self.__url_dic:
            return self.__url_dic[url]

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

        self.__url_dic[url] = response.text
        return self.__url_dic[url]

    def parse_head_category(self, url_base, category) -> None:
        file_dic = {}
        category_dic = {}
        self.parse_category(category, url_base, category, file_dic, category_dic)
        for f in file_dic.values():
            f.close()

    def parse_category(
        self, file_prefix, url_base, category, file_dic, category_dic
    ) -> None:
        if category in category_dic:
            return
        category_dic[category] = True

        content = self.request_url(url_base, category)
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

            if suffix not in file_dic:
                if suffix:
                    file_dic[suffix] = open(f"{file_prefix}_{suffix}.list", "w")
                else:
                    file_dic[suffix] = open(f"{file_prefix}.list", "w")

            if not domain:
                continue

            if prefix:
                if prefix == "include":
                    self.parse_category(
                        file_prefix,
                        self.__category_url_base,
                        domain,
                        file_dic,
                        category_dic,
                    )
                elif prefix == "full":
                    file_dic[suffix].write(f"DOMAIN,{domain}\n")
                elif prefix == "regexp":
                    file_dic[suffix].write(f"DOMAIN-REGEX,{domain}\n")
                else:
                    continue
            else:
                file_dic[suffix].write(f"DOMAIN-SUFFIX,{domain}\n")


if __name__ == "__main__":
    prebuild = Action()
    prebuild.main(sys.argv)
