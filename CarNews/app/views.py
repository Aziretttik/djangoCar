from django.shortcuts import render
from .models import News


def news_create_view(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        news = News(title=title, description=description)
        news.save()
    return render(request=request, template_name='app/news_create.html')


def car_create_view(request):

    return render(request=request, template_name='app/car_create.html')




