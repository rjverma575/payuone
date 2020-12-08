from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
import logging, traceback
import checkout.constants as constants
import checkout.config as config
import hashlib
import requests
from random import randint
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'checkout/home.html')

def payment(request):


    data = {}
    txnid = get_transaction_id()
    hash_ = generate_hash(request, txnid)
    hash_string = get_hash_string(request, txnid)
    # use constants file to store constant values.
    # use test URL for testing
    data["action"] = constants.PAYMENT_URL_LIVE 
    data["amount"] = float(constants.PAID_FEE_AMOUNT)
    data["productinfo"]  = constants.PAID_FEE_PRODUCT_INFO
    data["key"] = config.KEY
    data["txnid"] = txnid
    data["hash"] = hash_
    data["hash_string"] = hash_string
    data["firstname"] = request.session["student_user"]["name"]
    data["email"] = request.session["student_user"]["email"]
    data["phone"] = request.session["student_user"]["mobile"]
    data["service_provider"] = constants.SERVICE_PROVIDER
    data["furl"] = request.build_absolute_uri(reverse("students:payment_failure"))
    data["surl"] = request.build_absolute_uri(reverse("students:payment_success"))
    return render(request, 'checkout/payment.html', data)    


# generate the hash
def generate_hash(request, txnid):
        # get keys and SALT from dashboard once account is created.
        # hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
        hash_string = get_hash_string(request,txnid)
        generated_hash = hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()
        return generated_hash
    

# create hash string using all the fields
def get_hash_string(request, txnid):
    hash_string = config.KEY+"|"+txnid+"|"+str(float(constants.PAID_FEE_AMOUNT))+"|"+constants.PAID_FEE_PRODUCT_INFO+"|"
    hash_string += request.session["student_user"]["name"]+"|"+request.session["student_user"]["email"]+"|"
    hash_string += "||||||||||"+config.SALT

    return hash_string

# generate a random transaction Id.
def get_transaction_id():
    hash_object = hashlib.sha256(str(randint(0,9999)).encode("utf-8"))
    # take approprite length
    txnid = hash_object.hexdigest().lower()[0:32]
    return txnid

# no csrf token require to go to Success page. 
# This page displays the success/confirmation message to user indicating the completion of transaction.
@csrf_exempt
def payment_success(request):
    data = {}
    return render(request, "checkout/success.html", data)

# no csrf token require to go to Failure page. This page displays the message and reason of failure.
@csrf_exempt
def payment_failure(request):
    data = {}
    return render(request, "checkout/failure.html", data)    