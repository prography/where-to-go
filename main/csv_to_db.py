from main.models import Landmark, Image
import csv

path1 = "../landmark_db.csv"
path2 = "../image_db.csv"


with open(path2) as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = Image.objects.get_or_create(
            landmark = Landmark.objects.get(landmark=row[0]),
            url = row[1],
        )



with open(path1) as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = Landmark.objects.get_or_create(
            landmark = row[1],
            country = row[2],
        )