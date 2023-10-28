# ECommerce Product Management API

This project is a simple CRUD (Create, Read, Update, Delete) API for managing products in an ECommerce shopping website. It's built using Python, Django, Django Rest Framework, and MySQL.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Documentation](#documentation)
- [Dockerization (Optional)](#dockerization-optional)
- [Fixtures (Optional)](#fixtures-optional)
- [Caching (Optional)](#caching-optional)
- [Deployment on PythonAnywhere](#deployment-on-pythonanywhere)
- [HTTPS Configuration (Optional)](#https-configuration-optional)
- [Contributing](#contributing)
- [License](#license)

## Features

- Create, Read, Update, and Delete product records.
- Store product data in a MySQL database.
- API documentation available.
- Optional Docker containerization.
- Option to prepopulate the database with base data (fixtures).
- Optional caching for improved performance.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/lodhi5580/curd_project.git
   
   
   


1. Install the project dependencies:
     pip install -r requirements.txt
   
2. Apply the database migrations:
    python manage.py makemigrations
    python manage.py migrate

Usage:
1. Start the development server:
   python manage.py runserver
2.Access the API at http://localhost:8000/ in your web browser.

API Endpoints
List all products: GET /api/products/
Create a new product: POST /api/products/
Retrieve a specific product: GET /api/products/{id}/
Update a product: PUT /api/products/{id}/
Delete a product: DELETE /api/products/{id}/
For detailed documentation, visit the API Documentation section.

Documentation
API documentation is available at /api/docs/. You can explore the endpoints, make requests, and view responses interactively.
