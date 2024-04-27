from typing import Union


def toBytes(data: Union[int, str]) -> bytes:
    if isinstance(data, str):
        return data.encode(encoding='utf-8')
    elif isinstance(data, int):
        size = round((data.bit_length() + 7) / 8)
        # size2 = (data.bit_length() + 7) // 8
        return data.to_bytes(size, 'big')
    else:
        pass  # error


def encode(data: Union[int, str, list]) -> bytes:
    if isinstance(data, int) or isinstance(data, str):
        byteData = toBytes(data)
        lenByteData = len(byteData)
        if lenByteData == 1 and ord(byteData) <= 0x7f:
            return byteData
        elif lenByteData <= 55:
            return (0x80 + lenByteData).to_bytes(1, 'big') + byteData
        else:
            size = round((lenByteData.bit_length() + 7) / 8)
            # size2 = (lenByteData.bit_length() + 7) // 8
            return (0xb7 + size).to_bytes(1, 'big') + lenByteData.to_bytes(size, 'big') + byteData
    elif isinstance(data, list):
        byteData = b''
        for val in data:
            byteData += encode(val)
        lenByteData = len(byteData)
        if lenByteData <= 55:
            return (0xc0 + lenByteData).to_bytes(1, 'big') + byteData
        else:
            size = round((lenByteData.bit_length() + 7) / 8)
            # size2 = (lenByteData.bit_length() + 7) // 8
            return (0xf7 + size).to_bytes(1, 'big') + lenByteData.to_bytes(size, 'big') + byteData
    else:
        pass  # error
