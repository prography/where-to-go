import csv
import os
import codecs
# # remove duplicates
# lines = []
# with codecs.open('image_db.csv', 'r', 'utf-8') as f:
#     lines = f.readlines()
#
#     seen = set()
#     seen_add = seen.add
#     lines = [x for x in lines if not (x in seen or seen_add(x))]
#
#
# with codecs.open('image_db.csv', 'w', 'utf-8') as f:
#     f.writelines(lines)

# # fix index
# new_lines = []
# c=0
# with codecs.open('image_db.csv', 'r', 'utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#
#     for i,line in enumerate(csvreader):
#         if i==0:
#             new_lines.append(line)
#         else:
#             try:
#                 # idx = int(line[-1][-1])+1
#                 # file = line[-1][:-1]+str(idx)+'.jpg'
#                 # new_line = line[:-1]
#                 # new_line.append(file)
#                 # print(new_line)
#                 if os.path.exists(line[-1]):
#                     new_lines.append(line)
#             except Exception as e:
#                 print(e)
#
#
# with codecs.open('image_db.csv', 'w', 'utf-8') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     for line in new_lines:
#         csvwriter.writerow(line)

dirs = []
with codecs.open('image_db.csv', 'r', 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile)

    for i,line in enumerate(csvreader):
        if i!=0:
            dirs.append(line[-1])
# print(dirs)

files = []
for d in os.listdir('landmark'):
    d_r = 'landmark/' + d
    d = os.path.join('landmark',d)
    for f in os.listdir(d):
        files.append(d_r+'/'+f)
        f = os.path.join(d, f)
# print(files)

# with codecs.open('image_db.csv', 'a', 'utf-8') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     for dir in files:
#         if dir not in dirs:
#             landmark = dir.split('/')[1]
#             line = [landmark, dir]
#             csvwriter.writerow(line)

# print(len(files))
# print(len(dirs))
# files = list(set(files))
# dirs = list(set(dirs))
# print(len(files))
# print(len(dirs))
# for dir in dirs:
#     if dir not in files:
#         print(dir)
