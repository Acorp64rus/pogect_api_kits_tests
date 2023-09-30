import sender_stand_request
import data

# ПОДГОТОВКА К ТЕСТИРОВАНИЮ
# Функция для создания токена
def get_new_user_token():
    new_user = sender_stand_request.post_new_user(data.user_body) # в переменную new_user сохраняем результат запроса на создание нового пользователя
    auth_token = new_user.json()["authToken"] # в переменную auth_token сохраняем полученное тело с authToken созданного пользователя
    return auth_token # возвращаем значение authToken

# Функция, которая меняет содержимое тела запроса
def get_kit_body(name): # задаем функцию с параметром name
    current_body = data.kit_body.copy() # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body["name"] = name # изменение значения ключа name в словаре тела
    return current_body # возвращается новый словарь с нужным значением name

# Функция для позитивных проверок
def positive_assert(name):
    kit_body = get_kit_body(name) # в переменную kit_body сохраняем измененное тело запроса
    auth_token = get_new_user_token() # сохраняем результат получения в переменную auth_token для передачи
    set_response = sender_stand_request.post_new_client_kit(kit_body, auth_token) # в переменную set_response сохраняем результат запроса на создание набора
    assert set_response.status_code == 201 # проверяем соответствие статус кода ответа
    assert set_response.json()["name"] == name # проверяем изменилось ли имя набора

# Функция для негативных проверок
def negative_assert_code_400(name):
    kit_body = get_kit_body(name) # в переменную kit_body сохраняем измененное тело запроса
    auth_token = get_new_user_token() # сохраняем результат получения в переменную auth_token для передачи
    set_response = sender_stand_request.post_new_client_kit(kit_body, auth_token) # в переменную set_response сохраняем результат запроса на создание набора
    assert set_response.status_code == 400 # проверяем соответствие статус кода ответа

# ТЕСТИРОВАНИЕ
# Тест 1. Допустимое количество символов (1)
def test_create_kit_1_letter_in_kit_name_get_success_response():
    positive_assert("a")

# Тест 2. Допустимое количество символов (511)
def test_create_kit_511_letters_in_kit_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест 3. Количество символов меньше допустимого ("")
def test_create_kit_0_letters_in_kit_name_get_error_response():
    negative_assert_code_400("")

# Тест 4. Количество символов больше допустимого (512)
def test_create_kit_512_letters_in_kit_name_get_error_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест 5. Разрешены английские буквы ("QWErty")
def test_create_kit_eng_letters_in_kit_name_get_success_response():
    positive_assert("QWErty")

# Тест 6. Разрешены русские буквы ("Мария")
def test_create_kit_rus_letters_in_kit_name_get_success_response():
    positive_assert("Мария")

# Тест 7. Разрешены спецсимволы (""№%@",")
def test_create_kit_spec_letters_in_kit_name_get_success_response():
    positive_assert('"№%@",')

# Тест 8. Разрешены пробелы (" Человек и КО ")
def test_create_kit_whitespaces_letters_in_kit_name_get_success_response():
    positive_assert(" Человек и КО ")

# Тест 9. Разрешены цифры ("123")
def test_create_numb_spec_letters_in_kit_name_get_success_response():
    positive_assert("123")

# Тест 10. Параметр не передан в запросе (kit_body={})
def test_create_kit_no_name_letters_in_kit_name_get_error_response():
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit({}, "Bearer " + auth_token)
    assert response.status_code == 400
# FAILED create_kit_name_kit_test.py::test_create_kit_no_name_letters_in_kit_name_get_error_response - assert 500 == 400 Прошу прощения, но я не понимаю почему статус код 500

# Тест 11. Передан другой тип параметра (123)
def test_create_kit_int_letters_in_kit_name_get_error_response():
    negative_assert_code_400(123)