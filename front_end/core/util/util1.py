def get_bast_value_buy(json_data):

    if json_data == None:

        return 0

    elif len(json_data) > 0:

        best_price = float(json_data[0]['negotiable_price'])

        for data in json_data:

            if best_price >= float(data['negotiable_price']):

                best_price = float(data['negotiable_price'])

        return best_price

    else:

        return 0


def get_bast_value_sell(json_data):

    if json_data == None:

        return 0

    elif len(json_data) > 0:

        best_price = float(json_data[0]['negotiable_price'])

        for data in json_data:

            if best_price <= float(data['negotiable_price']):

                best_price = float(data['negotiable_price'])

        return best_price

    else:

        return 0