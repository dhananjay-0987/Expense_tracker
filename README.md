# Expense Tracker

A simple and efficient Django-based expense tracking application that helps users manage their income and expenses.

## Features

- Track income and expenses
- Real-time balance updates
- Transaction history with descriptions
- Delete transactions
- Visual representation of credits and debits
- Responsive design

## Prerequisites

- Python 3.x
- Django 5.x
- MySQL Database
- XAMPP 
## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/dhananjay-0987/Expense_tracker
   cd Expense_tracker
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django mysqlclient
   ```

4. **Database Setup**
   - Start XAMPP and ensure MySQL service is running
   - Create a new database named 'expense_tracker'
   - Update database settings in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'expense_tracker',
           'USER': 'root',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

5. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## Usage

1. **Adding Transactions**
   - Enter a description for your transaction
   - Input amount (positive for income, negative for expenses)
   - Click "Add transaction"

2. **Viewing Transactions**
   - All transactions are displayed in the history section
   - Green entries indicate income
   - Red entries indicate expenses

3. **Deleting Transactions**
   - Click the trash icon next to any transaction to delete it
   - Balance will automatically update

## Project Structure

```
expense_tracker/
├── tracker/
│   ├── models.py          # Database models
│   ├── views.py           # View logic
│   └── templates/
│       └── index.html     # Main template
├── manage.py
└── requirements.txt
```

## Models

### curr_balance
- Maintains the current balance
- Single instance model with float field

### track_history
- Stores all transactions
- Fields:
  - balance (ForeignKey to curr_balance)
  - amount (FloatField)
  - expense_type (CharField: Credit/Debit)
  - description (TextField)
  - created_at (DateTimeField)
  - updated_at (DateTimeField)

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## Acknowledgments

- Django Documentation
- Bootstrap for styling
- Font Awesome for icons
