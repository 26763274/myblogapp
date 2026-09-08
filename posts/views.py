from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
# 同じフォルダのmodels.pyで定義したPostモデルを読み込む。これでデータベース内の投稿データを操作できるようになる。

from django.db.models import Q

def index(request):
    #return HttpResponse("Hello, world! このページは投稿のインデックスです。")
    posts = Post.objects.order_by('-published')
    # Postのobjectsを持ってくる。
    #.order_by('-published') その投稿を最新のものから順に表示させる。
    #return render(request, 'posts/index.html', {'posts': posts})
    # request:ユーザーから届いたアクセス情報(第１引数)
    # posts/index.html: 表示に使用するHTMLテンプレートファイルを指定(第2引数)
    # {'posts': posts}: index.htmlを読みだすときに、posts変数にデータを持っている状態でテンプレートが呼び出される。(第3引数)

    keyword = request.GET.get('keyword')
    if keyword:
        posts = posts.filter(
            Q(title__icontains=keyword) | Q(body__icontains=keyword)
        )

    context = {
        'posts':posts,
    }
    return render(request, 'posts/index.html', context)

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    
    return redirect(request.META.get('HTTP_REFERER', 'post_detail'))


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_detail.html', {'post':post})
# Create your views here.
