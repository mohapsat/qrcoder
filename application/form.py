from flask_wtf import FlaskForm
from flask_wtf.file import FileField
# for file upload ref: https://flask-wtf.readthedocs.io/en/latest/form.html#module-flask_wtf.file
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired



class QRForm(FlaskForm):
    qrtext = StringField('Enter text or URL', validators=[DataRequired()])
    submit = SubmitField('Generate QR Code')

class QRBatchForm(FlaskForm):
    inputfile = FileField()
    submit = SubmitField('Generate Batch Codes')

class LoginForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired])
    password = PasswordField('Password')
    submit = SubmitField('Log In')
