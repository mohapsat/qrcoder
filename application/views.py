from flask import render_template, flash, redirect, json
from application import app
# imports app variable from application package
from .form import QRForm, QRBatchForm
from qrcode_generator import generate_qrcode, generate_qrcode_batch_csv


# @app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():

    form = QRForm()
    batchform = QRBatchForm()

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

    if batchform.validate_on_submit():
        inputFile = 'qr_fileinput.csv'
        app.logger.info(inputFile)
        qrBatchJsonResponse = generate_qrcode_batch_csv(inputFile)
        app.logger.info(qrBatchJsonResponse)
        flash('You requested Batch QR codes for: "%s"' % inputFile)
        # app.logger.info(form.qrtext.data)
        # app.logger.info(responseURL)

        # return redirect('/index')
        return render_template('index.html',
                               batchform=batchform,
                               qrBatchJsonResponse=qrBatchJsonResponse
                               )

    return render_template('index.html',
                           form=form
                           # batchform=batchform
                           )