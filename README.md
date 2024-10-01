# Proyecto Urban Grocers 
# Marcela Ortiz Montoya
# Sprint 7, Grupo 14

En este proyecto hice pruebas para la creación de un kit en la aplicación de Urban Grocers. Más específicamente, trabajé en la automatización de 9 pruebas distintas para el parámetro “name”, donde encontré 4 errores.

## Lista de Comprobación de Pruebas

| Nº | Descripción                                                                 | Código de Respuesta                          |
|----|-----------------------------------------------------------------------------|---------------------------------------------|
| 1  | El número permitido de caracteres (1): `kit_body = { "name": "a" }`       | 201 El campo "name" del cuerpo de respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 2  | El número permitido de caracteres (511): `kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}` | 201 El campo "name" en el cuerpo de respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 3  | El número de caracteres es menor que la cantidad permitida (0): `kit_body = { "name": "" }` | 400                                         |
| 4  | El número de caracteres es mayor que la cantidad permitida (512): `kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }` | 400                                         |
| 5  | Se permiten caracteres especiales: `kit_body = { "name": "№%@" }`          | 201 El campo "name" del cuerpo de respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 6  | Se permiten espacios: `kit_body = { "name": " A Aaa " }`                   | 201 El campo "name" del cuerpo de respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 7  | Se permiten números: `kit_body = { "name": "123" }`                        | 201 El campo "name" del cuerpo de respuesta coincide con el campo "name" del cuerpo de la solicitud |
| 8  | El parámetro no se pasa en la solicitud: `kit_body = { }`                 | 400                                         |
| 9  | Se ha pasado un tipo de parámetro diferente (número): `kit_body = { "name": 123 }` | 400                                         |

## Paquetes Utilizados

- **Python**
- **PyCharm**
- **requests**
- **pytest**

Aprendí a trabajar con GitHub y utilicé la terminal para clonar repositorios desde mi computadora.

## Archivos en el Proyecto

- `Configuration.py`
- `sender_stand_request.py`
- `data.py`
- `create_kit_name_kit_test.py`
- `.gitignore`
- `README.md`

## Pasos para Realizar el Proyecto

1. Configuración con Git y GitHub.
2. Clonar el repositorio en el computador.
3. Trabajar con el proyecto de forma local.
4. Hacer pruebas en PyCharm con la ayuda del paquete de pytest.
5. Correr pruebas.
6. Revisar los resultados de las pruebas.

### Como ejecutar las pruebas 
Despues de tener todas las pruebas listas en el Pycharm tener instalado el paquete de pytest, dar clic en la parte superior y elegir la opcion “Current File”
despues dar clic en el icono “Run”
