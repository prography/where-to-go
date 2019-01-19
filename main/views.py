from django.shortcuts import render
from main.models import Landmark, Image

# Create your views here.

def index_page(request):
    return render(request, 'main/index.html', {})

def select(request):
    count = request.GET.get('count')
    selected_img = request.GET.get('selected_img')

    if count == 1:
        img1 = Image.objects.filter(cluster1=0).order_by('?').first()
        img2 = Image.objects.filter(cluster1=1).order_by('?').first()
        img3 = Image.objects.filter(cluster1=2).order_by('?').first()
        img4 = Image.objects.filter(cluster1=3).order_by('?').first()
        return render(request, 'main/select.html', {'count': count + 1, 'image': [img1, img2, img3, img4]})

    elif count == 2:
        choice = Image.objects.filter(url=selected_img)
        img1 = Image.objects.filter(cluster1=choice.cluster1).filter(cluster2=0).order_by('?').first()
        img2 = Image.objects.filter(cluster1=choice.cluster1).filter(cluster2=1).order_by('?').first()
        img3 = Image.objects.filter(cluster1=choice.cluster1).filter(cluster2=2).order_by('?').first()
        img4 = Image.objects.filter(cluster1=choice.cluster1).filter(cluster2=3).order_by('?').first()
        return render(request, 'main/select.html', {'count': count + 1, 'image': [img1, img2, img3, img4]})

    elif count == 3:
        choice = Image.objects.filter(url=selected_img)
        img1 = Image.objects.filter(cluster2=choice.cluster2).filter(cluster3=0).order_by('?').first()
        img2 = Image.objects.filter(cluster2=choice.cluster2).filter(cluster3=1).order_by('?').first()
        img3 = Image.objects.filter(cluster2=choice.cluster2).filter(cluster3=2).order_by('?').first()
        img4 = Image.objects.filter(cluster2=choice.cluster2).filter(cluster3=3).order_by('?').first()
        return render(request, 'main/result.html', {})

