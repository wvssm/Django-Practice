import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200) #질문, 문자필드
    pub_date = models.DateTimeField('date published') #질문 발행일, 날짜와시간 필드
    #클래스 생성자에 첫번째 위치 인수 전달하여, 사람이 읽기 좋은 이름 지정 가능

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        #현재 이후의 발행된 데이터 리턴
        #오늘 - 어제 

#pub_date 이런 것은 데이터베이스의 컬럼명

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #여기는 하나의 question에 대한 다수의 selection을 가지기 때문에 1대 다라고 생각할 수 있다.


    #Choice가 하나의 Question과 관계된다는 것을 장고에게 알려줌
    #장고는 many to one, one to many, one to one 모든 일반 데이터베이스의 관계들을 지원함
    choice_text = models.CharField(max_length=200) #선택문
    votes = models.IntegerField(default=0) #투표수

    def __str__(self):
        return self.choice_text
