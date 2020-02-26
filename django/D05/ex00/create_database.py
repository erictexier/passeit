import os
import sys
import json
import psycopg2
from d05 import settings

'''
schema: table name: ex00_movies
title : chaine de charactere variable, unique, d’une taille maximale de 64 octets, non nul.-> character varying [ (64) ]
episode_nb : entier, PRIMARY KEY.   integer
opening_crawl : texte, peut être nul, pas de taille limite. -> character varying [ (n) ]
director : chaîne de caractères variable, non nul, d’une taille maximale de 32 octets. -> char [ (n) ]
producer : chaîne de caractères variable, non nul, d’une taille maximale de 128 octets -> char [ (n) ]
release_date : date (sans l’heure), non nul. --> date
'''

# define the needed and optional key
key_table = ['title', 'director', 'producer', 'release_date']
key_option = ['opening_crawl']

'''
def init_data_base(name, host, user_name, user_password):
    from psycopg2 import sql
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE
    try:
        con = psycopg2.connect( dbname=name,
                                host=host,
                                user=user_name,
                                password=user_password)
    except Exception as e:
        print(str(e))


    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # <-- ADD THIS LINE

    cur = con.cursor()

    # Use the psycopg2.sql module instead of string concatenation 
    # in order to avoid sql injection attacs.
    try:
        cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(name)))
    except Exception as e:
        print(str(e))
        return False 
    print ("DONE")
    return True

def table_exist(dbname, user):
    a = "dbname='{}' user='{}' host='{}' port='{}' password='{}'".format('formationdjango','djangouser','localhost','5432','secret')
    with psycopg2.connect(a) as conn:
        cur = conn.cursor()
        query = "select to_regclass(%s)"
        cur.execute(query, ['{}.{}'.format('schema', table)])
    exists = bool(cur.fetchone()[0])
    cur.close()
    return exists
'''





def DefaultTable(with_crawl = False):
    DATA = '''
    episode_nb : 1 - title : The Phantom Menace - director : George Lucas - producer : Rick McCallum - release_date : 1999-05-19
    episode_nb : 2 - title : Attack of the Clones - director : George Lucas - producer : Rick McCallum - release_date : 2002-05-16
    episode_nb : 3 - title : Revenge of the Sith - director : George Lucas - producer : Rick McCallum - release_date : 2005-05-19
    episode_nb : 4 - title : A New Hope - director : George Lucas - producer : Gary Kurtz, Rick McCallum - release_date : 1977-05-25
    episode_nb : 5 - title : The Empire Strikes Back - director : Irvin Kershner - producer : Gary Kutz, Rick McCallum - release_date : 1980-05-17
    episode_nb : 6 - title : Return of the Jedi - director : Richard Marquand - producer : Howard G. Kazanjian, George Lucas, Rick McCallum - release_date : 1983-05-25
    episode_nb : 7 - title : The Force Awakens - director : J. J. Abrams - producer : Kathleen Kennedy, J. J. Abrams, Bryan Burk - release_date : 2015-12-11
    '''
    ajson = os.path.join(os.path.join(settings.BASE_DIR), 'ex02/static/ex02/opening_crawl.json')
    a=DATA.split("\n")
    aslist = list()
    for aa in a:
        x = aa.split(" - ")
        d = dict()
        for xx in x:
            u = xx.split(":")
            if (len(u) == 2):
                d[u[0].strip()] = u[1].strip()
        if len(d) >= 5:
            aslist.append(d)
    f = open(ajson,"r")
    data = json.loads(f.read())
    if with_crawl:
        for l in aslist:
            for k in data:
                 if k in l['title']:
                    l['opening_crawl'] = data[k].replace("'","&quot;")
    return aslist

#print(DefaultTable())

def table_exist(con, table_name):
    exists = False
    try:
        cur = con.cursor()
        cur.execute("select exists(select relname from pg_class where relname='" + table_name + "')")
        exists = cur.fetchone()[0]
        cur.close()
    except psycopg2.Error as e:
        print(e)
    return exists

CREATE_COMMAND_TABLE_MOVIE = '''
CREATE TABLE %s (episode_nb serial PRIMARY KEY NOT NULL, 
                          title char(64) NOT NULL,
                          opening_crawl varchar, 
                          director char(32) NOT NULL, 
                          producer char (128) NOT NULL, 
                          release_date date NOT NULL);
'''

A_RECORD = '''INSERT INTO %(table)s (episode_nb, title, director, producer, release_date) 
        VALUES ('%(episode_nb)s', '%(title)s', '%(director)s', '%(producer)s', '%(release_date)s')'''
A_RECORD_OPTION = '''INSERT INTO %(table)s (episode_nb, title, director, producer, release_date, opening_crawl) 
        VALUES ('%(episode_nb)s', '%(title)s', '%(director)s', '%(producer)s', '%(release_date)s', '%(opening_crawl)s')'''

def get_connection(host, dbname, user, password):
    try:
        conn = psycopg2.connect("host='{}' dbname='{}' user='{}' password='{}'".format( host,
                                                                                        dbname, 
                                                                                        user, 
                                                                                        password))
    except Exception as e:
        print(str(e))
        return None
    return conn

def insert_into(conn, cur, table_name, record_dict):
    ''' insert a new object into the database
    '''
    if conn == None or cur == None:
        return False
    # wrap the table key for simpler insertion
    record_dict['table'] = table_name
    trecord = A_RECORD
    try:
        for l in key_option:
            if l in record_dict:
                trecord = A_RECORD_OPTION
                break
        cur.execute( (trecord % record_dict) )
    except Exception as e:
        print (str(e))
        return False
    return True

def create_table_movie(host, dbname, user, password, table_name):
    ''' get a connection and create a table table_name if it doesn't exist
    '''
    conn = get_connection(host, dbname, user, password)
    if conn == None:
        return False
    if (table_exist(conn, table_name)):
        return False
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Create table statement
    cur.execute(CREATE_COMMAND_TABLE_MOVIE % table_name)
    conn.commit()
    cur.close()
    return True

def do_it_make_table(table_name):
    return create_table_movie("localhost", "formationdjango", "djangouser", "secret", table_name)

if __name__ == '__main__':
    #do_it_make_table('fake table')
    print (conn = get_connection('localhost', 'formationdjango', 'djangouser', 'secret'))
    pass
