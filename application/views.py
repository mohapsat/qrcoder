from flask import render_template, flash, request

from application import app
from qrcode_generator import generate_qrcode, generate_qrcode_batch_csv
# imports app variable from application package
from .form import QRForm, QRBatchForm


# two forms on the same page ref:
# https://stackoverflow.com/questions/21949452/wtforms-two-forms-on-the-same-page

# @app.route('/')
@app.route('/onetime', methods=['GET', 'POST'])
def onetime():
    onetime_form = QRForm(request.form, prefix="onetime-form")

    if onetime_form.validate_on_submit():
        responseURL = generate_qrcode(onetime_form.qrtext.data)
        flash('You requested QR code for: "%s"' % onetime_form.qrtext.data)
        # app.logger.info(form.qrtext.data)
        # app.logger.info(responseURL)

        # return redirect('/index')

        return render_template('onetime.html',
                               lform=onetime_form,  # lform > form on the left
                               responseURL=responseURL
                               )
    return render_template('onetime.html',
                           lform=onetime_form,  # lform > form on the left
                           )


@app.route('/batch', methods=['GET', 'POST'])
def batch():
    batch_form = QRBatchForm(request.form, prefix="batch-form")

    if batch_form.validate_on_submit():
        inputFile = batch_form.csvfileinput.data
        app.logger.info(inputFile)
        qrBatchJsonResponse = generate_qrcode_batch_csv(inputFile)
        app.logger.info(qrBatchJsonResponse)
        flash('You requested Batch QR codes for: "%s"' % inputFile)
        # app.logger.info(form.qrtext.data)
        # app.logger.info(responseURL)

        # return redirect('/index')
        return render_template('batch.html',
                               rform=batch_form,
                               qrBatchJsonResponse=qrBatchJsonResponse
                               )
    return render_template('batch.html',
                           rform=batch_form,
                           )


@app.route('/index')
def index():
    return render_template('index.html')
