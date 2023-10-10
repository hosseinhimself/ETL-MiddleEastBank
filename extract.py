import json
import requests

def fetch_data_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error", response.status_code)


def extract(api_url):
    data = fetch_data_from_api(api_url)
    # Process the retrieved data
    if data:
        return data


def save_to_json(data):
    # open a file for writing
    try:
        with open("fipiran_data.json", "w") as outfile:
            # write the data to the file in JSON format
            json.dump(data, outfile)
        print("Data Saved Successfully!")
    except:
        print("Error in saving json file")


def main():
    url = "https://fund.fipiran.ir/api/v1/fund/fundcompare/"
    fipiran_data = extract(url)
    save_to_json(fipiran_data)
