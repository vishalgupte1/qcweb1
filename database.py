from flask import jsonify
from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STR']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_colors_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from colors"))
   
    colors_list = []
    for row in result:
      colors_dict = {'ID': row[0], 'COLOR_ID':row[1], 'COLOR_NAME':row[2]}
      colors_list.append(colors_dict)
    return colors_list


def load_color_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from colors where ID = :val"),
                          {"val": id})
    rows = result.mappings().all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])

'''
with engine.connect() as conn:
  results = conn.execute(text("select * from colors"))
  #results_as_dict = results.mappings().all()
  #print(type(results_as_dict))
  print(type(results))
  print(results.all())
  #rows = results.mappings()
  #print(rows)

  #query = "select * from colors"
  #results = conn.execute(text("select * from colors")).fetchall()
  #dict_result = [dict(row) for row in results]
  #jsonify(results)
  #colors = results.mappings().all()
  #print(type(colors))
  '''
