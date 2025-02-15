# My Web App

This project is a web application that combines FastAPI and Streamlit to provide a seamless user experience. The FastAPI backend serves as an API for handling requests, while the Streamlit frontend offers an interactive user interface.

## Project Structure

```
my-web-app
├── app
│   ├── main.py                # Entry point for the FastAPI application
│   ├── api
│   │   └── v1
│   │       └── endpoints.py   # API endpoints for the application
│   ├── streamlit_app.py       # Streamlit application code
│   └── models
│       └── __init__.py        # Data models or schemas
├── requirements.txt           # Project dependencies
├── tech_stack.csv             # Tech stack and portfolio websites
├── testing_chroma.ipynb       # Jupyter notebook for ChromaDB testing
├── testing_groq.ipynb         # Jupyter notebook for Groq testing
└── README.md                  # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-web-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the FastAPI application:
   ```
   uvicorn app.main:app --reload
   ```

4. Start the Streamlit application:
   ```
   streamlit run app/streamlit_app.py
   ```

## Usage

- Access the FastAPI documentation at `http://127.0.0.1:8000/docs` to explore the available API endpoints.
- Use the Streamlit application to interact with the backend and visualize data.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.