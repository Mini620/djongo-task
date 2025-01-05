from django.shortcuts import render
from django.http import JsonResponse
from .models import Message
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def submit_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        sender = data.get('sender')
        recipient = data.get('recipient')
        content = data.get('content')

        if sender and recipient and content:
            Message.objects.create(sender=sender, recipient=recipient, content=content)
            return JsonResponse({'status': 'success', 'message': 'Message submitted.'})
        return JsonResponse({'status': 'error', 'message': 'Invalid data.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

def get_messages(request, sender_name):
    if request.method == 'GET':
        messages = Message.objects.filter(sender=sender_name).order_by('-timestamp')[:10]
        message_list = [
            {'recipient': msg.recipient, 'content': msg.content, 'timestamp': msg.timestamp}
            for msg in messages
        ]
        return JsonResponse({'status': 'success', 'messages': message_list})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})
