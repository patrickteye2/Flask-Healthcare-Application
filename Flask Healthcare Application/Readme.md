# Flask Healthcare Application

A simple web application for collecting and analyzing healthcare-related spending data using Flask and MongoDB. Users can submit their age, gender, income, and expenses in various categories. The data is stored in MongoDB and can be exported for further analysis.

## Features

- User-friendly web survey for healthcare spending
- Stores responses in MongoDB Atlas
- Exports data to CSV for analysis
- Jupyter notebook for data visualization and statistics

## Project Structure

```
Flask Healthcare Application/ │ 
├── app.py # Main Flask application 
├── process_data.py # Script to export MongoDB data to CSV 
├── user.py # User data model for export
├── analysis.ipynb # Jupyter notebook for data analysis 
├── templates/ │ 
    └── index.html # HTML template for the survey form 
└── Readme.md # Project documentation
```


## Setup Instructions

### Prerequisites

- Python 3.12+
- pip (Python package manager)
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) account

### Installation

1. **Clone the repository**

   ```sh
   git clone https://github.com/patrickteye2/Flask-Healthcare-Application.git
   cd "Flask Healthcare Application"
   ```

2. **Install Dependencies**

    ``` sh
    pip install flask pymongo
    ```

3. **Configure MongoDB**

    - The MongoDB connection URI is set in app.py and process_data.py.
    - Update the uri variable if you use your own MongoDB Atlas cluster.

4. **Run the Flask app**
    ``` sh
    python app.py
    ```

    The app will be available at http://127.0.0.1:5000.


## Usage
1. Open the app in your browser.

2. Fill out the survey form with your age, gender, income, and expenses.

3. Submit the form. Your data will be stored in MongoDB.

4. To export all data to CSV, run:
    ```sh
    python process_data.py
    ```
    This will create a `user_data.csv` file in the project directory.

5. Analyze the exported data using the provided Jupyter notebook `analysis.ipynb`.

## Data Model
Each user submission includes:

- Age (integer)
- Gender (string)
- Income (float)
- Expenses (dictionary with keys: utilities, entertainment, school_fees, shopping, healthcare)

## Analysis
- The `analysis.ipynb` notebook demonstrates how to:
    - Load and preview the data 
    - Visualize average income by age
    - Compare spending by gender and category
    - Generate descriptive statistics

## Customization
- To add more expense categories, update:
    - The categories list in `app.py`
    - The form in `index.html`
    - The export logic in user.py and `process_data.py`

## License
This project is for educational purposes.

## Author:
Patrick Teye
patrick96rich@gmail.com