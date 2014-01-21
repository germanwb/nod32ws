__author__ = 'german_or_jane'
x = []
s = ''
h1 = {}
myfile = open("update.ver", "rU") #чтение из файла
for line in myfile.readlines(): #построчно читаем файл и выводим на экран
    if line[0] == '[':
        if s != '':
            h1.update({x:s})
            s == ''
        x = line[1:len(line)-2]
    s=s+line

print(h1['EAV_WINNT64_1058'])