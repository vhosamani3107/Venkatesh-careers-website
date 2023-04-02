from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS= [
    {
        'id' : 1,
        'title' : 'Data analyst',
        'location' : 'Bengalore',
        'Salary' : 100000
    },
     {
        'id' : 2,
        'title' : 'Mainframes',
        'location' : 'Bengalore',
        'Salary' : 1000000
    },
     {
        'id' : 3,
        'title' : 'Java',
        'location' : 'Bengalore',
        'Salary' : 150000
    }
]
@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS)


@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)