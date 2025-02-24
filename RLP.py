from typing import Union


def to_bytes(_data: Union[int, str]) -> bytes:
    if isinstance(_data, str):
        return _data.encode(encoding='utf-8')
    elif isinstance(_data, int):
        size = round((_data.bit_length() + 7) / 8)
        # size2 = (data.bit_length() + 7) // 8
        return _data.to_bytes(size, 'big')
    else:
        pass  # error


def encode(data: Union[int, str, list]) -> bytes:
    if isinstance(data, int) or isinstance(data, str):
        __byte_data = to_bytes(data)
        __len_byte_data = len(__byte_data)
        if __len_byte_data == 1 and ord(__byte_data) <= 0x7f:
            return __byte_data
        elif __len_byte_data <= 55:
            return (0x80 + __len_byte_data).to_bytes(1, 'big') + __byte_data
        else:
            size = round((__len_byte_data.bit_length() + 7) / 8)
            # size2 = (__len_byte_data.bit_length() + 7) // 8
            return (0xb7 + size).to_bytes(1, 'big') + __len_byte_data.to_bytes(size, 'big') + __byte_data
    elif isinstance(data, list):
        __byte_data = b''
        for val in data:
            __byte_data += encode(val)
        __len_byte_data = len(__byte_data)
        if __len_byte_data <= 55:
            return (0xc0 + __len_byte_data).to_bytes(1, 'big') + __byte_data
        else:
            size = round((__len_byte_data.bit_length() + 7) / 8)
            # size2 = (lenByteData.bit_length() + 7) // 8
            return (0xf7 + size).to_bytes(1, 'big') + __len_byte_data.to_bytes(size, 'big') + __byte_data
    else:
        pass  # error
