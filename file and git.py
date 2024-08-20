filename = 'calc.txt'

with open('calc.txt') as file:
    task = file.readlines()


string = ''
for f in task:
    string += f.strip()
res = eval(string)
print(res)

with open(filename, mode='a') as file:
    file.write(f' = {res}')