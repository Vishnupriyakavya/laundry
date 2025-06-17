# LaundryPro - Laundry Management System

A comprehensive web-based laundry management system built with Django that allows customers to order laundry services and administrators to manage orders efficiently.

## 🚀 Features

### Customer Features
- **User Registration & Authentication**: Secure user accounts with profile management
- **Service Browsing**: View available laundry services with pricing
- **Item Selection**: Browse different clothing items and select services
- **Shopping Cart**: Add, update, and remove items from cart
- **Order Management**: Place orders and track order status
- **Order History**: View past orders and their details

### Admin Features
- **Dashboard**: Comprehensive admin panel for order management
- **Order Tracking**: View and update order status (Pending, Processing, Completed, Delivered)
- **Customer Management**: View customer details and order history
- **Service Management**: Add, edit, and manage laundry services
- **Item Management**: Manage clothing items and their details

## 🛠️ Technology Stack

- **Backend**: Django 5.1.7 (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5.3.0
- **Database**: SQLite (Development), PostgreSQL (Production ready)
- **Additional**: Font Awesome, AOS.js (Animations), Pillow (Image handling)

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd la2
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Load Sample Data
```bash
python manage.py create_sample_data
```

### 8. Run Development Server
```bash
python manage.py runserver
```

### 9. Access the Application
- **Main Application**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
la2/
├── la2/                 # Main project settings
├── accounts/           # User authentication & profiles
├── services/           # Laundry services & items
├── cart/              # Shopping cart functionality
├── orders/            # Order management
├── templates/         # HTML templates
├── static/            # Static files (CSS, JS, images)
├── media/             # User uploaded files
├── manage.py          # Django management script
└── requirements.txt   # Python dependencies
```

## 🗄️ Database Models

### User Management
- **User**: Extended Django User model
- **UserProfile**: Additional user information (phone, address, role)

### Services
- **Service**: Laundry services (wash, dry clean, iron, etc.)
- **Item**: Clothing items (shirts, pants, dresses, etc.)

### Cart System
- **Cart**: User shopping cart
- **CartItem**: Individual items in cart

### Orders
- **Order**: Customer orders with status tracking
- **OrderItem**: Individual items in orders

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Database Configuration
The system uses SQLite by default. For production, update `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 👥 User Roles

### Customer
- Register and login
- Browse services and items
- Add items to cart
- Place orders
- Track order status
- View order history

### Admin
- Access admin panel
- Manage all orders
- Update order status
- View customer details
- Manage services and items
- Generate reports

## 🎨 Customization

### Styling
- Modify `templates/base.html` for global styling
- Update Bootstrap classes for layout changes
- Customize CSS in the `<style>` section

### Adding New Services
1. Go to Admin Panel → Services
2. Add new service with name, type, and price
3. Services will automatically appear in the customer interface

### Adding New Items
1. Go to Admin Panel → Items
2. Add new item with name, type, and description
3. Items will be available for customers to select

## 🚀 Deployment

### Production Settings
1. Set `DEBUG = False` in `settings.py`
2. Configure production database
3. Set up static file serving
4. Configure media file storage
5. Set up HTTPS

### Recommended Hosting
- **Heroku**: Easy deployment with PostgreSQL
- **PythonAnywhere**: Django-friendly hosting
- **DigitalOcean**: VPS with full control
- **AWS**: Scalable cloud hosting

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Contact: info@laundrypro.com

## 🔄 Version History

- **v1.0.0**: Initial release with basic functionality
- Customer registration and authentication
- Service and item management
- Shopping cart functionality
- Order placement and tracking
- Admin panel for order management

---

**Built with ❤️ using Django** 