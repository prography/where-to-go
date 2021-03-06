from django.shortcuts import render
from main.models import Landmark, Image



def index_page(request):
    return render(request, 'main/index.html', {})


def select_page(request):
    count = request.GET.get('count')
    selected_img = request.GET.get('selected_img', None)
    msgs=[
    '나의 여행 스타일과 가장 비슷한 사진을 선택해주세요.',
    '가장 인상 깊었던 여행지의 느낌을 선택해주세요.',
    '마지막으로 가장 궁금한 여행지의 사진을 선택해주세요',
    ]
    if count == "1":
        img1 = Image.objects.filter(cluster1=0).order_by('?').first()
        img2 = Image.objects.filter(cluster1=1).order_by('?').first()
        img3 = Image.objects.filter(cluster1=2).order_by('?').first()
        img4 = Image.objects.filter(cluster1=3).order_by('?').first()

        try:
            print(img1.cluster1)
            print(img2.cluster1)
            print(img3.cluster1)
            print(img4.cluster1)
        except:
            pass

        return render(request, 'main/select.html', {'msg':msgs[0],'count': int(count) + 1,
                                                    'img1':img1.url, 'img2':img2.url, 'img3':img3.url, 'img4':img4.url})

    elif count == "2":
        choice = Image.objects.get(url=selected_img)
        cluster1 = choice.cluster1

        img1 = Image.objects.filter(cluster1=cluster1, cluster2=0).order_by('?').first()
        img2 = Image.objects.filter(cluster1=cluster1, cluster2=1).order_by('?').first()
        img3 = Image.objects.filter(cluster1=cluster1, cluster2=2).order_by('?').first()
        img4 = Image.objects.filter(cluster1=cluster1, cluster2=3).order_by('?').first()

        try:
            print(img1.cluster1, img1.cluster2)
            print(img2.cluster1, img2.cluster2)
            print(img3.cluster1, img3.cluster2)
            print(img4.cluster1, img4.cluster2)
        except:
            pass

        return render(request, 'main/select.html', {'msg':msgs[1],'count': int(count) + 1,
                                                    'img1':img1.url, 'img2':img2.url, 'img3':img3.url, 'img4':img4.url, 'first':choice.url})

    elif count == "3":
        first = request.GET.get('first', None)
        first = Image.objects.get(url=first)

        choice = Image.objects.get(url=selected_img)
        cluster1 = choice.cluster1
        cluster2 = choice.cluster2

        img1 = Image.objects.filter(cluster1=cluster1, cluster2=cluster2, cluster3=0).order_by('?').first()
        img2 = Image.objects.filter(cluster1=cluster1, cluster2=cluster2, cluster3=1).order_by('?').first()
        img3 = Image.objects.filter(cluster1=cluster1, cluster2=cluster2, cluster3=2).order_by('?').first()
        img4 = Image.objects.filter(cluster1=cluster1, cluster2=cluster2, cluster3=3).order_by('?').first()

        try:
            print(img1.cluster1, img1.cluster2, img1.cluster3)
            print(img2.cluster1, img2.cluster2, img2.cluster3)
            print(img3.cluster1, img3.cluster2, img3.cluster3)
            print(img4.cluster1, img4.cluster2, img4.cluster3)
        except:
            pass

        return render(request, 'main/select.html', {'msg':msgs[2],'count': int(count) + 1,
                                                    'img1':img1.url, 'img2':img2.url, 'img3':img3.url, 'img4':img4.url, 'prev':choice.url, 'first':first})

    # resultPage
    elif count == "4":
        choice = Image.objects.get(url=selected_img)
        cluster1 = choice.cluster1
        cluster2 = choice.cluster2
        cluster3 = choice.cluster3

        final = list(Image.objects.filter(cluster1=cluster1, cluster2=cluster2, cluster3=cluster3).order_by('?')[:10])

        # 최종 결과
        result = final[0]
        result_land = Landmark.objects.get(id=result.landmark_id)
        result_img = Image.objects.filter(landmark_id=result_land)

        # 비슷한 이미지
        similar_img = []
        cnt = 0
        for image in final:
            if image.landmark == result.landmark:
                continue
            else:
                similar_img.append(image)
                cnt += 1
                if cnt == 3:
                    break

        similar_land = []
        for s in similar_img:
            similar_land.append(Landmark.objects.get(id=s.landmark_id))

        return render(request, 'main/resultPage.html', {'result_img': result_img, 'result_land': result_land,
                                                        'similar_img': similar_img, 'similar_land': similar_land})
