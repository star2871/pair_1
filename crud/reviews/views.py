from django.shortcuts import render, redirect
from .models import Review

# Create your views here.


def index(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/index.html", context)


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    created_at = request.GET.get("created_at")

    Review.objects.create(
        content=content,
        created_at=created_at,
        title=title,
    )

    return redirect("reviews:index")


def detail(request, pk_):
    review = Review.objects.get(pk=pk_)
    context = {
        "review": review,
    }
    return render(request, "reviews/detail.html", context)


def update(request, pk_):
    # update할 특정 데이터를 불러온다. -> pk_ 를 사용해서
    review = Review.objects.get(id=pk_)

    title_ = request.GET.get("title")
    content_ = request.GET.get("content")

    # 데이터를 수정
    review.title = title_
    review.content = content_

    # 데이터를 수정한 것을 반영(save)
    review.save()

    # 데이터의 디테일 페이지로 리다이렉트
    return redirect("reviews:detail", review.pk)


def delete(request, pk):
    # pk에 해당하는 글 삭제
    target = Review.objects.get(id=pk)
    target.delete()
    return redirect("reviews:index")


def new(request):
    return render(request, "reviews/new.html")


def edit(request, pk_):
    # get 메소드를 사용해서 특정 pk 데이터를 불러온다.
    review = Review.objects.get(pk=pk_)
    context = {
        "review": review,
    }

    return render(request, "reviews/edit.html", context)
