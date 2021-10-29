import logging
import datetime
from datetime import datetime, date

from django.http import Http404
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required, login_required, user_passes_test
# Create your views here.
from django.contrib.auth.models import User
from .models import GameData

from . import process_input


@login_required
@permission_required('fast_fingers.can_play_game', login_url='/fast_fingers/login/', raise_exception=True)
def type(request):
    if request.user.is_authenticated:
        try:
            user_data = GameData.objects.get(user_id=request.user.id)
            user_input = user_data.user_input
        except Exception as why:
            logging.error(why)
            user_input = ""

        if user_input:
            user_input = user_input.strip()
        return render(request, 'fast_fingers/type.html', {"user_input": user_input})
    else:
        return JsonResponse({}, safe=False)

def login_page(request):
    if not request.user.is_authenticated:
        return render(request, 'fast_fingers/login.html')
    else:
        return redirect("type")

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("type")
        else:
            return redirect("login")
    else:
        return redirect("login")

def logout_user(request):
    logout(request)
    return redirect('login')

@csrf_exempt
def get_user_input(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == "POST":
        user_id = request.user.id
        try:
            record = GameData.objects.get(user_id=user_id)
        except Exception:
            user = User.objects.get(id=request.user.id)
            record = GameData(user_id=user, assinged_input=request.POST.get("assinged_input", ""),
                            user_input=request.POST.get("text", ""), end_time=datetime.now().time())
            record.save()

        record.user_input = request.POST.get("text", "")

        if not record.assinged_input:
            record.assinged_input = request.POST.get("assinged_input", "")
        record.end_time = datetime.now().time()
        record.save()
        serializer = {"data": request.POST}
        return JsonResponse(serializer, safe=False)

@csrf_exempt
def calculate_all_scores(request):
    if request.method == "POST":
        records = GameData.objects.all()
        for record in records:
             score = process_input.calculate_score(record.assinged_input, record.user_input)
             record.score = score
             record.save()

        return JsonResponse(list(records.values()), safe=False)

@user_passes_test(lambda u: u.is_superuser)
def display_score(request):
    records = GameData.objects.all()
    processed_records = []

    for record in records:
        end_time = record.end_time
        start_time = record.start_time
        speed = round((datetime.combine(date.today(), end_time) - datetime.combine(date.today(), start_time)).seconds / 60, 3)
        processed_records.append({"username": record.user_id.username, "score": record.score, "start_time": start_time, "end_time": end_time, "speed": speed})

    return render(request, "fast_fingers/display_score.html", {"records": processed_records})
