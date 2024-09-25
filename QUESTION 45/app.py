from flask import Flask, render_template, redirect, url_for
from forms import MyForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Required for CSRF protection

@app.route('/', methods=['GET', 'POST'])
def home():
    form = MyForm()
    if form.validate_on_submit():
        # Process the form data here
        name = form.name.data
        email = form.email.data
        return redirect(url_for('success'))
    return render_template('home.html', form=form)

@app.route('/success')
def success():
    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
