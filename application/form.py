from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class QRForm(FlaskForm):
    qrtext = StringField('Enter text or URL', validators=[DataRequired()])


class QRBatchForm(FlaskForm):
    qr_csvfileinput = StringField('File Input')
