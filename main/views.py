from django.shortcuts import render
from .models import Movie


# Create your views here.

def bookmark(request):
    return render(request, 'main/bookmark.html')


def info(request):
    movies = Movie.objects.all()
    return render(request, 'main/info.html', {'movies': movies})


def recommend(request):
    filtered_movies = None  # 처음에는 아무 영화도 필터링하지 않음
    no_movies_message = None  # 일치하는 영화가 없을 경우 메시지를 저장할 변수

    if request.method == 'POST':
        # POST 요청에서 선택된 장르를 받아옴
        selected_genres = request.POST.getlist('genres')
        if selected_genres:
            # 선택된 장르에 해당하는 영화들을 필터링
            filtered_movies = Movie.objects.filter(
                **{genre: True for genre in selected_genres if hasattr(Movie, genre)}
            )
            # 필터링된 영화가 없는 경우
            if not filtered_movies:
                no_movies_message = "일치하는 영화가 없습니다."
        else:
            no_movies_message = "Checkbox를 선택하세요."

    return render(request, 'main/recommend.html', {'movies': filtered_movies, 'no_movies_message': no_movies_message})


def homelands(request):
    return render(request, 'main/homelands.html')


def test(request):
    return render(request, 'main/test.html')
