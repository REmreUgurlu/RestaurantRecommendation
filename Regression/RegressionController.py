import pandas as pd

from DataAccess.Read import ReadData


def check_regression(data):
    print('Checking Regression rate')
    column_names = ['MenuName', 'Price', 'RestaurantName']
    df_new = pd.DataFrame(data=data, columns=column_names)
    df_new.drop_duplicates(subset=['MenuName'], inplace=True, ignore_index=True)
    df_new.reset_index(inplace=False)
    df_original = ReadData.read_from_csv_with_parameters(ReadData.restaurant_menu_csv_url, 'RestaurantName', df_new['RestaurantName'][0])
    for i in range(0, min(len(df_original), len(df_new))):
        original_price = float(df_original.iloc[i, 2])
        new_price = float(df_new.iloc[i, 1])
        price_change = original_price - new_price
        if price_change != 0.0:
            indexes_of_change.append(i)
            prices_of_change.append(new_price)
            recession_rate = (original_price - new_price) * 100 / original_price
            recessed_item = df_original.iloc[i, 1]
            recession = [recessed_item, recession_rate, new_price]
            recessed_rows.append(recession)
    if len(recessed_rows) == 0:
        return 'No Price Changes at this restaurant'
    else:
        update_csv(df_original)


def update_csv(df_original):
    df_org = pd.DataFrame(df_original)
    for i in range(0, len(indexes_of_change)):
        df_org.iloc[indexes_of_change[i], 2] = prices_of_change[i]

    df_org.to_csv('restaurant_menus.csv', mode='a', index=True)
    return recessed_rows


indexes_of_change = []
prices_of_change = []
recessed_rows = []
