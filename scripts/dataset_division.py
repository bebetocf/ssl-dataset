import os, re, copy

path = "../1_resized/"
class_path = path + "classes.txt"
dirs = os.listdir( path )

classes = []
temp_class = []
class_file = open(class_path, "r")
for c in class_file.read().splitlines():
    classes.append({"class": c, "qtd": 0})
    temp_class.append({"class": c, "qtd": 0})
# print (classes[0])

regex = re.compile(r'^0.*.txt$')
dirs = list(filter(regex.search, dirs))
# print (len(dirs))

image_detail = []
for item in dirs:
    annotation_file = open(path + item, "r")
    file_dict = {"file": item, "classes": copy.deepcopy(temp_class)}
    for c in annotation_file.read().splitlines():
        classes[int(c.split()[0])]['qtd'] += 1
        file_dict["classes"][int(c.split()[0])]['qtd'] += 1
    image_detail.append(file_dict)

print (image_detail[1])
print (classes)