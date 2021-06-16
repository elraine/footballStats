
from cupParser import CupParser


c = CupParser()

c.present(fileName="../worldcup/2018--russia/cup.txt")
print(c.title)
print(c.groups)