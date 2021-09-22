import BlocksDatabase
import TransactionDatabase
import MinerCode
import Registration
import Blacklisting
import textTransaction
import balance
import flask
import threading
import sqlite3
import flash
from flask import flash,redirect,url_for,session


hosting = flask.Flask(__name__)
hosting.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # all the session data is encrypted in the server so we need a secret key to encrypt and decrypt the data

@hosting.route("/",methods = ["GET","POST"])
def register():
    if flask.request.method == "POST":
        # gets the parameter form the form in index.html
        Name = flask.request.form.get("Aname")
        Password = flask.request.form.get("pass")
        ContactNumber = flask.request.form.get("Cnumber")
        Email = flask.request.form.get("email")    
        AadharNumber = flask.request.form.get("aadhar")
        PanNumber = flask.request.form.get("pan")
        Passport = flask.request.form.get("passport")
        public = 1234

        # appending to all parameters in message
        message = str(Name)+ "-"+str(Password)+"-"+str(ContactNumber)+"-"+str(Email)+"-"+str(AadharNumber)+"-"+str(PanNumber)+"-"+str(Passport)+"-"+str(public)
        
        # creates new account
        Registration.createAccount(message)

        # displaying the registration table
        Registration.Display()

        # appending name and email to value parameter 
        value = Name+"-"+Email

        # creating record of the registered account in balance table
        balance.first(value)
        
        # flashing message in html form 
        flash('Registered Successfully!')

        # redirecting to login page
        return redirect(url_for("signin"))
        
    return flask.render_template("index.html")

@hosting.route("/sign",methods = ["GET","POST"])
def signin():
    if flask.request.method == "POST":
        # gets the parameter form the form in index.html
        Email = flask.request.form.get("email")
        Password = flask.request.form.get("pass")

        # validation of the credentials entered
        checkResponse = Registration.signIn(Email,Password)

        # checking if the credentials are valid or not
        if checkResponse == True:
            flask.session["UserId"] = Email # creating a session of the email id
            return flask.redirect(url_for("displaydash")) # redirecting to dashboard
        else: 
            return "Wrong Credentials"

    return flask.render_template("index.html")

@hosting.route("/dashboard",methods = ["GET","POST"])
def displaydash(): 
    if flask.request.method == "POST":
        pass

    # /dashboard should be visible only if the user has logged in. Hence checking if the session varibale has value or not 
    if "UserId" not in flask.session:
        return flask.redirect(url_for("signin")) # If user tries to bypass to next route then it will display login page only

    # redirecting to dashboard
    return flask.render_template("dashboard.html")

@hosting.route("/profile",methods = ["GET","POST"])
def pageProfile():
    # /profile should be visible only if the user has logged in. Hence checking if the session varibale has value or not 
    if "UserId" not in flask.session:
        return flask.redirect(url_for("signin")) # If user tries to bypass to next route then it will display login page only

    # gets the Registration database
    data = Registration.Display()
    
    # to display content of the logged in user
    for i in data:
        if i[3]==flask.session["UserId"]: # finding the record of the logged in user
            return flask.render_template("profile page.html",Name=str(i[0]),email=i[3],aadhar=i[4],pan=i[5],passport=i[6],password=i[1],contact=i[2])
    
    return flask.redirect(url_for("signin"))
    # return ('Error')

@hosting.route("/wallet",methods = ["GET","POST"])
def walletpage():
    # /wallet should be visible only if the user has logged in 
    if "UserId" not in flask.session:
        return flask.redirect(url_for("signin")) # If user tries to bypass to next route then it will display login page only
    
    email = flask.session["UserId"]
    
    data = balance.display() # gets the Balance database
    # Data1 = list(data[0])

    value = balance.getbalance(str(email))
    value2 = list(value[0])
    return flask.render_template("wallet.html",Name=value2[0],Balance=value2[1])
    

@hosting.route("/sendtransation",methods = ["GET","POST"])
def sendtransaction():
    # /sendtransaction should be visible only if the user has logged in 
    if "UserId" not in flask.session:
        return flask.redirect(url_for("signin"))

    if flask.request.method == "POST":
        # gets the parameter form the form in wallet.html
        payeeemail = flask.request.form.get("payeeemail")
        amount = flask.request.form.get("value")


        email = flask.session["UserId"]

        value1 = balance.getbalance(str(email))
        value2 = balance.getbalance(str(payeeemail))

        # formatting the parameters in message in the given format
        # payer payervalue payee payeevalue amounttransacted
        message = email + " " + value1[0][1] + " " + payeeemail + " " + value2[0][1] + " " + amount

        # checking if the payeeemail is a blacklisted account or not
        if Blacklisting.checkBlacklist(str(payeeemail))==False:
            if Blacklisting.checkBlacklist(str(email))==False:
                print("!!   This account has NOT BLACKLISTED and TRANSACTION will be processed  !!")
                balance.transact(message)
            else:
                flash(f"{email} has been BLACKLISTED!!")
                print(f"{payeeemail} has been BLACKLISTED!!")
        else:
            print(f"{payeeemail} has been BLACKLISTED!!")
        
        # displaying the balance database
        balancedata = balance.display()
        
        return flask.redirect(url_for("walletpage"))

@hosting.route("/report",methods = ["GET","POST"])
def reportpage():
    # /report should be visible only if the user has logged in 
    if "UserId" not in flask.session:
        return flask.redirect(url_for("signin"))
    
    email = flask.session["UserId"]
    fraudMailId = flask.request.form.get("fraudMailId") # gets the reported maid id from the transaction.html

    con = sqlite3.connect("TransactionData1.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from TransactionsInfo WHERE Sender = '{}'".format(str(email)))
    rows = cur.fetchall()
    con.commit()
    con.close()

    if fraudMailId !=None:
        print("----------------------------------------------------------------------------------------------")
        Blacklisting.trace(str(fraudMailId))
        print("----------------------------------------------------------------------------------------------")
        flash("Your Complaint has been reported")
        #return("Your Complaint has been reported")

    return flask.render_template("Transaction History.html", rows=rows)

@hosting.route("/logout",methods = ["GET","POST"])
def logout():
    flask.session.pop("UserId",None) # removing email from session variable
    return redirect(url_for("signin")) # redirecting to login page

if __name__ == "__main__":
    hosting.run(debug=True)
