# dependencies
from flask import Flask, jsonify
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# create engine
path = 'Resources/hawaii.sqlite'
engine = create_engine(f'sqlite:///{path}')

# reflect database into model
Base = automap_base()

# reflect tables
Base.prepare(engine, reflect=True)

# save references to tables
Station = Base.classes.station
Measurement = Base.classes.measurement

# create session from Python to the DB
session = Session(engine)

# create app
app = Flask(__name__)

# set routes
@app.route('/')
# show available routes on homepage
def home():
    return (             
        f'Hello! Here is the list of available routes:<br/>'
        f'/api/v1.0/precipitation<br/>'
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/start<br/>'
        f'/api/v1.0/start/end<br/><br/>'
        f'Note: for the last two endpoints, replace start and end with dates in YYYY-MM-DD format'
        )
    
@app.route('/api/v1.0/precipitation')
def precipitation():
    prcp = session.query(Measurement.date, Measurement.prcp).all()
    prcp_list = [{x.date: x.prcp} for x in prcp]
    
    return jsonify(prcp_list)    
    
@app.route('/api/v1.0/stations')
def stations():
    stations = session.query(Station.station).all()
    station_list = [x.station for x in stations]
    
    return jsonify(station_list)

@app.route('/api/v1.0/tobs')
def tobs():
    max_station = session.query(Measurement.station).\
        group_by(Measurement.station).\
        order_by(func.count(Measurement.station).desc()).first()['station']
    
    max_date_str = session.query(Measurement.date).order_by(Measurement.date.desc()).first()['date']
    max_date = dt.datetime.strptime(max_date_str, '%Y-%m-%d')
    start_date = max_date - dt.timedelta(365)
    
    temps = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == max_station).\
        filter(Measurement.date >= start_date).\
        order_by(Measurement.date).all()
    
    temp_list = [{x.date: x.tobs} for x in temps]
        
    return jsonify(temp_list)

# @app.route('/api/v1.0/<start>')
# def start():
#     # code here
    
# @app.route('/api/v1.0/<start>/<end>')
# def start_and_end():
#     # code here

if __name__ == '__main__':
    app.run(debug=True)