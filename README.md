
# FastAPI MongoDB CRUD Project

This project is a simple API built with FastAPI, using MongoDB as the database. The main goal of the project is to demonstrate how to connect to MongoDB and perform CRUD (Create, Read, Update, Delete) operations.

## Features

- **Create**: Add new interns to the database.
- **Read**: Retrieve all interns.
- **Update**: Update intern information.
- **Delete**: Remove an intern from the database.

## Tech Stack

- **FastAPI**: Python web framework for building APIs.
- **MongoDB**: NoSQL database for storing intern data.
- **Motor**: Async MongoDB driver for Python.
- **Beanie**: ODM (Object-Document Mapper) built on Motor for MongoDB.
- **Pydantic**: Data validation using Python's type annotations.

---

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8+
- MongoDB (can be installed locally or used via a cloud service like MongoDB Atlas)
- [FastAPI](https://fastapi.tiangolo.com/) and related dependencies.

---

## Getting Started

Follow the steps below to set up and run the project.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create and Activate a Virtual Environment

On macOS/Linux:
```bash
python3 -m venv env
source env/bin/activate
```

On Windows:
```bash
python -m venv env
.\env\Scripts\activate
```

### 3. Install Required Dependencies

Install the required dependencies listed in `requirements.txt` by running:

```bash
pip install -r requirements.txt
```

### 4. Set Up MongoDB Connection

1. **Local MongoDB**:
   - Install MongoDB locally or use MongoDB Atlas.
   - Make sure MongoDB is running on `mongodb://localhost:27017/` (default for local MongoDB).

2. **MongoDB Atlas** (if using MongoDB in the cloud):
   - Create an account and set up a MongoDB cluster.
   - Replace the MongoDB connection string in the `.env` file with your MongoDB Atlas connection string.

### 5. Create a `.env` File

Create a `.env` file in the root directory to store environment variables. Add your MongoDB connection URL:

```env
MONGO_URI="mongodb://localhost:27017/intern_db"
```

Or, for MongoDB Atlas:

```env
MONGO_URI="mongodb+srv://<username>:<password>@cluster0.mongodb.net/intern_db?retryWrites=true&w=majority"
```

### 6. Run the FastAPI Application

To start the FastAPI server, run:

```bash
uvicorn app.main:app --reload
```

The API will be accessible at: `http://127.0.0.1:8000`

### 7. Test the API

You can use tools like [Postman](https://www.postman.com/) or [cURL](https://curl.se/) to test the API, or you can use the FastAPI interactive API documentation at `http://127.0.0.1:8000/docs`.

---

## API Endpoints

- **POST /interns/**: Add a new intern.
  - Request Body:
    ```json
    {
      "name": "John Doe",
      "department": "Engineering"
    }
    ```
  - Response:
    ```json
    {
      "name": "John Doe",
      "department": "Engineering"
    }
    ```

- **GET /interns/**: Get all interns.
  - Response:
    ```json
    [
      {
        "name": "John Doe",
        "department": "Engineering"
      },
      {
        "name": "Jane Smith",
        "department": "Marketing"
      }
    ]
    ```

- **PUT /interns/{intern_id}**: Update intern details.
  - Request Body:
    ```json
    {
      "name": "Jane Smith",
      "department": "Marketing"
    }
    ```

- **DELETE /interns/{intern_id}**: Delete an intern by ID.

---

## How to Perform CRUD Operations

### 1. **Create** (Add an Intern)
   - Use the `POST /interns/` endpoint.
   - Provide `name` and `department` in the request body.

### 2. **Read** (Get All Interns)
   - Use the `GET /interns/` endpoint.
   - This returns a list of all interns stored in the MongoDB database.

### 3. **Update** (Modify Intern Details)
   - Use the `PUT /interns/{intern_id}` endpoint.
   - Replace the `intern_id` in the URL with the actual ID of the intern.
   - Provide new `name` and `department` details in the request body.

### 4. **Delete** (Remove an Intern)
   - Use the `DELETE /interns/{intern_id}` endpoint.
   - Replace `intern_id` in the URL with the actual ID of the intern to delete them.

---

## Deployment

If you want to deploy the project, make sure to:

1. Use a production-grade server like **Uvicorn** or **Gunicorn**.
2. Set up a proper environment (e.g., Docker or cloud service providers like AWS, GCP, Heroku, etc.).
3. Ensure MongoDB access from the production environment.

---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more information.

---

## Conclusion

This project demonstrates the basic implementation of a CRUD API using FastAPI and MongoDB. You can extend it by adding more features, implementing user authentication, or deploying it to production.

