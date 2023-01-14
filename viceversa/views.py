from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['usertext']
    count = len(user_text.split())
    reversed_text = user_text[::-1]
    info = {'usertext':user_text,'reversedtext':reversed_text,'words':count}
    return render(request, 'reverse.html',info)