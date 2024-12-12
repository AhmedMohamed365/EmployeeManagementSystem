# Company Management System with JWT Authentication

This project is a simple **RESTful API** built using Django and Django Rest Framework (DRF) to manage **companies**, **departments**, and **employees**. It includes **user creation and management** with **JWT** tokens for authentication and authorization.

## Features

- **RESTful API Endpoints**:
  - **Companies**: List, create, update, delete companies.
  - **Departments**: List, create, update, delete departments.
  - **Employees**: List, create, update, delete employees.
  - **User Management**: User creation, authentication, and role-based access control using JWT tokens.

- **JWT Authentication**:
  - Users can log in using email and password.
  - JWT tokens (access and refresh tokens) are generated for authenticated users.
  - The token is used for subsequent requests to ensure secure access.

- **Signal Handlers**:
  - **Adding a new department** automatically updates the number of employees in the department.
  - **Adding a new company** automatically updates the number of departments in the company.

- **Role-Based Access Control**:
  - **Admin** or **Manager** users can:
    - Add, update, and delete employees.
    - Add new companies and departments.
  - Other users can view data but cannot modify it.

- **Swagger Documentation**:
  - Integrated with **Swagger** for interactive API documentation.

## API Endpoints

### **Authentication Endpoints**

- **Login**: `POST /api/auth/jwt/create/`  
  Request body:  
  ```json
  {
    "email": "user@example.com",
    "password": "password123"
  }

**Company Endpoints**

- List Companies: GET /api/companies/

- Create Company: POST /api/companies/
Request body:
    ```json
    {
        " name": "New Company",
        "description": "A   description of the new company"
    }


**Department Endpoints**
- List Departments: GET /api/departments/

- Create Department: POST /api/departments/



**Examples from swagger**

!![Alt Text](docs/1.png)

!![Alt Text](docs/2.png)


!![Alt Text](docs/3.png)
