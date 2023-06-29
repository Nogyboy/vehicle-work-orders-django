# SEAUTO Workshop - Work Order Vehicle Management System

SEAUTO Workshop currently relies on an Excel document for managing work orders and tracking. The aim of this project is to develop a Work Order Vehicle Management System that replaces the manual process. The system will allow administrators to streamline work order management while offering clients a comprehensive overview of their vehicle's status and ongoing work, including pictures.

## Features

1. User Authentication

2. Vehicle Management

3. Work Order Management

4. External API Integration(UNSPLASH Images)

5. Django Admin Panel Integration for easy management

## Installation

1. Clone the repository:

```
git clone <repository_url>
cd work-order-vehicle-management-system
```

2. Install the required packages(Requires Python Pipenv):

```
pipenv install
```

3. Apply database migrations:

```
python manage.py migrate
```

4. Start the development server:

```
python manage.py runserver
```

## Project Structure

The project follows a standard Django project structure. Here's an overview of the main directories and files:

```
├── authentication
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── media
│   └── vehicles
│       ├── ABC1234.jpg
│       └── PTX0123.jpg
├── static
├── vehicles
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_vehicle_brand_alter_vehicle_color_and_more.py
│   │   ├── 0003_alter_vehicle_plate.py
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── work_orders_management
│   ├── __init__.py
│   ├── asgi.py


│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── workorders
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   ├── 0001_initial.py
    │   └── __init__.py
    ├── models.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

## Dependencies

The project relies on the following dependencies, which are listed in the `requirements.txt` file:

```plaintext
django==4.2.2
djangorestframework==3.14.0
pillow
requests
python-decouple
icecream
```

## Usage

- Run the development server:

```
python manage.py runserver
```

- Apply database migrations:

```
python manage.py migrate
```

- Create a superuser:

```
python manage.py createsuperuser
```
It can test the API endpoints using Postman. In the root directory of the project, you will find a file named "Vehicle Work Orders.postman_collection"

## License

[MIT](LICENSE)

Feel free to modify and customize this README file according to your project's specific needs.
# Credentials
## Super User
Email:admin@admin.com

Username: admin

Password: admin

## Client User
Email:
Username: christian
Password: Windows8.1