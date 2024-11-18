# FastAPI Email Lookup

This project provides a FastAPI server that exposes an endpoint to fetch a person's information based on their email. Additionally, it includes a Python client that interacts with the server to select an email from a list and request information from the API.

## Prerequisites

Before running the project, ensure you have the following installed on your system:

- Python 3.8 or higher
- MySQL database (with the `test_db` database set up)

## Setup

### Env

```shell
python3 -m venv .
source bin/activate
pip install -r requirements.txt
```

### Database

```shell
docker run -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -e MYSQL_ROOT_HOST=% -p 3306:3306 -v mysql_data:/var/lib/mysql --name mysql -d mysql:latest
```

```sql
-- Create the database
CREATE DATABASE test_db;

-- Use the database
USE test_db;

-- Create the table
CREATE TABLE people (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    birth_date DATE NOT NULL,
    phone_number VARCHAR(15)
);

-- Insert dummy data
INSERT INTO people (first_name, last_name, email, birth_date, phone_number) VALUES
('John', 'Doe', 'john.doe@example.com', '1990-01-15', '1234567890'),
('Jane', 'Smith', 'jane.smith@example.com', '1985-07-22', '0987654321'),
('Alice', 'Johnson', 'alice.johnson@example.com', '1993-03-11', '5551234567'),
('Bob', 'Brown', 'bob.brown@example.com', '1978-10-09', '5559876543'),
('Carol', 'Davis', 'carol.davis@example.com', '1995-12-25', '1231231234'),
('David', 'Wilson', 'david.wilson@example.com', '1980-05-30', '4564564567'),
('Eve', 'Taylor', 'eve.taylor@example.com', '1992-04-14', '7897897890'),
('Frank', 'Anderson', 'frank.anderson@example.com', '1988-11-19', '3213213210'),
('Grace', 'Thomas', 'grace.thomas@example.com', '1991-02-20', '6546546543'),
('Henry', 'Moore', 'henry.moore@example.com', '1987-08-08', '9879879876');
```

### Running server

```shell
uvicorn server:app --reload
```
### Running client

```shell
python3 client.py
```

--

# API Endpoints Documentation

This document provides details for the available API endpoints in the `FastAPI Email Lookup` project.

## Base URL

The base URL for all endpoints is: http://127.0.0.1:8000


## Endpoints

### 1. `GET /people`

- **Method**: `GET`
- **Description**: Fetches details of a person by their email address.
- **Request Body**: JSON object with an email address.

#### Request Example:
```json
{
  "email": "someone@example.com"
}
```

#### Response example
```json
{
  "id": 1,
  "first_name": "John",
  "last_name": "Doe",
  "email": "someone@example.com",
  "birth_date": "1990-01-01",
  "phone_number": "1234567890"
}

```

### `GET /emails`

- **Method**: `GET`
- **Description**: Fetches a list of all email addresses from the database.
- **Request Body**: None.
- **Response**: A JSON array containing all the email addresses.

## Request

There is no request body for this endpoint. Simply make a `GET` request to fetch all the emails.

#### Example Request using `curl`:

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/emails'

