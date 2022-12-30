import pandas as pd


def read_from_restaurant_menus():
    df = pd.read_csv(restaurant_menu_csv_url)
    print(len(df))
    return df


def read_from_restaurant_recommendation():
    df = pd.read_csv(restaurant_recommendation_csv_url)
    return df


def read_from_csv_with_parameters(csv_url, column_name, column_value):
    df = pd.read_csv(csv_url)
    df1 = df.loc[df[column_name] == column_value]
    return df1


restaurant_menu_csv_url = 'restaurant_menus.csv'
restaurant_recommendation_csv_url = 'restaurant_infos.csv'
