# AllmoxyCodeChallenge

This Python API application receives webhook calls with order information and creates corresponding tasks on a specified Trello board

## Features

- Receives webhook calls containing order information.
- Processes and stores the received data in a Django model
- Creates corresponding tasks on a trello board based on the order information

## Requirements

- Python3
- Django
  - 'requests' library
  - 'python-dotenv' library

### Installation Steps

1. **Install Required Packages**

- pip3 install django requests python-dotenv

2.  **Create a .env**

- Create a .env file in the root of the project with your api key and api token formatted as such:
  API_KEY=your_api_key
  TOKEN=your_api_token

3. **Database Migrations**

- python3 manage.py makemigrations
- python3 manage.py migrate

4. **Run the Development Server**

- python3 manage.py runserver

## Usage

### Sending a Webhook

Send a POST request to the webhook endpoint with order data:

curl -X POST http://localhost:8000/receiver_path/
-H "Content-Type: application/json"
-d '{"order_id": "12345", "customer_name": "John Doe", "total_amount": "99.99", "order_status": "Processing"}'

- If the POST request is formatted differently it will be sent as a string

### Verifying the Results

- **Django Admin:** Check the `WebhookData` model for received data.
- **Trello Board:** Verify the creation of the task with the received order information. This is the link to my public trello board the information is being sent to https://trello.com/b/Vfa4GNIB/allmoxy.
- If a user would like to send data to a different trello board the board_id and name would have to be changed.
