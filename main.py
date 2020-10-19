from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/dontC')
def dontC():
    return render_template('dontcare.html')

@app.route('/chattingP')
def chattingP():
    return render_template('chattingP.html')

@app.route("/PostMsg", methods=["POST"])
def PostMsg():
    return "This is post metode!"

@app.route("/info", methods=["GET","POST"])
def info():
    if request.method == "GET":
        vards = request.args.get("vards")
        uzvards = request.args.get("uzvards")
        return f"Esi sveiks {vards} {uzvards}"
    elif request.method == "POST":
        if request.content_type == "application/json":
            dati = request.json
            print(dati)
            return f"This is POST method with type {request.content_type}"
        else:
            return f"This content type is not allowed {request.content_type}"
    else:
        return "Method unknown"

app.run(host='0.0.0.0', port=80, debug=True)

