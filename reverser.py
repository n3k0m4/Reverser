#!/usr/bin/env python3

class reverser():
    def __init__(self, *args):
        pass

    def reverse(self, address: str) -> str:
        len_ = len(address)
        if (len_ != 8) and (len_ % 2 != 0):
            return ""
        elif (len_ != 8) and (len_ % 2 == 0):
            new_address = "2A"*((8-len(address))//2) + address
            return self.reverse(new_address)
        else:
            return chr(int(address[6:8], 16)) + chr(int(address[4:6], 16)) + chr(int(address[2:4], 16))+chr(int(address[0:2], 16))

    def resolve(self, buffer: str) -> str:
        res = ""
        buffer = buffer.replace(" ", "")
        values_list = buffer.split('0x')[1:]
        for val in values_list:
            res += self.reverse(val)
        return res


if __name__ == '__main__':
    data = "0x7b425448  0x5f796877  0x5f643164  0x34735f31  0x745f3376  0x665f3368  0x5f67346c  0x745f6e30  0x355f3368  0x6b633474  0x7d213f  0xe5df5a00  0xf7f093fc  0x56568f8c  0xff90a748  0x56566441 "
    rev = reverser()
    print(rev.resolve(data))
