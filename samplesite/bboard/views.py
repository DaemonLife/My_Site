
# * optimal methode
from django.shortcuts import render

from .models import Bb

def index(request):
    bbs = Bb.objects.all()
    return render(request, 'bboard/index.html', {'bbs': bbs})

# *

# from django.http import HttpResponse
# from django.template import loader

# from .models import Bb


# # old methode
# # def index(request):
# #     # сам шаблон
# #     template = loader.get_template('bboard/index.html')
    
# #     # создание словаря объектов из БД, отсортированных по дате
# #     bbs = Bb.objects.order_by('-published')
# #     context = {'bbs': bbs}

# #     # рендеринг: объединения шаблона со словарем объектов
# #     return HttpResponse(template.render(context, request))

# # new methode
# def index(request):
#     # сам шаблон
#     template = loader.get_template('bboard/index.html')
    
#     # создание словаря объектов из БД, отсортированных по дате
#     bbs = Bb.objects.order_by('-published')
#     context = {'bbs': bbs}

#     # рендеринг: объединения шаблона со словарем объектов
#     return HttpResponse(template.render(context, request))

