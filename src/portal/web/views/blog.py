from django.shortcuts import render

from ..forms.comment_form import CommentForm
from ...data.models.post import Post
from ...data.models.comment import Comment
from ...data.db_context import DATA


def blog_index(request):
    posts = DATA.get_all_posts()
    context = {"posts": posts}
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    posts = DATA.get_posts_by_category(category)
    context = {"category": category, "posts": posts}
    return render(request, "blog_category.html", context)


def blog_detail(request, pk):
    post = DATA.get_post_by_id(pk)
    comments = DATA.get_comments_by_post(post)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()

    context = {"post": post, "comments": comments, "form": form}
    return render(request, "blog_detail.html", context)
