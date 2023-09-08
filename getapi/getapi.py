from flask import Flask, jsonify

app = Flask(__name__)

courses = [{'name': 'python', 'course_id': '1', 'price': 500}, {'name': 'Java', 'course_id': '2', 'price': 5000},
           {'name': 'c', 'course_id': '3', 'price': 1000}]

@ app.route('/')
def index():
    return "welcome to the course api"




@app.route('/courses', methods=['GET'])
def get():
    return jsonify({'courses': courses})


@app.route('/courses/<int:course_id>', methods = ['GET'])
def get_course(course_id):
    return jsonify({'course':courses[course_id]})

if __name__=="__main__":
    app.run(debug=True)
