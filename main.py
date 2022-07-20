from flask import Flask, render_template
from flask_moment import Moment
from flask_uploads import configure_uploads, IMAGES, UploadSet
from flask_bootstrap import Bootstrap
import os
import uuid
from form import PaletteForm
from color_extractor import color_extractor

app = Flask(__name__)
Bootstrap(app)

# Date in footer
moment = Moment(app)

# Form security
app.config['SECRET_KEY'] = os.urandom(24)

# File upload setting
app.config['UPLOADED_IMAGES_DEST'] = 'static/images/'
images = UploadSet('images', IMAGES)
configure_uploads(app, images)

sample_image_directory = 'static/images/sample-image.jpg'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PaletteForm()
    if form.validate_on_submit():
        if form.image.data:
            image_name = images.save(form.image.data, name=str(uuid.uuid4())[:8] + '.')
            image_directory = f"{app.config['UPLOADED_IMAGES_DEST']}{image_name}"
            number = form.number.data
            result = color_extractor(number, image_directory)
            return render_template('index.html', form=form, submit=True,
                                   image_directory=image_directory, result=result)
        else:
            number = form.number.data
            result = color_extractor(number, sample_image_directory)
            return render_template('index.html', form=form, submit=True,
                                   image_directory=sample_image_directory, result=result)
    return render_template('index.html', form=form, submit=False, image_directory=sample_image_directory)


if __name__ == '__main__':
    app.run(host='0.0.0.0'
                 '', port=8080)
