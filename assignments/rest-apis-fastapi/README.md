# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build efficient, modern REST APIs using the FastAPI framework. You'll create endpoints, handle requests and responses, implement data validation, and understand best practices for API design.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a FastAPI application with basic endpoints to understand the framework structure and routing.

#### Requirements
Completed program should:

- Import and initialize a FastAPI application instance.
- Create a root endpoint (`/`) that returns a welcome message.
- Create a simple GET endpoint that accepts a name parameter and returns a personalized greeting.
- Example usage:
  ```
  GET / → {"message": "Welcome to FastAPI"}
  GET /greet?name=Alice → {"message": "Hello, Alice!"}
  ```

### 🛠️ Build CRUD Operations with Data Models

#### Description
Implement a simple in-memory data store with Create, Read, Update, and Delete operations using Pydantic models for validation.

#### Requirements
Completed program should:

- Define a Pydantic model for a resource (e.g., `Item`, `User`, `Product`).
- Create a POST endpoint to create new resources.
- Create a GET endpoint to retrieve all resources and another to get a single resource by ID.
- Create a PUT endpoint to update an existing resource.
- Create a DELETE endpoint to remove a resource.
- Validate input data using the Pydantic model.
- Return appropriate HTTP status codes (200, 201, 404, etc.).

### 🛠️ Handle Errors and Add Path Parameters

#### Description
Implement proper error handling and use path parameters to create more dynamic endpoints.

#### Requirements
Completed program should:

- Use path parameters (e.g., `/items/{item_id}`) to access individual resources.
- Return a 404 error when a resource is not found.
- Validate that path parameters are of the correct type (e.g., integer IDs).
- Return meaningful error messages in JSON format.
- Example error response:
  ```json
  {"detail": "Item with ID 99 not found"}
  ```
