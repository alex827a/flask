from flask import Flask,render_template,jsonify

app = Flask(__name__)
JOBS=[
    {
    'id':1,
    'title':'Data Analyst',
    'location':'Kharkiv Ukraine',
    'salary':'1000$'
    },
    {
    'id':2,
    'title':'Data Scietist',
    'location':'Kyiv Ukraine',
    
    },
    {
    'id':3,
    'title':'Data Enginer',
    'location':'Dnipro Ukraine',
    'salary':'5000$'
    }
]

@app.route("/")
def hello_world():
    return render_template('main.html',jobs=JOBS)
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
if __name__ == "__main__":
    app.run(debug=True)