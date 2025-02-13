# 3-6. Initials

name = "Langli Tieu"

print(name[0] + "." + name[-4])

# bonus way if you know about .split()
name = name.split(' ')
print(name[0][0] + "." + name[1][0])