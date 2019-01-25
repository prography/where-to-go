from main.models import Landmark, Image
import csv
import codecs

path1 = "landmark_db.csv"

with codecs.open(path1, encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        _, created = Landmark.objects.get_or_create(
            landmark = row[1],
            country = row[2],
        )
