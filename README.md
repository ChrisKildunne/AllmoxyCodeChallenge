# AllmoxyCodeChallenge

This Python API application receives webhook calls with order information and creates corresponding tasks on a specified Trello board

## Features

- Receives webhook calls containing order information.
- Processes and stores the received data in a Django model
- Creates corresponding tasks on a trello board based on the order information

##Setup and Installation

- Python3
- Django
  - 'requests' library
  - 'python-dotenv' library

### Installation Steps

1. **Install Required Packages**

- pip3 install django requests python-dotenv

2. **Database Migrations**

- python3 manage.py makemigrations
- python3 manage.py migrate

3. **Run the Development Server**

- python3 manage.py runserver

## Usage

### Sending a Webhook

Send a POST request to the webhook endpoint with order data:

Certainly! Below is a comprehensive README.md file for your Python API application, structured according to the project overview and specifications you've provided:

markdown
Copy code

# Python API Application for Webhook Handling and Task Creation

## Project Overview

This application is designed to receive webhook calls and create corresponding tasks in a project management tool, such as Trello. It processes incoming webhook data containing order information and utilizes the Trello API to create tasks based on this data.

### Objective

- Develop a Python API application to receive webhook calls.
- Create tasks in a project management tool based on the data received from webhooks.

### Integration Flow

1. API is triggered by an incoming webhook.
2. The API processes the received data.
3. A task is created in the project management tool (Trello).

## Key Features

### Webhook Integration

- Receives and handles incoming webhooks containing order information.

### Data Manipulation

- Extracts relevant data from the webhook payload.
- Transforms data as needed for the project management tool.

### Project Management Tool Integration

- Interacts with the Trello API to create tasks.

## Technical Specifications

### Programming Language

- Python

### Frameworks/Libraries

- Django
- Requests
- Python-dotenv

### Webhook Handling

- Implements a secure endpoint to receive and process incoming webhooks.

### Data Manipulation

- Develops functions to extract and manipulate data.

### API Authentication

- Uses environment variables for secure API key and token storage.
- Implements secure authentication mechanisms.

### Project Management Tool Integration

- Utilizes the Trello API for task creation.

## Setup and Installation

### Prerequisites

- Python 3.x
- Django
- `requests` library
- `python-dotenv` library

### Installation Steps

1. **Install Required Packages**
   pip install django requests python-dotenv

markdown
Copy code

2. **Set Up Environment Variables**

- Create a `.env` file in the root of your project.
- Add your Trello API key and token:
  ```
  API_KEY=your_trello_api_key
  TOKEN=your_trello_token
  ```

3. **Database Migrations**
   python manage.py makemigrations
   python manage.py migrate

markdown
Copy code

4. **Run the Development Server**
   python manage.py runserver

css
Copy code

## Usage

### Sending a Webhook

Send a POST request to the webhook endpoint with order data:

curl -X POST http://localhost:8000/receiver_path/
-H "Content-Type: application/json"
-d '{"order_id": "12345", "customer_name": "John Doe", "total_amount": "99.99", "order_status": "Processing"}'

### Verifying the Results

- **Django Admin:** Check the `WebhookData` model for received data.
- **Trello Board:** Verify the creation of the task with the received order information. This is the link to my public trello board the information is being sent to https://trello.com/b/Vfa4GNIB/allmoxy.
