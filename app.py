from flask import Flask, request, render_template

app = Flask(__name__)

''' 
4 main pages
'''

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/career', methods=['GET'])
def career():
    return render_template('career.html')

@app.route('/hobbies', methods=['GET'])
def hobbies():
    return render_template('hobbies.html')

@app.route('/travel', methods=['GET'])
def interests():
    return render_template('travel.html')

''' 
Resume page
'''

@app.route('/resume', methods=['GET'])
def resume():
    return render_template('resume.html')

''' 
Picture gallery pages.
'''

@app.route('/hobbies_sewing', methods=['GET'])
def sew_pics():
    return render_template('sew_pics.html')

@app.route('/hobbies_embroidery', methods=['GET'])
def emb_pics():
    return render_template('emb_pics.html')

@app.route('/hobbies_vinyl', methods=['GET'])
def vinyl_pics():
    return render_template('vinyl_pics.html')

@app.route('/hobbies_crochet', methods=['GET'])
def crochet_pics():
    return render_template('crochet_pics.html')

@app.route('/hobbies_baking', methods=['GET'])
def baking_pics():
    return render_template('baking_pics.html')

@app.route('/hobbies_misc', methods=['GET'])
def misc_pics():
    return render_template('misc_pics.html')

# @app.route('/pets', methods=['GET'])
# def pets():
#     return render_template('petsitting.html')

if __name__ == '__main__':
    app.run(debug=True)
