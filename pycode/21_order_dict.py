# -*-encoding:UTF-8 -*-

import collections

#词典有序化
d = {}
d['1'] = 1
d['2'] = 2
d['3'] = 3
d['4'] = 4

for k, v in d.items():
    print k, v

d = collections.OrderedDict()
d['1'] = 1
d['2'] = 2
d['3'] = 3
d['4'] = 4

for k, v in d.items():
    print k, v