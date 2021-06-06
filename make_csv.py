import csv


f = open("training_text/con_training_text.txt")
f2 = open("training_text/lib_training_text.txt")

f = f.readlines()
f2 = f2.readlines()

f3 = f + f2

new = []
max = 0
for line in f3:
    line = line.split()
    new.append(line[0:25])

new_file = []
for i in range(0, len(new)):
    new_str = ""
    for word in new[i]:
        new_str += word + " "
    new_str += "\n"

    new_file.append(new_str)

with open('train.csv', 'w', newline='') as csvfile:
    fieldnames = ['sentence', 'val']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    for line in f3:
      writer.writerow({"sentence" :line, "val" : 0})
