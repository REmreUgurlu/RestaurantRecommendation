import pandas as pd
from DataAccess.Rules import DataAccessRules


restaurant_info_csv_url = 'restaurant_recommendation.csv'
restaurant_menu_csv_url = 'restaurant_menus.csv'
reviews_csv_url = 'reviews.csv'


def write_to_restaurant_info_csv(data):
    column_names = ["RestaurantName", "Rating", "Type"]
    df = pd.DataFrame(data=data, columns=column_names)
    df.to_csv(restaurant_info_csv_url, mode='a', index=True, header=not DataAccessRules.check_if_csv_exist(restaurant_info_csv_url))


def write_to_restaurant_menu_csv(data):
    column_names = ["MenuName", "Price", "RestaurantName"]
    df = pd.DataFrame(data=data, columns=column_names)
    df.drop_duplicates(subset=['MenuName'], inplace=True, ignore_index=True)
    df.reset_index(inplace=False)
    df.to_csv(restaurant_menu_csv_url, mode='a', index=True, header=not DataAccessRules.check_if_csv_exist(restaurant_menu_csv_url))

