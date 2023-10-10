def drop_Nan_columns(df):
    for key in df.keys():
        if df[key].isna().all():
            df = df.drop(key, axis=1)

    return df


def main(df):
    # load into dataframes (each sub-dataframe plays the role of a table in the database

    # table of rank
    rank = df[['regNo', 'name', 'rankOf12Month', 'rankOf24Month', 'rankOf36Month', 'rankOf48Month', 'rankOf60Month',
               'rankLastUpdate']]
    rank = drop_Nan_columns(rank)
    rank.to_csv('database/rank.csv')

    # table of funds
    fund = df[['regNo', 'fundType', 'fundUnit', 'fundPublisher', 'fundWatch', 'fundSize']]
    fund = drop_Nan_columns(fund)
    fund.to_csv('database/fund.csv')

    # table of efficiency
    efficiency = df[
        ['regNo', 'dailyEfficiency', 'weeklyEfficiency', 'monthlyEfficiency', 'quarterlyEfficiency',
         'sixMonthEfficiency',
         'annualEfficiency', 'statisticalNav', 'efficiency']]
    efficiency = drop_Nan_columns(efficiency)
    efficiency.to_csv('database/efficiency.csv')

    # table of the details about manager
    manager = df[['regNo', 'manager', 'managerSeoRegisterNo', 'guarantorSeoRegisterNo', 'websiteAddress', 'auditor', 'custodian', 'guarantor']]
    manager = drop_Nan_columns(manager)
    manager.to_csv('database/manager.csv')

    # table of other details
    details = df[['regNo', 'typeOfInvest', 'initiationDate', 'cancelNav', 'issueNav', 'dividendIntervalPeriod',
                  'guaranteedEarningRate', 'date', 'netAsset', 'estimatedEarningRate', 'investedUnits',
                  'articlesOfAssociationLink', 'prosoectusLink',
                  'beta', 'alpha', 'isCompleted', 'fiveBest', 'stock', 'bond', 'other', 'cash', 'deposit', 'commodity']]
    details = drop_Nan_columns(details)
    details.to_csv('database/details.csv')




"""

from PostgreSQL import Database

if __name__ == "__main__":
    db = Database(host='127.0.0.1', port=5432, database='MEBTest', user='hosseinmh', password='ASD!@#asd123')
    db.connect()

    df = transform()

    columns = '''
    regNo SERIAL PRIMARY KEY,
    name VARCHAR(200),
    rankLastUpdate object
    '''

    db.save_dataframe_to_table('data',df)

    ff = db.get_table_as_dataframe('data')
"""
