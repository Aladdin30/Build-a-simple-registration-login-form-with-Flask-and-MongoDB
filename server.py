from flask import Flask,render_template,session,request,url_for,redirect
import pymongo
import bcrypt


app=Flask(__name__)
app.secret_key="testing"

myclient= pymongo.MongoClient("mongodb://localhost:27017")
db=myclient["login"]
coll=db['user']

print(myclient.list_database_names())
print(db.list_collection_names())

@app.route("/",methods=['post','get'])
def index():
    massage=""
    if "email" in session:
        return redirect(url_for("logged_in"))
    if request.method== "POST":
        username=request.form.get("fullname")
        email=request.form.get("email")
        password1=request.form.get("password1")
        password2=request.form.get("password2")
        
        user_found=coll.find_one({"username" : username})
        email_found=coll.find_one({"email" : email})
        
        if user_found:
            massage="this username  is already used before"
            return render_template("index.html",massage=massage)
        if email_found:
            massage="this email is already used before"
            return render_template("index.html",massage=massage)
        if password1 != password2:
            massage="password should matched!"
            return render_template("index.html",massage=massage)
        else:
            haspass=bcrypt.hashpw(password2.encode("utf-8"),bcrypt.gensalt())
            user_input={"name":username,"email":email,"password":haspass}
            coll.insert_one(user_input)
            
            user_data=coll.find_one({"email":email})
            new_email=user_data['email']
            return render_template("logged_in.html",email=new_email)
    return render_template('index.html')

@app.route("/login",methods=['post','get'])
def login():
    message='please enter your email and password '
    if "email" in session:
        return redirect(url_for("logged_in"))
    if request.method==['post']:
        email=request.form.get("email")
        password=request.form.get("password")
        
        email_found=coll.find_one({"email":email})
        if email_found:
            email_val=email_found['email']
            password_check=email_found['password']
            
            if bcrypt.checkpw(password.encode("utf-8"),password_check):
                session['email']=email_val
                return redirect(url_for('logged_in'))
            else:
                if "email" in session:
                    return redirect(url_for("logged_in"))
                message="wrong password!!"
                return render_template("login.html",message=message)
        else:
            message="email not found !!"
            return render_template("login.html",message=message)
    return render_template("login.html",message=message)

@app.route("/logged_in")
def logged_in():
    if "email" in session:
        email=session['email']
        return render_template("logged_in.html",email=email)
    else:
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    if "email" in session:
        session.pop['email']
        return render_template("signout.html")
    else:
        return render_template("index.html")
    
if __name__==("__main__"):
    app.run(debug=True,port=5000)
