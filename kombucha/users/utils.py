import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from kombucha import mail



#we must rename the photo so it doesnt create problems
def save_picture(form_picture):
    #8 is the number of bites returned
    random_hex = secrets.token_hex(8)
    #gets the file name nad the file ext, in this situation only f_ext is used. Use _ for unused variables
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    #os.path.join joins the file location, app.root_path finds (ie C:/Programs/..), static is the next folder
    #and picture_fn is the file we are looking for. 
    picture_path = os.path.join(current_app.root_path, 'static' , picture_fn)
    
    output_size = (300, 300)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    
    #Delete the previous profile pic
    prev_picture = os.path.join(app.root_path, 'static', current_user.image_file)
    if os.path.exists(prev_picture) and os.path.basename(prev_picture) != 'default.jpg':
        os.remove(prev_picture)

    
    return picture_fn

#send email
def send_reset_email(user):
    token = user.get_reset_token()
    #'Password Reset' is the email subject
    msg = Message('Password Reset', sender='noreply.kombuchajournal@gmail.com', recipients=[user.email])
    #link in the email needs to have the full domain name, which is why external is true.
    msg.body=f'''To reset password go to:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request, ignore this message
'''
    mail.send(msg)
