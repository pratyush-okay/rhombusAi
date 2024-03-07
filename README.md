# RhombusAI

YouTube Video [text](https://youtu.be/r3pnB1LcQg8)

# Data Processing Web Application

This web application is designed to process and display data, focusing on data type inference and conversion for datasets. The project comprises three main tasks: 

1. **Pandas Data Type Inference and Conversion (Backend Task):**
   - Develop a Python script using Pandas capable of inferring and converting data types in a dataset.
   - Address common issues with Pandas data types, such as incorrect inferences and handling mixed data types.
   - Ensure the script can handle large files and optimize for performance.
   - Refer to the provided `backend_task.ipynb` script as a starting point.

2. **Django Backend Development:**
   - Set up a Django project incorporating the Python script for data processing.
   - Create Django models, views, and URLs to handle data processing logic and user interactions.
   - Implement a backend API to work with the frontend.

3. **Frontend Development using React:**
   - Develop a frontend application using React to interact with the Django backend.
   - Allow users to upload CSV/Excel files, submit them for processing, and display the processed data.
   - Map backend (Pandas) data types to user-friendly names.
   - Provide users with the option to override inferred data types.
That's great! Dockerizing your project can make it easier to manage and deploy. Here's how you can update your README file to include Docker instructions:


## Getting Started

### Docker Instructions

To run the application using Docker, follow these steps:

1. Clone the repository:

   ```sh
   git clone https://github.com/pratyush-okay/rhombusAi.git
   ```

2. Build the Docker images for the frontend and backend:

   ```sh
   cd rhombusAi
   docker-compose build
   ```

3. Start the Docker containers:

   ```sh
   docker-compose up
   ```

4. Access the application at http://localhost:3000 in your browser.

## Getting Started Without Docker

1. Clone the repository:
   ```bash
   git clone https://github.com/pratyush-okay/rhombusAi.git
   ```

2. Install dependencies for the frontend and backend:
   ```bash
   cd frontend
   npm install
   cd ../backend
   pip install -r requirements.txt
   ```

3. Run the Django server for the backend:
   ```bash
   cd backend
   python manage.py runserver
   ```

4. Run the React development server for the frontend:
   ```bash
   cd frontend
   npm start
   ```

5. Access the application at `http://localhost:3000` in your browser.

## Project Structure

- **Backend:** Django project containing the data processing Python script.
- **Frontend:** React application for the user interface.
- **Tests:** Pytest for testing the data processing script.
- `data_processing_script.py`: Python script for Pandas data type inference and conversion.


Here's an updated version of the README file that includes information about the tests written using pytest:

---

# Data Processing Web Application

## Overview

You are tasked with creating a web application that processes and displays data, focusing on data type inference and conversion for datasets using Python and Pandas. The project comprises three main tasks:

1. **Pandas Data Type Inference and Conversion (Backend Task):**
   - Develop a Python script using Pandas capable of inferring and converting data types in a dataset.
   - Address the common issues where many columns default to 'object' dtype and Pandas might incorrectly infer types.
   - Ensure the script can handle large files and optimize it for performance.

2. **Django Backend Development:**
   - Set up a Django project incorporating your Python script for data processing.
   - Create Django models, views, and URLs to handle the data processing logic and user interactions.
   - Implement a backend API that works with the frontend, handling data input and output.

3. **Frontend Development using a JavaScript Framework (React Preferred):**
   - Develop a frontend application using a JavaScript framework, preferably React, to interact with the Django backend.
   - Allow users to upload data (CSV/Excel files), submit it for processing, and display the processed data.
   - Map the backend (Pandas) data types to user-friendly names.

## Running the Tests

### Prerequisites

Ensure you have Python and Pipenv installed on your machine.

### Running Tests

To run the tests, use the following command:

```bash
pytest
```

This will execute all the test cases and display the results.

## Testing Approach

Pytest is used for testing the data processing Python script. Each function in the script is tested individually to ensure it behaves as expected for different types of input. Test cases cover both positive and negative scenarios to validate the function's behavior under various conditions.

## Test Files

- **test_data_processing.py:** Contains test cases for the data processing script.

## Technologies Used

- Python
- Pandas
- Django
- React

## License

This project is licensed under the [MIT License](LICENSE).


