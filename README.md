## RLP
### Ethereum Recursive length prefix serialization <br>

#### example:
```python
import RLP

test1 = 255
test2 = 50000000000
test3 = "0x9a0c98574e305f77d3fabaf4e4f1c7fcbc04f81b"
test4 = [1, 21000, 50000000000, "0x9a0c98574e305f77d3fabaf4e4f1c7fcbc04f81b", 500000, 'this is my data']

print(f"test1 rlp = {RLP.encode(test1)}")
print(f"test2 rlp = {RLP.encode(test2)}")
print(f"test3 rlp = {RLP.encode(test3)}")
print(f"test4 rlp = {RLP.encode(test4)}")
```

#### result:
```text
test1 rlp = b'\x82\x00\xff'
test2 rlp = b'\x85\x0b\xa4;t\x00'
test3 rlp = b'\xaa0x9a0c98574e305f77d3fabaf4e4f1c7fcbc04f81b'
test4 rlp = b'\xf9\x00J\x01\x83\x00R\x08\x85\x0b\xa4;t\x00\xaa0x9a0c98574e305f77d3fabaf4e4f1c7fcbc04f81b\x83\x07\xa1 \x8fthis is my data'
```
