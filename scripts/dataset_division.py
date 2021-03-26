import os, re, copy, csv

path = "../annotations/yolo/"
class_path = path + "classes.txt"
dirs = os.listdir( path )

classes = []
temp_class = []
sizes = []
class_file = open(class_path, "r")
for c in class_file.read().splitlines():
    classes.append({"class": c, "qtd": 0, "size":{"small": 0, "medium": 0, "large": 0}})
    temp_class.append({"class": c, "qtd": 0, "size":{"small": 0, "medium": 0, "large": 0}})

regex = re.compile(r'^0.*.txt$')
dirs = list(filter(regex.search, dirs))

image_detail = []
for item in dirs:
    annotation_file = open(path + item, "r")
    file_dict = {"file": int(item.split('.')[0]), "classes": copy.deepcopy(temp_class)}
    for c in annotation_file.read().splitlines():
        classes[int(c.split()[0])]['qtd'] += 1
        file_dict["classes"][int(c.split()[0])]['qtd'] += 1
        w = int(float(c.split()[3]) * 224)
        h = int(float(c.split()[4]) * 224)
        if (h * w) < (32 * 32):
            classes[int(c.split()[0])]['size']['small'] += 1
            file_dict["classes"][int(c.split()[0])]['size']['small'] += 1
        elif (h * w) < (96 * 96):
            classes[int(c.split()[0])]['size']['medium'] += 1
            file_dict["classes"][int(c.split()[0])]['size']['medium'] += 1
        else:
            classes[int(c.split()[0])]['size']['large'] += 1
            file_dict["classes"][int(c.split()[0])]['size']['large'] += 1
    image_detail.append(file_dict)

image_detail = sorted(image_detail, key=lambda k: k['file'])
print(classes)

with open('../info/ssl-dataset.csv', mode='w') as csv_file:
    sizes = ['_small', '_medium', '_large']
    fieldnames = ['file'] + [k["class"] + s for k in classes for s in sizes]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for img in image_detail:
        temp_obj = {}
        temp = (img['file'])
        temp_obj["file"] = f'{temp:05d}'
        for o in img['classes']:
            temp_obj[o['class'] + '_small'] = o['size']['small']
            temp_obj[o['class'] + '_medium'] = o['size']['medium']
            temp_obj[o['class'] + '_large'] = o['size']['large']

        writer.writerow(temp_obj)