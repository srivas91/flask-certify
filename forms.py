from flask_wtf import Form
from wtforms import validators, ValidationError
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField


class SignUpForm(Form):
    name = StringField("Candidate Name")
    Address = TextAreaField("Address")
    email = StringField("Email")
    skill = SelectField('Your Skill', choices=[('excel', 'Excel'), ('py', 'Python'), ('draw', 'Draw')])
    submit = SubmitField("Submit")

