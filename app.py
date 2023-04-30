from flask import Flask, render_template, jsonify
from database import load_colors_from_db, load_color_from_db

'''
check git function 1
'''

app = Flask(__name__)


@app.route("/")
def hello_app():
  colors = load_colors_from_db()
  return render_template('home.html',
                         colors = colors,
                         company_name='Polycoat')


@app.route("/api/colors")
def list_colors():
  colors = load_colors_from_db()
  #return json.dumps(colors)  
  #return jsonify(colors)
  return jsonify(colors)
  

@app.route('/color/<int:id>')
def show_color(id):
  color = load_color_from_db(id)
  return jsonify(color)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

