# views.py
from .trello_api import create_trello_card, get_trello_list_ids
from django.views.decorators.csrf import csrf_exempt
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
        raw_data = request.body.decode('utf-8')

        try:
            data = json.loads(raw_data)
            is_json = True
        except json.JSONDecodeError:
            data = raw_data
            is_json = False

        WebhookData.objects.create(received_data=raw_data)
        trello_card_title = data.get(
            'title', 'New Order') if is_json else "New Order"

        if is_json:
            trello_card_description = (
                f"Order ID: {data.get('order_id', 'N/A')}\n"
                f"Customer Name: {data.get('customer_name', 'N/A')}\n"
                f"Total Amount: {data.get('total_amount', 'N/A')}\n"
                f"Order Status: {data.get('order_status', 'N/A')}"
            )
        else:
            trello_card_description = raw_data

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
