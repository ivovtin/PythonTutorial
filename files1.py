inp = open('input.txt', 'r')
out = open('output.txt', 'w')
s = inp.read()
print(s)
out.write(s)
inp.close()
out.close()
