from csv import DictReader
from glob import glob
path = ".\\Podatki"

files = [f for f in glob(path + "**/*.csv")]

readers = []

for fl in files:
    readers.append(DictReader((x.replace("\0", "") for x in open(fl, "rt", encoding="latin-1")), delimiter=";"))

almamatter = ""
for row in readers[0]:
    almamatter = row
print(almamatter)
print("Ola")
for row in readers[0]:
    almamatter = row
print(almamatter)


"""
fileName = "./Podatki/2014_3.csv"

fl = open(fileName, "r", encoding="latin-1")

if "\0" in open("Podatki/2014_1.csv").read():
    print("OhHeloThere")
    """