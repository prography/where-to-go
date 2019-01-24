from main.models import Landmark, Image
import csv
import codecs

path1 = "landmark_db.csv"
path2 = "image_db.csv"

with codecs.open(path1, encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        _, created = Landmark.objects.get_or_create(
            landmark = row[1],
            country = row[2],
        )

with codecs.open(path2, encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        r4=int(row[4])
        r5=int(row[5])
        r6=int(row[6])
        print(r4, type(r4))
        _, created = Image.objects.get_or_create(
            landmark = Landmark.objects.get(landmark=row[2]),
            url = row[3],
            cluster1 = r4,
            cluster2 = r5,
            cluster3 = r6,
        )
