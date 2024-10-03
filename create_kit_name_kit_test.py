import sender_stand_request
import data

# esta función cambia los valores en el parámetro "name"
def get_kit_body(name):
    current_body = data.product_kit.copy()
    current_body["name"] = name
    return current_body

# Función de prueba positiva
def positive_assert(kit_body):
    kit_body = get_kit_body(kit_body)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]


#funcion de prueba negativa
def negative_assert_code_400(kit_body):
    kit_body = get_kit_body(kit_body)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400

#numero permitido de caracteres el parametro "name" (1)
def test_create_kit_body_1_letter_in_name_get_success_response():
    positive_assert(data.one_letter_in_name)

#prueba 2
#numero de caracteres permitidos en el parametro "name" 511
def test_create_kit_body_511_letter_in_name_get_success_response():
    positive_assert(data.five_hundred_eleven_letter)

#prueba 3 Error
#parametro "name" es menor a los caracteres permitidos
def test_create_kit_body_0_letter_in_name_get_success_response():
    negative_assert_code_400(data.cero_letter)

#prueba 4 Error
#parametro "name" acepta mas caracteres de los permitidos (512)
def test_create_kit_body_512_letter_in_name_get_success_response():
    negative_assert_code_400(data.more_five_hundred_twelve_letter)

#prueba 5
#el parametro "name" permite caracteres especiales
def test_create_kit_body_has_especial_simbol_in_name_get_success_response():
    positive_assert(data.special_simbol)

#prueba 6
#el parametro "name" permite espacios
def test_create_kit_body_has_space_in_name_get_error_response():
    positive_assert(data.space_in_name)

#prueba 7
#el parametro "name" acepta numeros
def test_create_kit_body_has_number_in_name_get_error_response():
    positive_assert(data.has_number_in_name)

#funcion de prueba negativa no hay parametro de solicitud
def negative_assert_no_name(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400

#prueba 8 error
#La solicitud no contiene el parámetro "name"
def test_create_kit_body_no_name_get_error_response():
    kit_body = data.product_kit.copy()
    kit_body.pop(data.no_name)
    negative_assert_no_name(kit_body)

#prueba 9 error
#en el parametro "name" se pasa una solicitud diferente (numero)
def test_create_kit_body_number_type_name_get_error_response():
    kit_body = get_kit_body(data.number_type_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400

