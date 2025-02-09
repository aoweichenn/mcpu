import os

if __name__ == '__main__':
    dirname = os.path.dirname(os.path.abspath(__file__))
    with open("TenRom.bin", "wb") as fp:
        for var in range(256):
            var = str(var)
            var = int(var, base=16)
            byte = var.to_bytes(2, "little")
            fp.write(byte)
