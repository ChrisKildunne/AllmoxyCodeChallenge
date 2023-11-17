# views.py
from .trello_api import create_trello_card, get_trello_list_ids
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from .models import WebhookData
import json
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('API_KEY')
TOKEN = os.getenv('TOKEN')


@csrf_exempt  # Temporarily disable CSRF for testing purposes
def webhook(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        WebhookData.objects.create(received_data=data,
                                   order_id=data.get('order_id'),
                                   customer_name=data.get('customer_name'),
                                   total_amount=data.get('total_amount'),
                                   order_status=data.get('order_status'))

        trello_card_title = data.get('title', 'New Order')

        trello_card_description = (
            f"Order ID: {data.get('order_id')}\n"
            f"Customer Name: {data.get('customer_name')}\n"
            f"Total Amount: {data.get('total_amount')}\n"
            f"Order Status: {data.get('order_status')}"
        )

        board_id = 'Vfa4GNIB'
        list_ids = get_trello_list_ids(board_id, API_KEY, TOKEN)

        list_name = 'Allmoxy'
        list_id = list_ids.get(list_name)

        if not list_id:
            return JsonResponse({'error': 'List not found'}, status=404)

        trello_response = create_trello_card(
            trello_card_title, list_id, API_KEY, TOKEN, card_description=trello_card_description)

        return JsonResponse({'status': 'success', 'message': 'Data processed successfully', 'trello_response': trello_response})

    return JsonResponse({'error': 'Invalid request'}, status=400)
