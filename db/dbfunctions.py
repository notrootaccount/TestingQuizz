import re,sqlite3

def secure_formvalues(query):
    #####################################################################################
    ################################## Secure form values ###############################
    # We need to secure de value we insert into query to prevent sql injections         #
    #####################################################################################
    # With this we check if the "value" parameter dont have any special character like '"|\ ...
    # Also we check if the string dont contain SQL keywords

    valid_String = "^[A-Za-z0-9.,áéíóú ?¿¡!:()ñ]*[A-Za-z0-9.,áéíóú ?¿¡!:()ñ]$"
    Invalid_Strings = "(UNION)|(JOIN)|(SELECT)|(DELETE)|(INSERT)|(UPDATE)|(DROP)|(CREATE)"

    if ( re.search(Invalid_Strings,query,re.IGNORECASE) or not re.search(valid_String,query,re.IGNORECASE) ):
        print("SQL INJECCTION ATTEMPT or Dangerous character")
        print(query)
        return ""
    else:
        return query

    #####################################################################################

def insert_question(cursor,id,question):
    #####################################################################################
    ################################## INSERT QUESTION  #################################
    # This function sends query with id and text for questions to table questions       #
    #####################################################################################
    id = secure_formvalues(id)

    question = secure_formvalues(question)

    if ( id=="" or question == "" ):
        return "Error: SQLInjection or empty value"
    else:
        query = "INSERT INTO questions (idq, question) VALUES (\'"+id+"\', \'"+question+"\')"


    try:
        cursor.execute(query)
        print("Question Added")
    except sqlite3.IntegrityError as Eerror:
        print("Error de integridad: "+str(Eerror))
        print(question)
        print(id)
    ######################################################################################

def insert_newquestion(cursor, question):
    #####################################################################################
    ################################## INSERT QUESTION  #################################
    # This function sends query with id and text for questions to table questions       #
    #####################################################################################

    select_top_query = "SELECT idq FROM questions ORDER BY length(idq) DESC, idq DESC LIMIT 1"

    try:
        result = cursor.execute(select_top_query).fetchall()
        # obtenemos el valor del último idq
        id = result[0][0]
        # sacamos la p del inicio y le sumamos 1 y volvemos a generar el id
        id = id[0] + str(  int(id[1:]) + 1 )
        # creamos la nueva entrada
        insert_question(cursor, id, question)
        return True
    except:
        if len(cursor.execute("SELECT name FROM sqlite_master WHERE name='questions'").fetchall()) == 0:
            print("No table questions found")
            return False
        elif len(cursor.execute("SELECT idq FROM questions").fetchall()) == 0:
            print("First Question added")
            insert_question(cursor, 'p1', question)
            return True

        print("Error, no es posible obtener el último valor")
        return False


    #####################################################################################



    #####################################################################################

def insert_newanswer(cursor, ans, value, idq):
    #####################################################################################
    ################################## INSERT answers  #################################
    # This function chekcs the integrity, the existence of question and then send ans  #
    #####################################################################################
    idq = secure_formvalues(idq)

    ans = secure_formvalues(ans)

    if (idq == "" or ans == ""):
        return "Error: SQLInjection or empty value"
    elif len(cursor.execute("SELECT name FROM sqlite_master WHERE name='answers'").fetchall()) == 0:
        print("No table answers found")
        print(cursor.execute("SELECT name FROM sqlite_master WHERE name='answers'").fetchall())
        return False
    elif len(cursor.execute("SELECT idq FROM questions WHERE idq = \'" + idq +"\'" ).fetchall()) == 0:
        print("Not idq question match")
    else:
        query = "INSERT INTO answers (text, value, idq) VALUES (\'" + ans + "\', \'" + value + "\', \'" +idq + "\')"

        try:
            cursor.execute(query)
            print("Answer Added")
        except sqlite3.IntegrityError as Eerror:
            print("Error de integridad: " + str(Eerror))
            print(ans)
            print(id)

        return True


    return False


    #####################################################################################

def insert_description(cursor,value,text):
    #####################################################################################
    ################################## INSERT DESCPRIPT  #################################
    # This function sends query with value and text for descriptions of clases           #
    #####################################################################################
    value = secure_formvalues(value)

    text = secure_formvalues(text)

    if ( value=="" or text == "" ):
        return "Error: SQLInjection or empty value"
    else:
        query = "INSERT INTO descriptions (value, text) VALUES (\'"+value+"\', \'"+text+"\')"


    try:
        cursor.execute(query)
        print("Description Added")
    except sqlite3.IntegrityError as Eerror:
        print("Error de integridad: "+str(Eerror))
        print(value)
        print(text)
    ######################################################################################

