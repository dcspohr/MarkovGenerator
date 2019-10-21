import re
import random

class MChain:
    def __init__(self):
        self.graph_dict = {}
    def add(self, key1, key2):
        if self.graph_dict == {}:
            self.graph_dict['.'] = {key1 : 1}
        if key1 not in self.graph_dict:
            self.graph_dict[key1] = {}
        
        if key2 not in self.graph_dict[key1].keys():
            self.graph_dict[key1][key2] = 1
        else:
            self.graph_dict[key1][key2] += 1

    def run(self, count):
        curr = '.'
        for k in range(count):
            next = random.choices(list(self.graph_dict[curr].keys()), self.graph_dict[curr].values(), k=1)[0]
            print(next, end=" ")
            curr = next
    def print_dict_adj(self):
        for i in a.graph_dict:
            print(i, ':', end='')
            for j in a.graph_dict[i]:
                print(a.graph_dict[i][j], end=" ")
            print()
            

text_in = ""
filename = input("Enter filename: ")
infile = open(filename)
for line in infile:
    text_in += line
infile.close()

string = re.findall(r"[\w']+|[.,!?;]", text_in)
if string[-1]!= '.':
    string.append('.')

a = MChain()
if len(string) == 0:
    print("Invalid String, see readme for details")
else:
    prev = '.'
    for s in string:
        a.add(prev, s)
        prev = s
    iruns = int(input("Enter number of iteration runs: "))
    length = int(input("Enter number of words per iteration run: "))
    for i in range(0, iruns):
        a.run(length)
        print("\n")
