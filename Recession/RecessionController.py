import pandas as pd

from DataAccess.Read import ReadData


def check_recession(data):
    print('Checking Recession rate')
    column_names = ['MenuName', 'Price', 'RestaurantName']
    df1 = pd.DataFrame(data=data, columns=column_names)
    df1.drop_duplicates(subset=['MenuName'], inplace=True, ignore_index=True)
    df1.reset_index(inplace=False)
    df_original = ReadData.read_from_csv_with_parameters(ReadData.restaurant_menu_csv_url, 'RestaurantName', df1['RestaurantName'][0])
    for i in range(0, len(df_original)):
        original_price = float(df_original.iloc[i, 2])
        new_price = float(df1.iloc[i, 1])
        if original_price - new_price != 0.0:
            print(original_price, new_price)
            recession_rate = (original_price - new_price) * 100 / original_price
            recessed_item = df_original.iloc[i, 1]
            recession = [recessed_item, recession_rate]
            recessed_rows.append(recession)
    if len(recessed_rows) == 0:
        return 'No Recession'
    else:
        return recessed_rows


recessed_rows = []
