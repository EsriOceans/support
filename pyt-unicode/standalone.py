# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from codecs import open

strings = [
    "as string: 票西表島構内評豹掛川日本迎票府怖扶敷".encode("utf-8", "replace"),
    "helló wörld".encode("utf-8"),
    "touché, un café".encode("utf-8"),
]

with open('trials/write.log', 'w') as f:
    for entry in strings:
        f.write(entry)
        f.write("\n")
        print(entry)
