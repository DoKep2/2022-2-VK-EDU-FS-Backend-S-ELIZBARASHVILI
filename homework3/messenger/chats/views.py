import json

from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST

from . import chats, Chat


@require_GET
def chat_list(request):
    return JsonResponse({'chats': chats})


@require_GET
def get_chat(request):
    chat_name = request.GET.get('name')
    return JsonResponse({chat_name: list(filter(lambda el: el['name'] == chat_name, chats))})


@require_POST
def create_chat(request):
    body = json.loads(request.body.decode())
    chats.append(body)
    return JsonResponse(body)
