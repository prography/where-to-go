from django.shortcuts import render
from main.models import Landmark, Image

# Create your views here.


def index_page(request):
    return render(request, 'main/index.html', {})


def select_page(request):
    count = request.GET.get('count')
    selected_img = request.GET.get('selected_img')

    if count == 1:
        img1 = Image.objects.filter(cluster1=1).order_by('?').first()
        img2 = Image.objects.filter(cluster1=2).order_by('?').first()
        img3 = Image.objects.filter(cluster1=3).order_by('?').first()
        img4 = Image.objects.filter(cluster1=4).order_by('?').first()

        return render(request, 'main/select.html', {'count': count + 1,
                                                    'images': [img1.url, img2.url, img3.url, img4.url]})


    elif count == 2:
        choice = Image.objects.filter(url=selected_img)
        cluster1 = choice.cluster1

        img1 = Image.objects.filter(cluster1=cluster1, cluster2=1).order_by('?').first()
        img2 = Image.objects.filter(cluster1=cluster1, cluster2=2).order_by('?').first()
        img3 = Image.objects.filter(cluster1=cluster1, cluster2=3).order_by('?').first()
        img4 = Image.objects.filter(cluster1=cluster1, cluster2=4).order_by('?').first()

        return render(request, 'main/select.html', {'count': count + 1,
                                                    'images': [img1.url, img2.url, img3.url, img4.url]})


    elif count == 3:
        choice = Image.objects.filter(url=selected_img)
        cluster1 = choice.cluster1
        cluster2 = choice.cluster2

        img1 = Image.objects.filter(cluster1=cluster1, cluster2=cluster2).order_by('?').first()
        img2 = Image.objects.filter(cluster1=cluster1, cluster2=cluster2).order_by('?').first()
        img3 = Image.objects.filter(cluster1=cluster1, cluster2=cluster2).order_by('?').first()
        img4 = Image.objects.filter(cluster1=cluster1, cluster2=cluster2).order_by('?').first()

        return render(request, 'main/select.html', {'count': count + 1,
                                                    'images': [img1.url, img2.url, img3.url, img4.url]})

    # 결과
    elif count == 4:
        choice = Image.objects.filter(url=selected_img)
        cluster1 = choice.cluster1
        cluster2 = choice.cluster2
        cluster3 = choice.cluster3

        result = Image.objects.filter(cluster1=cluster1, cluster2=cluster2, cluster3=cluster3).order_by('?')
        landmark = result.first().landmark
        country = Landmark.objects.get(landmark=landmark).country

        # resurl_img 개수만큼 append



        si_img1 = result[1].url
        si_img2 = result[2].url
        si_img3 = result[3].url


        return render(request, 'main/resultPage.html', { })

        # result_img = []
        # simillar_img = []

