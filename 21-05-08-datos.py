file=open("datos.txt", "r", encoding="UTF-8")

content=file.read(7)
print(content)

file.seek(8)
print(file.read())
#lines=file.readlines()
#print(lines)

file.close()