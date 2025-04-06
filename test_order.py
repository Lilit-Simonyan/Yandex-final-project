# Лилит Симонян, 28-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request as sender
import data

# 1. Создание заказа
def test_create_order_and_find_by_track():
    response_create = sender.post_new_order(sender.data.order_body)
    print(response_create.status_code)
    print(response_create.json())
    assert response_create.status_code == 201

 # 2. Сохраняем track_id
    track_id = response_create.json().get("track")
    print(track_id)
    assert track_id is not None

# 3. Получение заказа по треку
    response_get = sender.get_order_by_track(track_id)
    print(response_get.status_code)
    print(response_get.json())
    assert response_get.status_code == 200
