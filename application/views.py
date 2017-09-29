from flask import render_template, flash, request, redirect, logging
from qrcode_generator import generate_qrcode, generate_qrcode_batch_csv
# imports app variable from application package
from .form import QRForm, QRBatchForm, LoginForm
from werkzeug.utils import secure_filename
from application import app


# two forms on the same page ref:
# https://stackoverflow.com/questions/21949452/wtforms-two-forms-on-the-same-page


@app.route('/onetime', methods=['GET', 'POST'])
def onetime():
    onetime_form = QRForm(request.form)

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
    batch_form = QRBatchForm(request.form)

    if batch_form.validate_on_submit():
        inputfile = 'sample.csv'
        # inputfile = secure_filename(batch_form.inputfile.data.filename)
        app.logger.info(inputfile)

        # batch_form.inputfile.data.save('uploads/' + inputfile)

        if inputfile:
            qrBatchJsonResponse = generate_qrcode_batch_csv('uploads/' + inputfile)
            app.logger.info(qrBatchJsonResponse)
            flash('You requested Batch QR codes for: %s' % 'uploads/' + inputfile)
            # app.logger.info(form.qrtext.data)
            # app.logger.info(responseURL)
            return render_template('batch.html',
                               rform=batch_form,
                               qrBatchJsonResponse=qrBatchJsonResponse
                                   )

    return render_template('batch.html',
                           rform=batch_form,
                           )


@app.route('/login', methods=['GET', 'POST'])
def login():
    # logger = logging.create_logger(app)
    # logger.setLevel('INFO')

    login_form = LoginForm(request.form)
    # flash('Congrats!')

    if login_form.validate_on_submit():
        # responseURL = generate_qrcode(onetime_form.qrtext.data)
        flash('Congrats! You have logged in as : "%s"' % login_form.username.data)
        # app.logger.info(form.qrtext.data)
        # app.logger.info(responseURL)

        # return redirect('/index')

        return render_template('login.html',
                               loginform=login_form  # lform > form on the left
                               # responseURL=responseURL
                               )
    return render_template('login.html',
                           loginform=login_form  # lform > form on the left
                           )
@app.route('/')
@app.route('/index')
def index():

    # return redirect('/login.html')
    # login_form = LoginForm()
    return render_template('index.html')

    # return render_template('login.html',
    #                        loginform=login_form  # lform > form on the left
    #                        )