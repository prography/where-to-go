import csv
import os

# # remove duplicates
# lines = []
# with open('image_db.csv', 'r') as f:
#     lines = f.readlines()
#
#     seen = set()
#     seen_add = seen.add
#     lines = [x for x in lines if not (x in seen or seen_add(x))]
#
#
# with open('image_db.csv', 'w') as f:
#     f.writelines(lines)
# quit()


# # fix index
# new_lines = []
# c=0
# with open('image_db.csv', 'r') as csvfile:
#     csvreader = csv.reader(csvfile)
#
#     for i,line in enumerate(csvreader):
#         if i==0:
#             new_lines.append(line)
#         else:
#             try:
#                 idx = int(line[-1][-1])+1
#                 file = line[-1][:-1]+str(idx)+'.jpg'
#                 new_line = line[:-1]
#                 new_line.append(file)
#                 # print(new_line)
#                 new_lines.append(new_line)
#                 # if os.path.exists(new_line[-1]):
#                 #     print(new_line[-1])
#
#
#             except Exception as e:
#                 print(e)
#
#
# with open('image_db.csv', 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     for line in new_lines:
#         csvwriter.writerow(line)
#
# quit()
