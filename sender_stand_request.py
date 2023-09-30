import configuration
import requests
import data

# функция запроса на создание пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.NEW_USER,
                         json=body,
                         headers=data.headers_user)

# функция для создания нового набора внутри пользователя
def post_new_client_kit(kit_body, auth_token):
    auth_headers = data.headers_user.copy() # копируем словарь с заголовком для создания пользователя, чтобы не потерять данные из исходного словаря
    auth_headers["Authorization"] = "Bearer " + auth_token # добавляем в заголовок словаря создаваемого пользователя ключ Authorization со значением "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT,
                         headers=auth_headers,
                         json=kit_body)