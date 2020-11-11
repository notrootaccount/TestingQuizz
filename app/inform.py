#De momento se guardan variables con la información
preguntas = [
		{
			'idq':'p1',
			'pregunta':'En tu camino por el mundo te encuentras a un esclavista que ha capturado a uno de tus amigos ¿Que harías?', 
			'respuestas': [ {'texto':'Iomedae (tu dios) está en contra de la eslavitud, por lo que utilizaré el poder de Iomedae para juzgar a este malevolo ser.', 'value':'paladin'},
                            {'texto':'Odio las cadenas, partiré en dos al esclavista con mi espada ¡Y LUEGO DESTROZARÉ LAS CADENAS CON MIS PROPIAS MANOS! ','value':'barbarian'}, 
                            {'texto':'Me acercaré como si quisiera adquirir uno de sus esclavos y luego le apuñalo en el cuello','value':'rogue'},
                            {'texto':'¡BOLA DE FUEGO! Luego ya veré si ha sobrevivido mi amigo','value':'sorcerer'},
                            {'texto':'Me acerco de forma rápida al esclavista y le asesto una serie de puñetazos muy rápido para dejarlo inconsciente, luego rompo el candado de un puñetazo','value':'monk'}
                          ]
                            
		},
		{
			'idq':'p2',
			'pregunta':'Unos goblins han acampado cerca de la capital, tienes que deshacerte de ellos ¿Qué haces?', 
   			'respuestas': [ {'texto':'¿Enserio hay gente que duda en esta opción? ¡BOLA DE FUEGO!', 'value':'sorcerer'},
                            {'texto':'Observo el terreno y elaboro un plan de ataque que minimice nuestras bajas','value':'fighter'}, 
                            {'texto':'Preparo una gran fiesta en un lugar lejano y los mantengo suficiente tiempo para que acampen allí','value':'bard'},
                            {'texto':'Entramos por la puerta gritando y arrasando con todo lo que veamos, los que sobrevivan estarán tan atemorizados que no volverán nunca','value':'barbarian'},
                            {'texto':'Invoco el poder del bosque para que hordas de animales salvajes arrasen su aldea mientras observo desde lejos','value':'druid'}
                          ]
            
        },
		{
			'idq':'p3',
			'pregunta':'¡Es hora de repartir el tesoro! Tienes que elegir una de las siguientes partes:', 
			'respuestas': [ {'texto':'Los libros y pergaminos con conocimiento, me permitirán crecer y aprender nuevos hechizos', 'value':'wizard'},
                            {'texto':'¡lo más caro!','value':'rogue'}, 
                            {'texto':'Objetos de interés religioso','value':'cleric'},
                            {'texto':'Un arma exotica que a pesar de que es dificil de manejar, tu sabes hacerlo','value':'fighter'},
                            {'texto':'Las posesiones materiales no son de tu interés, pero escogeras las monedas de oro para poder continuar con tu viaje','value':'monk'}
                          ]        
        },
        {
			'idq':'p4',
			'pregunta':'¿Que magia prefieres?', 
			'respuestas': [ {'texto':'¿Estás de broma? ¡BOLA DE FUEGO! ¡ MANOS ARDIENTES ! FUEGO FUEGO FUEGO!', 'value':'sorcerer'},
                            {'texto':'La magia ha de ser bella, cualquier magia que sirva para expresar y crear una obra de arte','value':'bard'}, 
                            {'texto':'Todo tipo de magia, cuanto más variada y más potente mejor','value':'wizard'},
                            {'texto':'La que me proporcione el bosque y pueda ayudar a mi compañero animal','value':'druid'},
                            {'texto':'La que me proporcione Saenrae, mi dios elige mi camino','value':'cleric'}
                          ]
        },
        {
			'idq':'p5',
			'pregunta':'¿Qué estilo de pelea prefieres?', 
			'respuestas': [ {'texto':'1v1 combate justo y a poder ser contra un enemigo malvado', 'value':'paladin'},
                            {'texto':'Estudiar a mi adversario, prácticar mis habilidades de pelea, usar el entorno a mi favor y utilizar la astucia para vencer','value':'fighter'}, 
                            {'texto':'DESTROZAR EL CRANEO DE MIS ENEMIGOS CON UN SOLO GOLPE Y QUE EL RESTO HUYA DE TERROR!','value':'barbarian'},
                            {'texto':'Puñetazos rápidos y mucha movildiad','value':'monk'},
                            {'texto':'Irme y cuando se de la espalda ¡APUÑALARLE EN EL CUELLO!','value':'rogue'}
                          ]
        },
        {
			'idq':'p6',
			'pregunta':'Si un amigo necesitase ayuda en batalla... ¿Como le ayudarías?', 
			'respuestas': [ {'texto':'Distraería a los enemigos, utilizaría mi escudo para protegerle y le curaría si fuera necesario', 'value':'paladin'},
                            {'texto':'Le quitaría el miedo, le daría fuerza y le curaría gracias al poder de Saenrae','value':'cleric'}, 
                            {'texto':'¿¡Mi gato está en peligro?! Me centraría en el, utilizaría toda mi magia para revitalizarle, fortalecerle y curarle','value':'druid'},
                            {'texto':'Le inspiraría con mis canciones para que luchara con más fuerza y más rápido','value':'bard'},
                            {'texto':'En mi gran colección de hechizos siempre tengo uno para cada ocasión','value':'wizard'}
                          ]
        },
        {
			'idq':'p7',
			'pregunta':'¡Hora de acampar! ¿Que rol escoges?', 
			'respuestas': [ {'texto':'Recolector y cazador, necesitamos comida', 'value':'druid'},
                            {'texto':'¡Enciendo el fuego! un fuego grande...','value':'sorcerer'}, 
                            {'texto':'Deleito al resto con mis historias, mis canciones... de forma que tengan más fuerza para el día siguiente','value':'bard'},
                            {'texto':'curo las heridas de mis compañeros','value':'cleric'}, 
                            {'texto':'Acabo lo que sea lo más rápido posible con algún hechizo, luego me pongo a estudiar mi libro de conjuros','value':'wizard'}
                          ]
        },
        {
			'idq':'p8',
			'pregunta':'¡Hay que cazar un gran animal maligno! ¿Cual es tu estrategia?', 
			'respuestas': [ {'texto':'Estudio el terreno, busco el mejor sitio para tenderle una emboscada, preparo trampas y me preparo para una pelea ardua', 'value':'fighter'},
                            {'texto':'Me escondo e intento cogerle desprevenido, intento utilizar trampas y venenos. Si el animal me encuentra huyo para poder volver a sorprenderle ne otro momento','value':'rogue'}, 
                            {'texto':'¡CAZA! Me emborracho y voy por el bosque gritando para atraerlo y poder luchar cuando me encuentre','value':'barbarian'},
                            {'texto':'Salto entre los arboles hasta que lo encuentre. En la pelea me dedicaré a esquivar sus golpes mientras le asesto puñetazos rápidos y precisos','value':'monk'},
                            {'texto':'Evito las trampas y el veneno ya que son herramientas deshonrosas. Soy capaz de detectar el mal, lo encontraré y acabaré con el.','value':'paladin'}
                          ]
        }
       
       
       
       
       
		]

clases = {
#debería mejorar las explicaciones
"fighter":"Pelea con armas, astuto...",
"barbarian":"¡Pelea con una peazo espada! ¡CHILLA MUCHO Y DESTRUYE COSAS!",
"paladin":"luchador del dios Iomedae, la justicia y el honor",
"monk":"lucha con los puños, da saltitos",
"rogue":"picaro que apuñala cuellos, se esconde y engaña a la gente",
"cleric":"healbot, tu objetivo es curar a los demás",
"druid":"amante de los arboles, tiene un gato gigante que hace mucho daño e invoca un monton de bichitos que molestan",
"wizard":"mago, hace de todo con magia, puede aprender muchisimos hechizos pero puede utilizar pocos cada día",
"sorcerer":"boladefuegoman, tu objetivo es prender cosas",
"bard":"Cantas canciones, obsesionado con la belleza y el arte, seduces todo lo que se mueva y eres un juerguista nato"
}
