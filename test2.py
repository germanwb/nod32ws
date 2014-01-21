__author__ = 'german_or_jane'
#in_file = open('update.ver','r')
#big_list = []
#i = -1
#for line in in_file:
#    if line.startswith('['):
#        big_list.append([])
#        i += 1
#    else:
#        big_list[i].append(line.strip())
#print(big_list{Expire})

def parse(name):
    f = open(name)
    myclasses={}
    classes = {}
    current_class = None
    for line in f.readlines():
        if line.startswith('['):
            current_class = line.strip('[]\n')
            classes[current_class] = []
        else:
            classes[current_class].append(line.rstrip())

    f.close()
    for key in classes.keys():
        param={}
        for element in classes[key]:
            n = element.split('=')
            if len(n) == 2:
                param.update({n[0]:n[1]})
        myclasses[key]=param


    return myclasses
current_ver=parse('nod_update/update.ver')
new_ver=parse('update.ver')

print(new_ver)

