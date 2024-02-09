from django.shortcuts import render, redirect
from .request import NewsAPI
from django.core.paginator import Paginator
from .models import FavNews

# Create your views here.
def categories(request):
    q = request.GET.get('search')
    if q:
        return redirect('news:search', query=q)
        
    CATEGORIES = ({'category':'business', 'url': 'https://exeedcollege.com/wp-content/uploads/2022/05/Biggest-Business-Trends-in-2022-2-e1651733586811-1024x498.jpg'}, 
                  {'category': 'entertainment', 'url': 'https://thaiindia.net/images/entertainment_industry.jpeg' },
                  {'category': 'general', 'url': 'https://www.sporcle.com/blog/wp-content/uploads/2018/10/1-69.jpg'}, 
                  {'category':'health', 'url': 'https://cms-api-in.myhealthcare.co/image/20220910103120.jpeg'}, 
                  {'category':'science', 'url': 'https://beyondexclamation.com/wp-content/uploads/2020/12/10-1.jpg'},
                  {'category': 'sports', 'url': 'https://www.hindustantimes.com/ht-img/img/2023/08/29/1600x900/pexels_1693295846485_1693295853881.jpg'},
                  {'category':'technology', 'url': 'https://www.simplilearn.com/ice9/free_resources_article_thumb/What_is_the_Importance_of_Technology.jpg'})

    return render(request, 'news/categories.html', context={'categories': CATEGORIES})

def source(request, cat):
    q = request.GET.get('search')
    if q:
        return redirect('news:search', query=q)

    source_list = NewsAPI().get_news_source(cat)
    source_list = list(set(source_list))

    paginate = Paginator(source_list, 20)
    page = request.GET.get('page')
    source_list = paginate.get_page(page)

    return render(request, 'news/sources.html', context={'sources': source_list, 'cat': cat})

def articles(request, cat, src):
    q = request.GET.get('search')
    if q:
        return redirect('news:search', query=q)

    if request.method == 'POST':
        title = request.POST.get('title', '')
        url = request.POST.get('url', '')
        thumbnail = request.POST.get('thumbnail', '')
        desc = request.POST.get('desc', '')
        date = request.POST.get('date', '')

        article = FavNews(title=title, url=url, thumbnail=thumbnail, desc=desc, date=date)
        article.save()

    article_list = NewsAPI().get_news_articles(cat, src)
    
    return render(request, 'news/articles.html', {'articles': article_list})

def search(request,query):
    q = request.GET.get('search')
    if q:
        return redirect('news:search', query=q)
    
    if request.method == 'POST':
        title = request.POST.get('title', '')
        url = request.POST.get('url', '')
        thumbnail = request.POST.get('thumbnail', '')
        desc = request.POST.get('desc', '')
        date = request.POST.get('date', '')

        article = FavNews(title=title, url=url, thumbnail=thumbnail, desc=desc, date=date)
        article.save()
    
    article_list = NewsAPI().search_news(query)
        
    return render(request, 'news/search.html', {'articles' : article_list})

def favorites(request):
    articles = FavNews.objects.all()

    if request.method == "POST":
        id = request.POST.get('delete_fav', '')

        FavNews.objects.get(id=id).delete()

    return render(request, 'news/favorites.html', {'articles': articles})



