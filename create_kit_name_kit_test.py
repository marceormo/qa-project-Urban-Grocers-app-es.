import sender_stand_request
import data

# esta función cambia los valores en el parámetro "name"
def get_kit_body(name):
    current_body = data.user_body.copy()
    current_body["name"] = name
    return current_body

# Función de prueba positiva
def positive_assert(kit_body):
    user_body = get_kit_body(kit_body)
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 201
    assert user_response.json().get("authToken")

#funcion de prueba negativa
def negative_assert_code_400(kit_body):
    user_body = get_kit_body(kit_body)
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400

#numero permitido de caracteres el parametro "name" (1)
def test_create_user_1_letter_in_name_get_success_response():
    positive_assert("one_letter_in_name")

#prueba 2
#numero de caracteres permitidos en el parametro "name" 511
def test_create_user_511_letter_in_name_get_success_response():
    positive_assert("five_hundred_eleven_letter")

#prueba 3 Error
#parametro "name" es menor a los caracteres permitidos
def test_create_user_0_letter_in_name_get_success_response():
    negative_assert_code_400("cero_letter")

#prueba 4 Error
#parametro "name" acepta mas caracteres de los permitidos (512)
def test_create_user_512_letter_in_name_get_success_response():
    negative_assert_code_400("more_five_hundred_twelve_letter")

#prueba 5
#el parametro "name" permite caracteres especiales
def test_create_user_has_especial_simbol_in_name_get_success_response():
    positive_assert("special_simbol")

#prueba 6
#el parametro "name" permite espacios
def test_create_user_has_space_in_name_get_error_response():
    positive_assert("space_in_name")

#prueba 7
#el parametro "name" acepta numeros
def test_create_user_has_number_in_name_get_error_response():
    positive_assert("has_number_in_name")

#funcion de prueba negativa no hay parametro de solicitud
def negative_assert_no_name(user_body):
    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400

#prueba 8 error
#La solicitud no contiene el parámetro "name"
def test_create_user_no_name_get_error_response():
    user_body = data.user_body.copy()
    user_body.pop("no_name")
    negative_assert_no_name(user_body)

#prueba 9 error
#en el parametro "name" se pasa una solicitud diferente (numero)
def test_create_user_number_type_name_get_error_response():
    user_body = get_kit_body("number_type_name")
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400

