from flask import Flask, render_template

app = Flask(__name__)

# Make sure all your routes return static-friendly content
@app.route('/')
def index():
    return render_template('index.html')

# Add other routes...

# Add this if your site is not at the root of the domain
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'build'

if __name__ == '__main__':
    app.run(debug=True)
