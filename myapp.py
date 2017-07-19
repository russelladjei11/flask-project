from flask import Flask, render_template, send_from_directory
import os
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("moorhouseassociates.com", 1883, 60)

app= Flask(__name__)

@app.route('/')
def index():
        return render_template("index.html" , to="Sam Moorhouse")


@app.route('/btn')
def btn():
	print("button clicked")
	client.publish("test/all", "this is my message to you")
	return ""

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img',path)

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


