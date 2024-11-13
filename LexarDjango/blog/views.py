from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post


# Create your views here.
def post_list(request):
    per_page = request.GET.get('per_page') or 2
    # получаем все посты
    posts = Post.objects.all().order_by('id') or per_page

    # создаем пагинатор
    paginator = Paginator(posts,  per_page)  # 10 постов на странице

    # получаем номер страницы, на которую переходит пользователь
    page_number = request.GET.get('page')
    try:
        # получаем посты для текущей страницы
        page_posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_posts = paginator.page(1)
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)

    # передаем контекст в шаблон
    return render(request,
                  'post_list.html',
                  {'page_posts': page_posts})
