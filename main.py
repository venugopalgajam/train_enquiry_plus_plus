
import datetime as dt
import logging

from flask import Flask, render_template, request, redirect, url_for

from rendering_lib import *
from tepp import get_paths

app = Flask(__name__)

@app.route('/enquiry.html')
def enquiry():
    return render_template('enquiry.html')
@app.route('/favicon.ico')
def favicon():
    return render_template('train_ico.png')

@app.route('/')
def index():
    return redirect(url_for('enquiry'))

@app.route('/service.html')
def service():
    return render_template('service.html')

@app.route('/get_paths.html',methods=['GET'])
def get_paths_html():
    src = str(request.args.get('src','')).split('-')[-1]
    dst = str(request.args.get('dst','')).split('-')[-1]
    date = str(request.args.get('jdate','')).split('-')
    jdate=dt.datetime(int(date[0]),int(date[1]),int(date[2]))
    # print(src,dst,jdate)# pylint: disable=E1601
    trains_details = get_paths(src,dst,jdate,False)# pylint: disable=E1601
    responce_html =''
    if 'direct' in trains_details:
        results = render_direct_trains_row(trains_details['direct'],src,dst,jdate)
        # print(results)# pylint: disable=E1601
        responce_html+= str(open('./templates/direct_train_table.html').read()).replace('{{tbody}}',results)

    if 'one_stop' in trains_details:
        results = render_one_stop_row(trains_details['one_stop'],src, dst, jdate)
        # print(results)# pylint: disable=E1601
        responce_html+=str(open('./templates/one_stop_table.html').read()).replace('{{tbody}}',results)
    return responce_html
@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500

# [END form]

# @app.route('/station_list.js',methods=['GET'])
# app.get('/station_list.js', function(req, res) {
# 	res.render('station_list.js');
# });
# [START submitted]
# @app.route('/submitted', methods=['POST'])
# def submitted_form():
#     name = request.form['name']
#     email = request.form['email']
#     site = request.form['site_url']
#     comments = request.form['comments']

#     # [END submitted]
#     # [START render_template]
#     return render_template(
#         'submitted_form.html',
#         name=name,
#         email=email,
#         site=site,
#         comments=comments)
#     # [END render_template]


# [END app]
