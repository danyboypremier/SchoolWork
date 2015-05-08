# -*- coding: utf-8 -*-

import filecmp
import os

print "TEST DEBUT"

x = 1
while True:
    fileexpected = "expected/%d.json" % x
    fileactual = "%d.json" % x
    if os.path.isfile(fileexpected) or os.path.isfile(fileactual):
        if not filecmp.cmp(fileexpected, fileactual, shallow=False):
            print "%d - False" % x
    else:
        x -= 1
        break
    x += 1

print ""
print "TEST FIN"
print x