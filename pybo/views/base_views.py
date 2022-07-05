from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Q, Count
from ..models import Question, Answer, Comment, QuestionCount
from ..forms import QuestionForm, AnswerForm, CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date, datetime, timedelta
import requests
import socket


# Create your views here.

def index(request):
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')
    so = request.GET.get('so','recent') #정렬기준

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:  # recent
        question_list = Question.objects.order_by('-create_date')
        
    #검색
    
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력

    """
    question = get_object_or_404(Question, pk=question_id)
    #ip = socket.gethostbyname(socket.gethostname()) #docker ip
    ip = get_client_ip(request)
    #requests 모듈과 jsonip.com을 이용한 접속ip알아내기 # 공유기 ip
    #r= requests.get(r'http://jsonip.com')
    #ip = r.json()['ip']
   
    context = {'question': question, 'ip' : ip}
    
    response= render(request, 'pybo/question_detail.html', context)

    # 조회수 기능(쿠키이용)
    expire_date, now = datetime.now(), datetime.now()
    expire_date += timedelta(days=1)
    expire_date = expire_date.replace(hour=0, minute=0, second=0, microsecond=0)
    expire_date -=now
    max_age = expire_date.total_seconds()

    cookie_value = request.COOKIES.get('hitboard','_')

    if f'_{question_id}_' not in  cookie_value:
        cookie_value += f'{question_id}_'
        response.set_cookie('hitboard', value=cookie_value, max_age=max_age,  httponly=True)
        question.view_count +=1
        question.save()
    return response

#ip 체크 
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

