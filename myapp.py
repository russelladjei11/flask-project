from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def index():
        return render_template("index.html")
@app.route('/mylinux')

def mylinux():
       return render_template('linux.html')

@app.route('/mypython')
def mypython():
        return render_template('python.html')

@app.route('/whereami')
def whereami():
        return "Kdua"


if __name__ == '__main__':
       app.run(host="0.0.0.0")