def send_singlequery(query,db):
    ##########################################################################################
    #########################   SEND a single Query ###########################################
    ##########################################################################################
    # just to manage things. Dont add it into the code
    con = sqlite3.connect(db)
    cur=con.cursor()
    cur.execute(query)
    con.commit()
    con.close()

def managedb(action,db):
    #####################################################################################
    ################################## MANAGE FUNCTION  #################################
    #            MADE TO CALL SPECIFIC FUNCTIONS FOR MANAGEMENT PURPOSES                #
    #####################################################################################
    if action == 'init':
        init_database(db)
        return True

    elif action=='drop':
        print(send_singlequery("SELECT * FROM questions",db))
        send_singlequery("DROP TABLE IF EXISTS questions",db)
        send_singlequery("DROP TABLE IF EXISTS answers",db)
        return True
    #####################################################################################

def get_all_info_structured(db):
    #####################################################################################
    ################################## get all info     #################################
    #    Take the info from the Data Base and put into an estructured data variable     #
    #####################################################################################
    question_final_list = []
    final_dict = {}

    # it makes the conections with the db
    con = sqlite3.connect(db)
    cur = con.cursor()

    # here we make the query to send to sqlite3, it joins both questions and answers"
    all_answers = cur.execute(
        "SELECT questions.idq, answers.text, answers.value FROM questions LEFT JOIN answers ON questions.idq = answers.idq").fetchall()
    # here we take all the questions id and text from db
    idqs = cur.execute("SELECT * FROM questions").fetchall()

    # here I created the same structure that we had in the file
    question_content={}
    #question its a dict with 3 entries: idq, question and ans. Ans is a list of all answers.
    # aux_answers = [] have a list of dicts aux_answer_content which contains the keys text and value
    aux_answer_content = {}

    for id in idqs:
        """
        question{
                    idq=0
                    question = esta es la pregunta?
                    ans = [
                                        {text = respuesta , value=valor}
                                        {text = respuesta , value=valor}
                                        {text = respuesta , value=valor}
                                        {text = respuesta , value=valor}
                                        ]
        
                }
        """

        question_content["idq"]=id[0]
        question_content["question"]=id[1]
        aux_answers = []

        for sans in all_answers:
            if sans[0] == id[0]:
                # interesante: en los loop hay que crear un objeto nuevo o SI NO mantiene la dirección de la variable
                aux_answer_content = { 'text' : sans[1] , 'value': sans[2]}
                aux_answers.append(aux_answer_content)

        #we add to the question_content the value of ans
        question_content["ans"]=aux_answers
        # we add to the final list the entry of this question
        question_final_list.append(question_content)
        # clean the aux variable question_content for restart in the next loop
        question_content={}
    description={}
    descs = cur.execute("SELECT * FROM descriptions").fetchall()
    for desc in descs:
        description[desc[0]]=desc[1]

    final_dict = {
        'questions':question_final_list,
        'descriptions':description }

    #Close the connection wtih db and return final variable
    con.commit()
    con.close()
    return final_dict

    #####################################################################################

def init_database(db):
    ## conection data base ##
    con = sqlite3.connect(db)
    cur = con.cursor()
    ##########################################################################################
    #########################   DATA BASE CREATION ###########################################
    ##########################################################################################
    # Table definition
    # First of all: enable integrity reference
    con.execute('PRAGMA foreign_keys=ON')
    query_create_table_questions = """CREATE TABLE IF NOT EXISTS questions (
                                                idq varchar(10) PRIMARY KEY,
                                                question TEXT NOT NULL
                                                );"""

    cur.execute(query_create_table_questions)
    query_create_table_questions = """CREATE TABLE IF NOT EXISTS descriptions (
                                                value varchar(30) PRIMARY KEY,
                                                text TEXT NOT NULL
                                                );"""

    cur.execute(query_create_table_questions)
    query_create_table_answers = """CREATE TABLE IF NOT EXISTS answers (
                                                ida INTEGER PRIMARY KEY AUTOINCREMENT,
                                                text TEXT NOT NULL,
                                                value VARCHAR(30),
                                                idq varchar(10),
                                                FOREIGN KEY (idq) REFERENCES questions(idq),
                                                FOREIGN KEY (value) REFERENCES descriptions(value)
                                                );"""
    cur.execute(query_create_table_answers)
    con.commit()
    con.close()
    ##########################################################################################

