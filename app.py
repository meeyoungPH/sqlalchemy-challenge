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
    
    # create session from Python to the DB
    session = Session(engine)
    
    # query for all precipitation observations by date
    prcp = session.query(Measurement.date, Measurement.prcp).all()
    
    # close session
    session.close()
    
    # create list and return as JSON
    prcp_list = [{x.date: x.prcp} for x in prcp]    
    return jsonify(prcp_list)    
    
@app.route('/api/v1.0/stations')
def stations():    
    
    # create session from Python to the DB
    session = Session(engine)
    
    # query for stations
    stations = session.query(Station.station).all()
    
    # close session
    session.close()
    
    # create list and return as JSON
    station_list = [x.station for x in stations]
    return jsonify(station_list)

@app.route('/api/v1.0/tobs')
# return JSON for all temperature observations in the past year for the most active station
def tobs():
    
    # create session from Python to the DB
    session = Session(engine)
    
    # identify most active station by count of records
    max_station = session.query(Measurement.station).\
        group_by(Measurement.station).\
        order_by(func.count(Measurement.station).desc()).first()['station']
    
    # determine start date based on max date of observations
    max_date_str = session.query(Measurement.date).order_by(Measurement.date.desc()).first()['date']
    max_date = dt.datetime.strptime(max_date_str, '%Y-%m-%d')
    start_date = max_date - dt.timedelta(365)
    
    # query by station and start date
    temps = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == max_station).\
        filter(Measurement.date >= start_date).\
        order_by(Measurement.date).all()
    
    # close session
    session.close()
    
    # create list and return as JSON
    temp_list = [{x.date: x.tobs} for x in temps]
    return jsonify(temp_list)

@app.route('/api/v1.0/<start>')
def start(start):
    # capture start date from endpoint and convert to datetime format
    start_str = start
    start_dt = dt.datetime.strptime(start_str, '%Y-%m-%d') - dt.timedelta(1)

    # create session from Python to the DB
    session = Session(engine)

    # query to summarize temperature data filtered by start date   
    temps = session.query(func.min(Measurement.tobs).label('min'),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_dt).one()
        
    # close session
    session.close()
    
    # create list and return as JSON
    temp_summary = [
        {'min':temps[0],
        'avg':temps[1],
        'max':temps[2]
        }
    ]
    return jsonify(temp_summary)
    
@app.route('/api/v1.0/<start>/<end>')
def start_and_end(start, end):
    # capture start and end dates from endpoint and convert to datetime format
    start_str = start
    end_str = end
    start_dt = dt.datetime.strptime(start_str, '%Y-%m-%d') - dt.timedelta(1)
    end_dt = dt.datetime.strptime(end_str, '%Y-%m-%d')

    # create session from Python to the DB
    session = Session(engine)
    
    # query to summarize temperature data filtered by start and end dates
    temps = session.query(func.min(Measurement.tobs).label('min'),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_dt).\
        filter(Measurement.date <= end_dt).one()
    
    # close session    
    session.close()
    
    # create liset and return as JSON
    temp_summary = [
        {'min':temps[0],
        'avg':temps[1],
        'max':temps[2]
        }
    ]
    return jsonify(temp_summary)

# run app
if __name__ == '__main__':
    app.run(debug=False)