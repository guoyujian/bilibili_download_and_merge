import re

'''
专门用来做测试的模块
'''
p = re.compile(r"\d+\.blv$")
L = ["1.blv", "1.blv.sum"]
for item in L:
    if p.match(item):
        print(item)
