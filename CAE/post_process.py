import csv
import codecs
import pandas as pd

landmark_map={}
with codecs.open('data/landmark_db.csv', 'r', 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for i,line in enumerate(csvreader):
        if i==0:
            continue
        else:
            landmark_map[line[1]]=line[2]

# print(landmark_map.values())
# quit()
# line_count=0
# distinct_landmark_names=[]
# with codecs.open('result/landmark_db.csv', 'w', 'utf-8') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     with codecs.open('clustered_image_db.csv', 'r', 'utf-8') as csvfile:
#         csvreader = csv.reader(csvfile)
#         for i,line in enumerate(csvreader):
#             if i==0:
#                 csvwriter.writerow(['id','landmark_name','country'])
#             else:
#                 if line[0] in distinct_landmark_names:
#                     continue
#                 else:
#                     distinct_landmark_names.append(line[0])
#                     try:
#                         row=[line_count,line[0],landmark_map[line[0]]]
#                         line_count+=1
#                         csvwriter.writerow(row)
#                     except:
#                         # print(line[0])
#                         row=[line_count,line[0]]
#                         line_count+=1
#                         csvwriter.writerow(row)

landmark_df = pd.read_csv('result/landmark_db.csv', encoding='utf8', usecols = ['id', 'landmark_name'])
# print(landmark_df[landmark_df['landmark_name']=='Altes Tramdepot']['id'].iloc[0])

new_lines=[]
with codecs.open('clustered_image_db.csv', 'r', 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for i,line in enumerate(csvreader):
        if i==0:
            new_lines.append(['id','landmark_id','landmark_name','image_url','cluster1','cluster2','cluster3'])
        else:
            landmark_idx = landmark_df[landmark_df['landmark_name']==line[0]]['id'].iloc[0]
            new_line = [i-1,landmark_idx] + line
            new_lines.append(new_line)


with codecs.open('../image_db.csv', 'w', 'utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    for line in new_lines:
        csvwriter.writerow(line)
