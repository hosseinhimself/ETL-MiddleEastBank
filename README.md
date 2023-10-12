
# ETL-MiddleEastBank

This technical task, named ETL-MiddleEastBank, was done for the position of a Data Engineer at a Middle East bank. The project focuses on the Extract, Transform, Load (ETL) process for financial data from the Fipiran API into a PostgreSQL database. The project includes three main Python scripts: `extract.py`, `transform.py`, and `load.py`, along with an orchestrating script, `ETL.py`.

## Project Components

### Extract.py
The `extract.py` script is responsible for fetching data from the Fipiran API, processing the retrieved data, and saving it to a JSON file. The following functions are defined within this script:

- `fetch_data_from_api(api_url)`: Fetches data from the specified API URL.
- `extract(api_url)`: Calls `fetch_data_from_api()` to retrieve data from the API.
- `save_to_json(data)`: Saves the extracted data to a JSON file.

### Transform.py
The `transform.py` script focuses on transforming the extracted data into a structured DataFrame and performing necessary data cleaning operations. The functions within this script include:

- `load_json_file(name)`: Loads data from a JSON file into a DataFrame.
- `main()`: Loads data, processes it into a DataFrame, and performs data transformations.

### Load.py
The `load.py` script manages the loading of the transformed data into a PostgreSQL database by creating tables and saving relevant data. It includes the following functions:

- `drop_Nan_columns(df)`: Drops columns with all NaN values.
- `main(df)`: Loads transformed data into separate tables in the PostgreSQL database.

### ETL.py
The `ETL.py` script orchestrates the ETL process by calling functions from `extract.py`, `transform.py`, and `load.py`. It sequentially calls the `main()` functions from `extract.py`, `transform.py`, and `load.py` to perform the ETL process.

## PostgreSQL Integration
Although the project mentions PostgreSQL integration, the specific code related to interacting with a PostgreSQL database is not provided in the snippets. The candidate for this position would be expected to implement the necessary code to interact with a PostgreSQL database.

## Execution Instructions
To run the ETL process, it's crucial to configure the PostgreSQL database credentials appropriately in the `ETL.py` script before running the ETL process. Additionally, the candidate should ensure they have the required dependencies installed, such as `requests`, `pandas`, and any necessary PostgreSQL libraries.

To initiate the ETL process, the candidate should execute `ETL.py` using the following command:

```bash
python ETL.py
```

This command will extract data from the Fipiran API, transform it, and load it into the specified PostgreSQL database.
