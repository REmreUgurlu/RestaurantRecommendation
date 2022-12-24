from DataAccess.Read import ReadData
import os


def check_if_csv_exist(csv_url):
    if os.path.exists(csv_url):
        return True
    else:
        return False


def check_if_restaurant_already_searched(restaurant_name):
    rule_result = check_if_csv_exist(ReadData.restaurant_recommendation_csv_url)
    if rule_result is True:
        df = ReadData.read_from_restaurant_recommendation()
        if restaurant_name in df.values:
            return True, 'This restaurant data is already extracted'
        else:
            return False, 'This restaurant can be extracted'
    else:
        return False, 'csv does not exist'
