from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('core/index.html')

@app.route('/form',methods=['GET','POST'] )
def form():
    if request.method=='POST':
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        with open('form_data.csv', 'a') as f:
            f.write(f'{name.strip()}, {email.strip()}, {message.strip()}\n')

        return render_template('core/formsubmit.html')
    return render_template('core/form.html')

@app.route('/about')
def about():
    return render_template('core/about.html')

@app.route('/tnc')
def tnc():
    return render_template('core/tnc.html')

@app.route('/privacy')
def privacy():
    return render_template('core/privacy.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)