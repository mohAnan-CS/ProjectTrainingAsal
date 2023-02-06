import pandas as pd
from file_operation import ObjectCreator


def read_product_file(path_file):
    data = pd.read_csv(path_file)
    product_list = []
    for index in data.index:
        product_id = data['product_id'][index]
        product_type = data['product_type'][index]
        product = data['product'][index]
        price = data['current_retail_price'][index]
        product_obj = ObjectCreator.create_product_obj(product_id,
                                                       product_type,
                                                       product,
                                                       price)
        product_list.append(product_obj)

    return product_list

