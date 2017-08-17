from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
    # for file upload ref: https://flask-wtf.readthedocs.io/en/latest/form.html#module-flask_wtf.file
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



class QRForm(FlaskForm):
    qrtext = StringField('Enter text or URL', validators=[DataRequired()])
    submit = SubmitField('Generate QR Code')

class QRBatchForm(FlaskForm):
    csvfileinput = FileField()
