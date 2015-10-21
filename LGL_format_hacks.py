fin = open("MontereyBay_expanded.txt",'r')
with open("MontereyBay_expanded2.txt", 'a') as fout:
    for line in fin:
        line_new = line.replace('[', '').replace(']','')
        fout.write(line_new)
