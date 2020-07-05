import os, re, copy, csv

path = "../1_resized/"
class_path = path + "classes.txt"
dirs = os.listdir( path )

classes = []
temp_class = []
class_file = open(class_path, "r")
for c in class_file.read().splitlines():
    classes.append({"class": c, "qtd": 0})
    temp_class.append({"class": c, "qtd": 0})

regex = re.compile(r'^0.*.txt$')
dirs = list(filter(regex.search, dirs))

image_detail = []
for item in dirs:
    annotation_file = open(path + item, "r")
    file_dict = {"file": int(item.split('.')[0]), "classes": copy.deepcopy(temp_class)}
    for c in annotation_file.read().splitlines():
        classes[int(c.split()[0])]['qtd'] += 1
        file_dict["classes"][int(c.split()[0])]['qtd'] += 1
    image_detail.append(file_dict)

image_detail = sorted(image_detail, key=lambda k: k['file']) 

with open('../info/ssl-dataset.csv', mode='w') as csv_file:
    fieldnames = ['file'] + [k["class"] for k in classes]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for img in image_detail:
        temp_obj = {}
        temp = (img['file'])
        temp_obj["file"] = f'{temp:05d}'
        for o in img['classes']:
            temp_obj[o['class']] = o['qtd']

        writer.writerow(temp_obj)