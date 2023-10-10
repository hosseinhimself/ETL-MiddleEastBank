# ETL-MiddleEastBank

This project consists of three Python scripts: `extract.py`, `transform.py`, and `load.py`, as well as an `ETL.py` script that orchestrates the Extract, Transform, Load (ETL) process for financial data from the Fipiran API into a PostgreSQL database.

## Extract.py
`extract.py` contains functions to fetch data from the Fipiran API, process the retrieved data, and save it to a JSON file.

- `fetch_data_from_api(api_url)`: Fetches data from the specified API URL.
- `extract(api_url)`: Calls `fetch_data_from_api()` to retrieve data from the API.
- `save_to_json(data)`: Saves the extracted data to a JSON file.

## Transform.py
`transform.py` involves transforming the extracted data into a structured DataFrame and performing data cleaning operations.

- `load_json_file(name)`: Loads data from a JSON file into a DataFrame.
- `main()`: Loads data, processes it into a DataFrame, and performs data transformations.

## Load.py
`load.py` handles the loading of the transformed data into a PostgreSQL database by creating tables and saving relevant data.

- `drop_Nan_columns(df)`: Drops columns with all NaN values.
- `main(df)`: Loads transformed data into separate tables in the PostgreSQL database.

## ETL.py
`ETL.py` orchestrates the ETL process by calling functions from `extract.py`, `transform.py`, and `load.py`.

- It calls the `main()` functions from `extract.py`, `transform.py`, and `load.py` sequentially to perform the ETL process.

## PostgreSQL
The code related to interacting with a PostgreSQL database is present but is not defined in the provided snippets.

Make sure to configure your PostgreSQL database credentials appropriately in the `ETL.py` script before running the ETL process. Also, ensure you have the required dependencies installed, such as `requests`, `pandas`, and any necessary PostgreSQL libraries.

To run the ETL process, execute `ETL.py`:

```bash
python ETL.py
```

This will extract data from the Fipiran API, transform it, and load it into the specified PostgreSQL database.
