from cassandra.cluster import Cluster
from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from cassandra.cqlengine.query import BatchQuery
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.models import Model

from collections import Counter
import uuid
import pandas as pd
import math
import datetime as dt

BATCH_SIZE=10000
HOSTS = ['127.0.0.1']

class FlightModel(Model):
    __table_name__ = "flightlog"
    __keyspace__   = "airport"

    id                  = columns.Integer(primary_key=True)
    year                = columns.Integer()
    day_of_month        = columns.Integer()
    fl_date             = columns.DateTime()
    airline_id          = columns.Integer()
    carrier             = columns.Text()
    fl_num              = columns.Integer()
    origin_airport_id   = columns.Integer()
    origin              = columns.Text()
    origin_city_name    = columns.Text()
    origin_state_abr    = columns.Text()
    dest                = columns.Text()
    dest_city_name      = columns.Text()
    dest_state_abr      = columns.Text()
    dep_time            = columns.DateTime()
    arr_time            = columns.DateTime()
    actual_elapsed_time = columns.Integer()
    air_time            = columns.Integer()
    distance            = columns.Integer()


def load_csv():
    # ref panda see:
    #  https://www.datacamp.com/community/blog/python-pandas-cheat-sheet
    #  https://www.datacamp.com/community/tutorials/python-data-science-cheat-sheet-basics

    # create the table using the FlightModel
    sync_table(FlightModel)

    # load the data from a csv
    df = pd.read_csv("flights_from_pg.csv", header=None)

    df.columns = ['id',
                  'year',
                  'day_of_month',
                  'fl_date',
                  'airline_id',
                  'carrier',
                  'fl_num',
                  'origin_airport_id',
                  'origin',
                  'origin_city_name',
                  'origin_state_abr',
                  'dest',
                  'dest_city_name',
                  'dest_state_abr',
                  'dep_time',
                  'arr_time',
                  'actual_elapsed_time',
                  'air_time',
                  'distance']

    # Combine dep_time and arr_time have 2400 values - change those to 0000
    df.dep_time[df.dep_time == 2400] = 0
    df.arr_time[df.arr_time == 2400] = 0

    # add the date parts to the departure and arrival times
    padtime = lambda x: "%04d" % x
    df.dep_time = df.fl_date + " " + df.dep_time.apply(padtime)
    df.arr_time = df.fl_date + " " + df.arr_time.apply(padtime)

    # convert all the timestamp types to pandas datetimes
    df.fl_date  = pd.to_datetime(df.fl_date)
    df.dep_time = pd.to_datetime(df.dep_time)
    df.arr_time = pd.to_datetime(df.arr_time)

    # output the table data: rows, columns
    print(df.shape)

    # Apply/load the data to the table..
    df.apply( lambda r: FlightModel.create(**r.to_dict()), axis=1)



########
# Main #
########

# Initialise connection to cluster
connection.setup(HOSTS, "cqlengine", protocol_version=3)

# Populate the flightlog table
load_csv()

