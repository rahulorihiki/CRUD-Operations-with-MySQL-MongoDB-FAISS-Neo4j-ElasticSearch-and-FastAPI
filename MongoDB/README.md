# FastAPI MongoDB CRUD Application

This project demonstrates how to build a CRUD (Create, Read, Update, Delete) API using FastAPI and MongoDB. It includes detailed steps to set up the database, implement CRUD operations, and expose these operations through RESTful APIs.

## Requirements

- Python 3.6+
- MongoDB
- FastAPI
- Uvicorn

## Installation

### MongoDB Setup

1. Download and install MongoDB from [MongoDB's official site](https://www.mongodb.com/try/download/community).
2. Create a MongoDB database and collection:
   ```shell
   mongo
   use mydatabase
   db.createCollection('items')
   ```

# Python Environment Setup

1. Clone this repository and navigate into the project directory.
2. Create a virtual environment and activate it:

python -m venv venv

### For Windows

venv\Scripts\activate

# Install the required packages

pip install fastapi uvicorn pymongo

# Start the FASTAPI server

uvicorn main:app --reload (The API will be available at http://localhost:8000.)

# API Endpoints

## The following endpoints are available:

1. POST /items/: Create a new item.
   {
   "name": "Sample Item",
   "description": "A sample item description",
   "price": 9.99,
   "on_offer": false
   }
2. GET /items/{item_id}: Retrieve an item by its ID.
3. PUT /items/{item_id}: Update an item by its ID.
4. DELETE /items/{item_id}: Delete an item by its ID.

## To test the API endpoints, you can use tools like Postman or curl. Here's an example using curl to create an item:

curl -X POST http://localhost:8000/items/ -H 'Content-Type: application/json' -d '{"name": "Test Item", "price": 10.99}'

### Explanation

This README file provides a thorough overview of your project, instructions for setting up and running the application, details on how to use the API, and guidelines for contributing to the project. This document is intended to be comprehensive, ensuring that anyone who accesses your GitHub repository can understand and interact with your project effectively. Adjust the actual commands and URLs based on your specific project setup and repository details.
