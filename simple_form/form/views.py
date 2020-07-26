from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Message
from django.http import JsonResponse
from .forms import MessageForm


def index(request):
    messages = Message.objects.all()
    form = MessageForm()
    context = {
        'messages':messages,
        'form': form
    }

    return render(request, 'basic_form.html', context)

def modal(request):
    form = MessageForm()
    context = {
        'form': form
    }

    return render(request, 'form.html', context)

def save(request):
    print("----------saving-----------")
    form = MessageForm()

    if request.is_ajax():
        print("----------request.is_ajax-----------")
        form = MessageForm(request.POST, None)
        if form.is_valid():
            print("----------form valid-----------")
            form.save()

            return JsonResponse({
                'msg': 'Success'
            })

        form = MessageForm(request.POST)

    return render(request, 'basic_form.html')
    