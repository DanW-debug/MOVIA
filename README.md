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


