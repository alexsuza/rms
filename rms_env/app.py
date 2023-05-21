from flask import Flask, template_rendered
app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)

@app.route('/')
def index():
    return '<h1> New Test </h1>'




@app.route('/about/<username>')
def about_page(username):
    return f'<h1> This is the about page of {username}</h1>'