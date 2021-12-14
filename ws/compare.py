#compare two text files and return lines that don't exist in both.

import sys

input_file1 = sys.argv[1]
input_file2 = sys.argv[2]
output = 'output.txt'

if len(sys.argv) >= 4:
    output = sys.argv[3]

def read_files(filename1, filename2):
    file1 = open(filename1, 'r')
    file2 = open(filename2, 'r')
    lines1 = file1.readlines()
    lines2 = file2.readlines()
    return lines1,lines2

def compare_files(lines1, lines2):
    comp = []
    if len(lines1) >= len(lines2):
        for line in lines1:
            if line not in lines2:
                comp.append(line)
        return comp
    else:
        for line in lines2:
            if line not in lines1:
                comp.append(line)
        return comp

def write_file(comp):
    out = open(output, 'w')
    for line in comp:
        out.write(line)

def lets_go():
    a,b = read_files(input_file1,input_file2)
    comp = compare_files(a,b)
    write_file(comp)
    print('Done, wrote ' + str(len(comp)) + ' lines.')

lets_go()
