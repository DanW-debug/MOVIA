# MOVIA
Movies statistics and recommender system

MOVIA is a statistics an recommender system for movies. Follows you can find a brief explanation of each modules:

The "PI_ETL_Phase.ipynb" IPython Notebook is a notebook that performs the Extraction, Transformation, and Loading (ETL) process for a project called MOVIA. Through code and text cells, various operations are carried out to prepare the data for analysis and visualization.

Here's a general overview of the notebook's flow:

    Importing libraries: Necessary libraries such as pandas, numpy, and matplotlib are imported to perform ETL operations and data visualization.

    Data extraction: A CSV data file is loaded using the pd.read_csv() function from the pandas library. The data is stored in a DataFrame for further processing.

    Data exploration and cleaning: Exploratory analysis is conducted to understand the data structure and quality. This involves checking for missing values, removing duplicates, correcting data formats, and performing necessary transformations.

    Data transformation: Various transformations are applied to the data to prepare it for analysis. This may include calculating new columns, grouping, data filtering, and format manipulation.

    Data analysis and visualization: Data analysis and visualization techniques are used to derive meaningful insights. This may involve generating charts, tables, and statistical summaries to highlight patterns, trends, and relationships in the data.

    Loading transformed data: Once the data has been cleaned and transformed, it can be saved to a new CSV file or another format for future use in the MOVIA project.

The notebook contains both code cells and explanatory text cells, making it easier to understand each step of the ETL process.

The "backend.py" file contains the backend code for the MOVIA project's API. It is responsible for handling incoming requests, processing data, and returning responses. Let's walk through the main components of the file:

    Importing libraries: The necessary libraries are imported, including pandas for data manipulation, FastAPI for creating the API endpoints, and uvicorn for running the FastAPI application.

    Loading the dataset: A dataset, typically a CSV file, is loaded using the pandas library. The data is stored in a DataFrame, which allows for easy data manipulation and analysis.

    API endpoint functions: Several functions are defined as API endpoints using the FastAPI decorators. These functions correspond to different routes that the API can handle. For example:
        The root endpoint ("/") returns a simple "Hello, World!" message.
        The "/api/v1/get_recommended_movies/{movie_title}" endpoint receives a movie title as a parameter and returns recommended movies based on that title.
        Other endpoints handle tasks such as retrieving movie counts per month, per day, querying movie details, and so on.

    Data processing: Within the API endpoint functions, the loaded dataset is manipulated and processed as required. This may involve filtering data, performing calculations, querying specific information, or any other data-related operations.

    Returning responses: After processing the data, the API endpoint functions return responses in the form of JSON objects. These responses may include status indicators, data results, or error messages, depending on the nature of the endpoint.

    Running the application: Finally, the FastAPI application is run using the uvicorn library. The application listens for incoming requests and handles them according to the defined API endpoints.

The "backend.py" file serves as the core of the backend infrastructure for the MOVIA project, enabling data processing and providing a web API for client applications to interact with.

The "frontend.py" file contains the frontend code for the MOVIA project's user interface. It is responsible for creating a web-based application using the Streamlit library, interacting with the backend API, and displaying the results to the user. Let's walk through the main components of the file:

    Importing libraries: The necessary libraries are imported, including Streamlit for building the user interface and making API requests, and the requests library for sending HTTP requests to the backend API.

    API communication functions: Several functions are defined to communicate with the backend API and retrieve data. These functions use the requests library to send HTTP requests to the appropriate API endpoints. For example:
        Functions like get_shoots_per_month and get_shoots_per_day send requests to endpoints that retrieve movie shoot counts per month and per day, respectively.
        Other functions handle tasks such as retrieving title scores, actor details, director details, and recommended movies.

    User interface creation: Using the Streamlit library, the user interface is built by defining interactive elements such as input fields, buttons, and text displays. These elements allow the user to input data or trigger actions.

    Data retrieval and display: When the user interacts with the user interface elements, the corresponding functions for API communication are called to retrieve data from the backend API. The retrieved data is then displayed to the user using Streamlit's text or visualization components.

    Error handling: The frontend code includes error handling logic to handle cases where the API requests fail or return errors. In such cases, appropriate error messages are displayed to the user using Streamlit's error display components.

    Application execution: The main function main() is called to start the Streamlit application. This function defines the layout and behavior of the user interface.

The "frontend.py" file serves as the user interface for the MOVIA project, allowing users to interact with the application and retrieve information from the backend API. It utilizes the Streamlit library to create a user-friendly and interactive experience.

The "ML_Code.py" file contains the machine learning code used in the MOVIA project. It includes functions and utilities related to data processing, model training, and recommendation generation. Let's go through the main components of the file:

    Importing libraries: The necessary libraries for data processing and machine learning are imported. These include pandas for data manipulation, NumPy for numerical computations, and scikit-learn for machine learning algorithms.

    Data preprocessing functions: The file includes functions for loading and preprocessing the movie dataset. For example, the function load_dataset() reads the movie data from a CSV file and returns a pandas DataFrame. Other functions perform tasks such as handling missing values, encoding categorical variables, and scaling numerical features.

    Model training and evaluation: The file contains functions for training and evaluating machine learning models. It includes a function like train_model() that takes the preprocessed data, splits it into training and testing sets, fits a machine learning model on the training data, and returns the trained model. The evaluation function assesses the model's performance using metrics such as accuracy, precision, and recall.

    Recommendation generation: The file includes functions for generating movie recommendations based on user input. It may use techniques like collaborative filtering or content-based filtering to recommend movies similar to the ones specified by the user. The specific recommendation algorithm and implementation depend on the project's requirements.

    Utility functions: The file may contain additional utility functions that support data processing or model training. These functions could include feature engineering, data visualization, or any other tasks relevant to the machine learning pipeline.

The "ML_Code.py" file serves as the core machine learning module for the MOVIA project. It provides functions for data preprocessing, model training, and recommendation generation. This code can be utilized by the backend API to process user requests, apply machine learning algorithms, and return movie recommendations based on the input data.



