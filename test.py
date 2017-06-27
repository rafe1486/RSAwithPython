'''data = b'abcde'
info = [data[i:i+3] for i in range(0, len(data), 3)]
print (info)'''

msg = '12345'.encode()
intFromBytes = int.from_bytes(msg,byteorder="little")
print(intFromBytes)

byteArray = intFromBytes.to_bytes(intFromBytes.bit_length(), byteorder="little").decode("utf-8")
print(byteArray)
