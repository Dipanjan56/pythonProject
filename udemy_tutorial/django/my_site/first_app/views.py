from django.http import *
from django.shortcuts import render
from django.urls import reverse

articles = {'sports': 'SPORTS PAGE', 'finance': 'FINANCE PAGE', 'politics': 'POLITICS PAGE'}


def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        result = 'NO PAGE FOR THAT TOPIC!'
        raise Http404('404 generic error!')  # later we connect this to 404 http template
        # return HttpResponseNotFound(result)


def add_view(request, num1, num2):
    return HttpResponse(f'{num1} + {num2} = {str(num1 + num2)}')


"""Redirection of page : 
example:/first_app/0 ---> /first_app/sports
        /first_app/1 ---> /first_app/finance
"""


def num_page_view(request, num_page):
    topic_list = list(articles.keys())
    topic = topic_list[num_page]

    return HttpResponseRedirect(reverse('topic-page', args=[topic]))
