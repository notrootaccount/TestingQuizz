from db.dbfunctions import *
from db.initdatabase.initquestions import init_questions, init_descriptions
import os
def start_db():
    ############################################################################################################
    #########                              Database definition                                                 #
    ############################################################################################################
    # Path definition: inside the app dir to aboid permission issues
    db_path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+'\\app\\database.db'


    # it use the "init_database" function from db_functions.py where it create the database and define the structure of the tables

    #check if db already exists
    if os.path.isfile(db_path):
        print("db exists in "+db_path)
    #if not exists, it creates it
    else:
        print("creating db in"+db_path)
        init_database(db_path)
        # it creates a connection and cursor to go throught database
        con = sqlite3.connect(db_path)
        con.execute('PRAGMA foreign_keys=ON')
        cur = con.cursor()


        # Insert all descriptions first for data integrity
        for val in init_descriptions.keys():
            insert_description(cur,val,init_descriptions[val])



        # It insert the initial questions from "initquestions.py" inside the database"
        for que in init_questions:
            insert_question(cur,que['idq'],que['question'])
            for anse in que['ans']:
                insert_newanswer(cur,anse['text'],anse['value'],que['idq'])
        # The database have reference integrity and the functions to insert answers or questions are defined in db_functions.py

        """
        # this is testing code to check the db content. The db have 2 tables, one for questions and one for answers, it can be really usefull for testing issues
        all_answers = cur.execute("SELECT questions.idq, answers.text, answers.value FROM questions LEFT JOIN answers ON questions.idq = answers.idq").fetchall()
        idqs = cur.execute("SELECT * FROM questions").fetchall()
        for id in idqs:
            i=1
            print(id[0])
            print(id[1])
            for sans in all_answers:
                if sans[0] == id[0]:
                    print(str(i)+". "+sans[1]+"---"+sans[2])
                    i=i+1
            print("")
            print("----------------------------")
            print("")
        """
# its really important to "commit" and close all connections to ensure the changes are saved.
        con.commit()
        con.close()
