from flask import render_template, request, redirect, make_response
from app import app, preguntas, descriptions

###################             Nuestras variables          #############################
#en el modulo inform tengo los datos, en un futuro debería sacarlos de una base de datos#
#########################################################################################
from app import inform
global clases
#       sería interesante buscar como hacer
#       para que no sean globales y solo los utilice el modulo que toca#
#########################################################################################





###################             Definición de rutas          ############################
#########################################################################################
# Flask no utiliza un sistema de permisos por arbol de directorios, parece que tienes que
# definir las posibles rutas a las que se puede acceder y que función ejecutarán (las de abajo)
# muy interesante ya que da mucho juego
# es importante indicar que utilizará los metodos get o post para poder enviar cosas con el formulario
@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
#al parecer el orden es muy importante, tiene que ser definición de ruta "@app.route(...)" y luego la función "def ...(): ..."

#########################################################################################





###################                   Página INDEX           ############################
#########################################################################################
def index():
    # La variable "preguntas" es global, por lo que ya está definida cuando iniciamos flask.
    # la variable preguntas se asigna a questions que se utilizará en el template

    return render_template('index.html', questions=preguntas)
    #en el return le ponemos lo que queremos que devuelva, en este caso devuelve la plantilla que haya en "index.html" 
    # dentro de la carpeta templates. Además hay que asignarle las variables que se utilicen en el jinja
    # de la plantilla que devolverá, en este caso a la variable "questions" del html le he asignado 
    # el valor de la variable "preguntas"
    # después se ejecutará el código jinjja en el servidor y se enviará un html plano al cliente
#########################################################################################


###################                   Página resultados      ############################
#########################################################################################
@app.route('/resultado', methods=['GET','POST'])
def resultado():
# aquí creo una lista para rellenar con los resultados y un diccionario para rellenar con x 
# los pares resultado y cantidad de veces que aparecen
    results_list_all = []
    results_list_counted = {}

    for question in preguntas:
       results_list_all.append(request.form.get(question.get('idq')))
       
    #hace una lista de las respuestas que se han enviado
    
    while len(results_list_all)!=0:
        aux_value=results_list_all[0]
        results_list_counted.update({aux_value:results_list_all.count(aux_value)})
        # Coje la primera respuesta
        # mira cuantas respuestas tienen el mismo valor y las cuenta
        # crea un diccionario con el valor y la cantidad de respuestas iguales
        while results_list_all.count(aux_value)!=0:
            results_list_all.remove(aux_value)
            #elimina todas las respuestas que contienen ese valor
        # ahora pasa a la siguiente respuesta, que será diferente porque ha eliminado todas las respuestas iguales
            
            
            
    #elimina el valor None que se produce al no contestar algo
    if None in results_list_counted.keys():
        results_list_counted.pop(None)
    
    
    
    
    
    ###############################ALGORITMO DE DECISIÓN DE CLASE #################################
    if len(results_list_counted) == 0:
        clase="No definido"
        descripcion = "Respuestas no pueden definir ninguna clase"
    else:
        result_max=max(results_list_counted.values())
        for value in results_list_counted.keys():
            if results_list_counted.get(value)==result_max:
                clase=value
                break
        descripcion=descriptions.get(clase)

    if clase == 'fighter':
        color='#6E5841'
    elif clase == 'bard':
        color='#C94DDA'
    elif clase == 'barbarian':
        color = '#B43327'
    elif clase == 'druid':
        color = '#4AB427'
    elif clase == 'wizard':
        color ='#2771B4'
    elif clase == 'rogue':
        color = '#434C54'
    elif clase == 'cleric':
        color = '#B4AF27'
    elif clase == 'monk':
        color = '#C8CA65'
    elif clase == 'sorcerer':
        color = '#F96226'
    else:
        color = 'black'

    ###############################################################################################
    return render_template('resultado.html', clase=clase,descripcion=descripcion,color=color)

#########################################################################################