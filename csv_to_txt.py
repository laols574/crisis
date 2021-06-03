import csv
import sys

#handles big fields
csv.field_size_limit(sys.maxsize)

save_file = open("stopwords100k.txt", "w")

with open('sw100k.csv', newline='') as csvfile:
	treader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	i = 0
	for row in treader:
		if(i == 0):
			i = 1
			continue
		save_file.write(row[0].replace('"', '').split(",")[0] + "\n")

save_file.close()
