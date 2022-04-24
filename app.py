from forms import SignUpForm
from flask import Flask,render_template,request

app = Flask(__name__)
app.secret_key = '356dbgjw0478983ndjkgsygyuf'

@app.route('/')
def home():
    return "Home page"

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    return render_template('contact.html', form=form)

@app.route('/success', methods=['GET', 'POST'])
def success():
    form = SignUpForm()
    if request.method=="POST":
        print("Candidate Name:",form.name.data)
        print("Address:",form.Address.data)
        print("Email:",form.email.data)
        print("Skills:",form.skill.data)
        return render_template("success.html")

if __name__ == '__main__':
    app.run(debug=True)

