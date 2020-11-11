"# TestingQuizz" 

# Este proyecto es el tipico básico de una serie de preguntas a las que respondes mediante raddio buttons
# y te devuelve el valor que más has respondido
# creo que es bastante interesante para trabajar ya que es sencillo de entender y entra en juego de casi todo
# además es muy modulable y es fácil de mejorar por diversas vias.
# de momento es muy feo y las variables se guardan en un archivo


# para ejecutarlo has de tener un entorno virtual de python, hacer flask run host="0.0.0.0"
# lo de host 0.0.0.0 es para definir que cualquier host externo se pueda conectar.

# la idea es mejorar los siguientes aspectos
# 1. Generar con css/javascript y algo más un sistema visual adecuado.
# 2. Incluir imagenes que presupongo que nos darán algun quebradero de cabeza
# 3. Crear una base de datos y que los valores los obtenga de la base de datos en vez de un archivo. 
#		3.1 Crear todas las funciones necesarias para interaccionar con la base de datos independientemente del contenido
#		3.2 Crear estas funciones de forma modular, que solo tengan peticio=>respuesta.
#		3.3 Crear un script de creación/edición de base de datos aunque sea muy cutre
# 4. Rehacer todo el sistema para que todo esté en cliente y solo utilice 2 API, una para pedir las preguntas  otra para enviar las respuestas y recibir el resultado.
# 5. ???
# 6. Beneficios