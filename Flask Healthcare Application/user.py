# user.py

class User:
    def __init__(self, age, gender, income, expenses):
        self.age = age
        self.gender = gender
        self.income = income
        self.expenses = expenses

    def to_dict(self):
        """Flatten the user data for CSV export."""
        data = {
            "Age": self.age,
            "Gender": self.gender,
            "Income": self.income,
        }

        # Add expense categories (default to 0.0 if missing)
        for category in ['utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']:
            data[category.capitalize()] = self.expenses.get(category, 0.0)
        
        return data