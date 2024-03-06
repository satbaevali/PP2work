import os
import json
massiv = [1, 5, 5, 4]
massiv_j = json.dumps(massiv)
x = open("for_5.txt", 'a')
x.write(massiv_j)
x.close()