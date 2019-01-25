from sklearn.cluster import KMeans
import numpy as np
import csv
import codecs

new_lines=[]
c=0
with codecs.open('data/image_db.csv', 'r', 'utf-8') as csvfile:
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
with codecs.open('data/image_db.csv', 'r', 'utf-8') as csvfile:
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

with codecs.open('clustered_image_db.csv', 'w', 'utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    for line in new_lines:
        csvwriter.writerow(line)


sum=0
# further cluster hierarchically
cluster_level=3
for cluster_idx in range(4):
    indices = []
    with codecs.open('clustered_image_db.csv', 'r', 'utf-8') as csvfile:
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
    with codecs.open('clustered_image_db.csv', 'r', 'utf-8') as csvfile:
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

    with codecs.open('clustered_image_db.csv', 'w', 'utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        for line in new_lines:
            csvwriter.writerow(line)

cluster_level=4
for cluster_idx_1 in range(4):
    for cluster_idx_2 in range(4):
        indices = []
        with codecs.open('clustered_image_db.csv', 'r', 'utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for i,line in enumerate(csvreader):
                if int(line[-2])==cluster_idx_1 and int(line[-1])==cluster_idx_2 and len(line)==cluster_level:
                    indices.append(i)

        encodings_partial = []
        for index in indices:
            enco=list(encodings[index])
            encodings_partial.append(enco)
            # print(encodings_partial)
        encodings_partial = np.array(encodings_partial)
        clustering = KMeans(n_clusters=4).fit(encodings_partial)


        # print(list(zip(indices,clustering.labels_)))


        c=0

        new_lines=[]
        with codecs.open('clustered_image_db.csv', 'r', 'utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            for i,line in enumerate(csvreader):
                if i==0:
                    new_lines.append(line)
                else:
                    if int(line[-2])==cluster_idx_1 and int(line[-1])==cluster_idx_2 and len(line)==cluster_level:
                        line.append(clustering.labels_[c])
                        # print(line)
                        c+=1
                        new_lines.append(line)
                    else:
                        new_lines.append(line)
        with codecs.open('clustered_image_db.csv', 'w', 'utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            for line in new_lines:
                csvwriter.writerow(line)
