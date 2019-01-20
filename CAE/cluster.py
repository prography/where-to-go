from sklearn.cluster import KMeans
import numpy as np
import csv

new_lines=[]
c=0
with open('data/image_db.csv', 'r') as csvfile:
    line_count = len(csvfile.readlines())
    csvreader = csv.reader(csvfile)

    for i,line in enumerate(csvreader):
        if i==0:
            continue
        dir=[]

# # dummy encoding file
# encoder_result = np.random.rand(line_count,50)
# np.save('./encoding.npy', encoder_result)
#
# print(encoder_result.shape[1])
# quit()

# read encoding file
encodings = np.load('./encoding.npy')
# print(encodings.shape)
encodings = encodings[1:]
# print(encodings.shape)
# quit()

# cluster step 1
clustering = KMeans(n_clusters=4).fit(encodings)
# print(clustering.labels_)

new_lines=[]
with open('data/image_db.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    for i,line in enumerate(csvreader):
        if i==0:
            new_lines.append(line)
        else:
            line.append(clustering.labels_[i-1])
            new_lines.append(line)
# print(len(new_lines))
# print(new_lines[0])
# quit()

with open('image_db.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    for line in new_lines:
        csvwriter.writerow(line)


sum=0
# further cluster hierarchically
for cluster_level in range(3,6):
    for cluster_idx in range(4):
        indices = []
        with open('image_db.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for i,line in enumerate(csvreader):
                if int(line[-1])==cluster_idx and len(line)==cluster_level:
                    indices.append(i)

        encodings_partial = []
        for index in indices:
            enco=list(encodings[index])
            encodings_partial.append(enco)
            # print(encodings_partial)
        encodings_partial = np.array(encodings_partial)
        clustering = KMeans(n_clusters=4).fit(encodings_partial)




        c=0

        new_lines=[]
        with open('image_db.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for i,line in enumerate(csvreader):
                if i==0:
                    new_lines.append(line)
                else:
                    if int(line[-1])==cluster_idx and len(line)==cluster_level:
                        line.append(clustering.labels_[c])
                        # print(line)
                        c+=1
                        new_lines.append(line)
                    else:
                        new_lines.append(line)

        with open('image_db.csv', 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            for line in new_lines:
                csvwriter.writerow(line)
