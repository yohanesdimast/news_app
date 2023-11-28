from django.shortcuts import render
from .request import NewsAPI
from django.core.paginator import Paginator

# Create your views here.
def categories(request):
    CATEGORIES = ('business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology')

    return render(request, 'news/categories.html', context={'categories': CATEGORIES})

def source(request, cat):
    news = NewsAPI(cat)

    page = request.GET.get('page')
    
    source_list = news.get_news_source(page)[0]
    total_source = news.get_news_source(page)[1]
    
    paginate = Paginator(source_list, 20)
    source_list = paginate.get_page(page)

    if page == None or page == 0:
        page = 1
    # print(page)
    next_page = int(page) + 1
    prev_page = int(page) - 1
    
    if (int(total_source) / (20*int(page)) > 1):
        has_next = True
    else:
        has_next = False
    if int(page) == 1 :
        has_prev = False
    else:
        has_prev = True


    return render(request, 'news/sources.html', 
                  context={'sources': source_list, 
                           'page_now': page,
                           'next_page': str(next_page),
                           'prev_page' : str(prev_page),
                           'has_next' : has_next,
                           'has_prev': has_prev})
