# FastAPI Text Processing API

## Overview

This project is a simple FastAPI-based application that provides the following functionalities:

- **Heartbeat Endpoint**: Returns a timestamped message.
- **Version Endpoint** Returns the API version.
- **To Upper Endpoint**: Converts input text to uppercase.
- **To Lower Endpoint**: Converts input text to lowercase.

## Prerequisites

Ensure you have **Python 3.8+** installed on your system.

## Installation

1. Clone the repository (if applicable) or copy the `main.py` file into your working directory.
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

## Running the Server

To start the FastAPI server, run the following command:

```bash
uvicorn main:app --reload
```

This will start the server at [**http://127.0.0.1:8000**](http://127.0.0.1:8000).

## API Endpoints

### 1. Heartbeat Endpoint

- **URL:** `GET /heartbeat/{input_text}`
- **Example:**
  ```bash
  curl -X 'GET' 'http://127.0.0.1:8000/heartbeat/HelloWorld' -H 'accept: application/json'
  ```
- **Response:**
  ```json
  {
    "message": "HelloWorld",
    "timestamp": "2025-03-09 14:09:45"
  }
  ```

### 2. Version Endpoint

- **URL:** `GET /version`
- **Example:**
  ```bash
  curl -X 'GET' 'http://127.0.0.1:8000/version' -H 'accept: application/json'
  ```
- **Response:**
  ```json
  {
    "version": "1.0.0"
  }
  ```

### 3. To Upper Endpoint

- **URL:** `POST /to-upper`
- **Example:**
  ```bash
  curl -X 'POST' 'http://127.0.0.1:8000/to-upper' \
       -H 'Content-Type: application/json' \
       -d '{"text": "welcome to world of AI"}'
  ```
- **Response:**
  ```json
  {
    "result": "WELCOME TO WORLD OF AI"
  }
  ```

### 4. To Lower Endpoint

- **URL:** `POST /to-lower`
- **Example:**
  ```bash
  curl -X 'POST' 'http://127.0.0.1:8000/to-lower' \
       -H 'Content-Type: application/json' \
       -d '{"text": "WELCOME TO WORLD OF AI"}'
  ```
- **Response:**
  ```json
  {
    "result": "welcome to world of ai"
  }
  ```

## Testing via Swagger UI

FastAPI provides an interactive documentation UI at:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Screenshots

Below are screenshots showing how to use the API endpoints in Swagger UI:

1. **Heartbeat Request UI** &#x20;
2. **Heartbeat Response** &#x20;
3. **Version Endpoint UI** &#x20;
4. **Version Response** &#x20;
5. **To Upper Request** &#x20;
6. **To Upper Response** &#x20;
7. **To Lower Request** &#x20;
8. **To Lower Response** &#x20;
9. **Swagger API Overview** &#x20;
10. **Successful API Calls** &#x20;

## Stopping the Server

To stop the FastAPI server, press **CTRL + C** in the terminal.

## License

This project is open-source and free to use for learning purposes.

