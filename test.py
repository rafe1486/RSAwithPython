data = b'abcde'
info = [data[i:i+3] for i in range(0, len(data), 3)]
print (info)