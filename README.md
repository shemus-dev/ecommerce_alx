# E-commerce Product API

A robust Django REST Framework (DRF) backend for a modern e-commerce platform. This API manages users, products, and orders with secure authentication and real-time stock management.

## 🚀 Application Features

### 1. User Management & Authentication
*   **Custom User Model**: Extended Django user model for future scalability.
*   **Secure Authentication**: Industry-standard **JWT (JSON Web Token)** implementation.
*   **Registration & Login**: Dedicated endpoints for user onboarding and token generation.

### 2. Product Management (CRUD)
*   **Full Control**: Create, Read, Update, and Delete products (Authenticated users/Admins).
*   **Image Support**: Handle product image uploads and serving.
*   **Stock Tracking**: Dynamic inventory management.

### 3. Advanced Search & Filtering
*   **Search**: Find products rapidly by `Name` or `Category` (e.g., `?search=MacBook`).
*   **Filters**: Drill down by:
    *   **Category**: `?category=Electronics`
    *   **Price Range**: `?min_price=100&max_price=500`
    *   **Availability**: `?in_stock=true`
*   **Pagination**: Optimized performance with paginated results (10 items per page).

### 4. Order System (Transactional)
*   **Place Orders**: Authenticated users can buy items.
*   **Automatic Stock Reduction**: System verifies stock *before* purchase and deducts immediately upon order confirmation.
*   **Order History**: Users can view their personal purchase history.
*   **Nested Architecture**: Orders handle multiple items in a single request.

---

## 🛠️ Setup & Installation

**Prerequisites:** Python 3.8+

1.  **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd ecommerce_alx
    ```

2.  **Create Virtual Environment**:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # Windows
    # source venv/bin/activate  # Mac/Linux
    ```

3.  **Install Dependencies**:
    ```bash
    pip install django djangorestframework djangorestframework-simplejwt django-filter Pillow python-dotenv
    ```

4.  **Database Migration**:
    ```bash
    python manage.py makemigrations users products orders
    python manage.py migrate
    ```

5.  **Create Admin User**:
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run Server**:
    ```bash
    python manage.py runserver
    ```

---

## 🧪 Testing the API

You can test the API using **Postman**, **curl**, or the built-in **Browsable API**.

### Option A: Browser (Recommended for quick testing)
*   **URL**: `http://127.0.0.1:8000/api/`
*   **Login**: Click the "Log in" button (top-right) and use your credentials.
*   **Navigate**: Click on `products` or `orders` to browse and post data via HTML forms.

### Option B: Curl / Postman (Headless)
**1. Register:**
```bash
POST /api/auth/register/
Body: {"username": "john", "email": "john@example.com", "password": "securePass123"}
```
**2. Login (Get Token):**
```bash
POST /api/auth/login/
Body: {"username": "john", "password": "securePass123"}
Response: {"access": "eyJ0eX...", "refresh": "..."}
```
**3. Use Token:**
Add header `Authorization: Bearer <ACCESS_TOKEN>` to all subsequent requests.

### API Endpoints Reference

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| **AUTH** | | | |
| `POST` | `/api/auth/register/` | Create account | No |
| `POST` | `/api/auth/login/` | Get JWT Tokens | No |
| **PRODUCTS** | | | |
| `GET` | `/api/products/` | List/Search/Filter products | No |
| `POST` | `/api/products/` | Add new product | **Yes** |
| `GET` | `/api/products/{id}/` | View product details | No |
| `PATCH` | `/api/products/{id}/` | Update product | **Yes** |
| `DELETE` | `/api/products/{id}/` | Remove product | **Yes** |
| **ORDERS** | | | |
| `GET` | `/api/orders/` | View my orders | **Yes** |
| `POST` | `/api/orders/` | Place new order | **Yes** |

**Order JSON Structure:**
```json
{
    "items": [
        { "product": 1, "quantity": 2 },
        { "product": 3, "quantity": 1 }
    ]
}
```
