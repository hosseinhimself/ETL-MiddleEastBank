import json
import pandas as pd

def load_json_file(name):
    try:
        with open(name, "r") as infile:
            # load the data from the json file
            data = json.load(infile)
            print('Data loaded from the json file')
            return data
    except:
        print("Error! JSON file didn't load!")


def main():
    data = load_json_file('fipiran_data.json')
    df = pd.DataFrame(data['items'])

    # fill NaN values (as
    df = df.replace('0001-01-01T00:00:00', pd.NaT)
    df['initiationDate'] = pd.to_datetime(df['initiationDate'], format='mixed', dayfirst=True)
    df = df.interpolate()
    return df



