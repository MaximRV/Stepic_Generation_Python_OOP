class IPAddress:
    def __init__(self, ip):
        if isinstance(ip, str):
            self.ip = ip.split('.')
        else:
            self.ip = ip

    def __str__(self):
        return f'{self.ip[0]}.{self.ip[1]}.{self.ip[2]}.{self.ip[3]}'

    def __repr__(self):
        return f"IPAddress('{self.ip[0]}.{self.ip[1]}.{self.ip[2]}.{self.ip[3]}')"


ip = IPAddress((1, 1, 11, 11))

print(str(ip))
print(repr(ip))