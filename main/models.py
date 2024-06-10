from django.contrib.sessions.models import Session
from django.db import models


class Movie(models.Model):
    # 영화 제목
    subject = models.CharField(max_length=200)

    # 영화 내용 또는 설명
    content = models.TextField()

    # 각 장르에 대해 True 또는 False를 저장하는 Boolean 필드
    action = models.BooleanField(default=True)  # 액션 장르
    adventure = models.BooleanField(default=False)  # 모험 장르
    comedy = models.BooleanField(default=False)  # 코미디 장르
    drama = models.BooleanField(default=False)  # 드라마 장르
    horror = models.BooleanField(default=False)  # 공포 장르
    fantasy = models.BooleanField(default=False)  # 판타지 장르
    sf = models.BooleanField(default=False)  # SF 장르
    romance = models.BooleanField(default=False)  # 로맨스 장르
    thriller = models.BooleanField(default=False)  # 스릴러 장르
    mystery = models.BooleanField(default=False)  # 미스터리 장르
    animation = models.BooleanField(default=False)  # 애니메이션 장르
    documentary = models.BooleanField(default=False)  # 다큐멘터리 장르
    musical = models.BooleanField(default=False)  # 뮤지컬 장르
    war = models.BooleanField(default=False)  # 전쟁 장르
    western = models.BooleanField(default=False)  # 서부극 장르
    likebool = models.BooleanField(default=False)  # 좋아하는지 ON/OF로 저장
    ytburl = models.CharField(max_length=200, default='kamsx_g2hnI')

    def __str__(self):
        return self.subject
    def get_genres(self):
        genres = []
        genre_fields = [
            ('action', '액션'),
            ('adventure', '모험'),
            ('comedy', '코미디'),
            ('drama', '드라마'),
            ('horror', '공포'),
            ('fantasy', '판타지'),
            ('sf', 'SF'),
            ('romance', '로맨스'),
            ('thriller', '스릴러'),
            ('mystery', '미스터리'),
            ('animation', '애니메이션'),
            ('documentary', '다큐멘터리'),
            ('musical', '뮤지컬'),
            ('war', '전쟁'),
            ('western', '서부극'),
        ]
        for field, genre_name in genre_fields:
            if getattr(self, field):
                genres.append(genre_name)
        return ', '.join(genres)


class Bookmark(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    is_bookmarked = models.BooleanField(default=False)

    def __str__(self):
        return f"Session: {self.session.session_key} - {self.movie.subject} - Bookmarked: {self.is_bookmarked}"
