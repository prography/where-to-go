from main.models import Landmark, Image
import csv
import codecs

path2 = "image_db.csv"

with codecs.open(path2, encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        # print(r4, type(r4))
        _, created = Image.objects.get_or_create(
            landmark = Landmark.objects.get(landmark=row[2]),
            url = row[3],
            cluster1 = int(row[4]),
            cluster2 = int(row[5]),
            cluster3 = int(row[6]),
        )
