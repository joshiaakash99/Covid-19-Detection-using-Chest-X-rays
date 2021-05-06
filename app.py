
from flask import Flask, render_template, request, session, redirect, url_for, flash,session
import os

from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model, model_from_json
import matplotlib.pyplot as plt
import cv2
import numpy as np
import mysql.connector




UPLOAD_FOLDER = './flask app/assets/images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__,static_url_path='/assets',
            static_folder='./flask app/assets', 
            template_folder='./flask app')
app.secret_key = os.urandom(24)

conn = mysql.connector.connect(host="remotemysql.com", user = "76agGTNkF5", password = "s9YU0REnhs" , database = "76agGTNkF5")
cursor = conn.cursor()
json_file = open('models/model.json','r')
loaded_model_json = json_file.read()
json_file.close()
# use Keras model_from_json to make a loaded model
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("models/inceptionv3_chest.h5")

# print("Loaded Model from disk")
# compile and evaluate loaded model

loaded_model.compile(
        loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy']
)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def login():
   return render_template('login.html')

@app.route('/register')
def register():
   return render_template('register.html')

@app.route('/login_validation',methods = ['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')
    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
    users = cursor.fetchall()
    print(users)
    if len(users)>0:
        session['user_id'] = users[0][0]
        return redirect('/index.html')
    else:
        return redirect('/')

@app.route('/add_user', methods = ['POST'])
def add_user():
    name = request.form.get('uname')
    email = request.form.get('uemail')
    password = request.form.get('upassword')
    cursor.execute("""INSERT INTO `users` (`user_id`,`name`,`email`,`password`) VALUES(NULL,'{}','{}','{}')""".format(name,email,password))
    conn.commit()
    return redirect('/')

@app.route('/index.html')
def index():
    if 'user_id' in session:
        return render_template('index.html')
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')

@app.route('/contact.html')
def contact():
   return render_template('contact.html')

@app.route('/news.html')
def news():
   return render_template('news.html')

@app.route('/about.html')
def about():
    if 'user_id' in session:
        return render_template('about.html')
    else:
        return redirect('/')

@app.route('/faqs.html')
def faqs():
   return render_template('faqs.html')

@app.route('/prevention.html')
def prevention():
   return render_template('prevention.html')

@app.route('/upload.html')
def upload():
    if 'user_id' in session:
        return render_template('upload.html')
    else:
        return redirect('/')

@app.route('/upload_chest.html')
def upload_chest():
    if 'user_id' in session:
        return render_template('upload_chest.html')
    else:
        return redirect('/')


@app.route('/upload_ct.html')
def upload_ct():
   return render_template('upload_ct.html')

@app.route('/uploaded_chest', methods = ['POST', 'GET'])
def uploaded_chest():
   if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            # filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

   #inception_chest = load_model('models/inceptionv3_chest.h5')


   image = cv2.imread('./flask app/assets/images/'+file.filename) # read file
   image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # arrange format as per keras
   image = cv2.resize(image,(224,224))
   image = np.array(image) / 255
   image = np.expand_dims(image, axis=0)



   inception_pred = loaded_model.predict(image)
   probability = inception_pred[0]
   print("Inception Predictions:")
   if probability[0] > 0.5:
      inception_chest_pred = str('%.2f' % (probability[0]*100) + '% COVID')
   else:
      inception_chest_pred = str('%.2f' % ((1-probability[0])*100) + '% NonCOVID')
   print(inception_chest_pred)



   return render_template('results_chest.html',inception_chest_pred=inception_chest_pred)



if __name__ == '__main__':
   app.secret_key = ".."
   app.run(debug = True)