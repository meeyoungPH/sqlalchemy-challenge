# dependencies
from flask import Flask

# create app
app = Flask(__name__)

# set routes
@app.route('/')
def home():
    '''Hello! Here is the list of available routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/<start>
    /api/v1.0/<start>/<end>'''
    
@app.route('/api/v1.0/preciptation')
def precipitation():
    # code here
    
@app.route('/api/v1.0/stations')
def stations():
    # code here

@app.route('api/v1.0/tobs')
def tobs():
    # code here

@app.route('/api/v1.0/<start>')
def start():
    # code here
    
@app.route('/api/v1.0/<start>/<end>')
def start_and_end():
    # code here

if __name__ == '__main__':
    app.run(debug=True)