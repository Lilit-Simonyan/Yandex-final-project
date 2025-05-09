import requests
import configuration
import data

# Функция для создания заказа
def post_new_order(order_body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=order_body,
        headers=data.headers
    )


# Функция для получения заказа по треку заказа
def get_order_by_track(track_id):
    params = {"t": track_id}
    return requests.get(
        configuration.URL_SERVICE + configuration.FIND_ORDER_TRACK,
        params=params,
        headers=data.headers
    )