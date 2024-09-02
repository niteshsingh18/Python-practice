f = open("poem.txt")
content = f.read()
if("Humpty" in content):
    print("The word 'Humpty' is present")
else:
    print("The word 'Humpty' is not present")

f.close