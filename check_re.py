import re


class check_re:

    @staticmethod
    def is_valid_ipv4(ip):
        # 定义IPv4地址的正则表达式
        ipv4_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
        return bool(ipv4_pattern.match(ip))

    @staticmethod
    def is_valid_ipv6(ip):
        # 定义IPv6地址的正则表达式
        ipv6_pattern = re.compile(r'^([0-9a-fA-F]{0,4}:){7}[0-9a-fA-F]{0,4}$')
        return bool(ipv6_pattern.match(ip))

    @staticmethod
    def is_valid_mac_address(mac):
        # 定义MAC地址的正则表达式
        mac_pattern = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
        return bool(mac_pattern.match(mac))


if __name__ == '__main__':
    ip = "192.168.1.1"
    check_re.is_valid_ipv4(ip)
    mac = "00:11:22:33:44:55"
    check_re.is_valid_mac_address(mac)
