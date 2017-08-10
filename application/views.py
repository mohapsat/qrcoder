from flask import render_template, flash, redirect, json
from application import app
# imports app variable from application package
from .form import QRForm
from qrcode_generator import generate_qrcode


# @app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():

    form = QRForm()

    if form.validate_on_submit():
        responseURL = generate_qrcode(form.qrtext.data)
        flash('You requested QR code for: "%s"' % form.qrtext.data)
        # app.logger.info(form.qrtext.data)
        # app.logger.info(responseURL)

        # return redirect('/index')
        return render_template('index.html',
                               form=form,
                               responseURL=responseURL
                               )

    return render_template('index.html',
                           form=form
                           )
