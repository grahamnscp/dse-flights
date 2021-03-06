# Datastax Flights Exercise

## DSE Install Docker (kick-tyres test)
```
$ docker run -d -p 9042:9042 --env DS_LICENSE=accept datastaxlabs/dse-cdc-server:6.8.0-20190925
a07f08c9c65187b7ae14b2f9d21104ddabcd84b092b9c757cda730c547fbfe5e

$ docker ps
CONTAINER ID        IMAGE                                        COMMAND                  CREATED             STATUS              PORTS                                                                                                                                                                                                     NAMES
a07f08c9c651        datastaxlabs/dse-cdc-server:6.8.0-20190925   "/entrypoint.sh dse …"   6 minutes ago       Up 6 minutes        4004/tcp, 4040/tcp, 5598-5599/tcp, 7000-7001/tcp, 7077/tcp, 7080-7081/tcp, 7199/tcp, 8090/tcp, 8182/tcp, 8609/tcp, 8983-8984/tcp, 9103/tcp, 9160/tcp, 9999-10000/tcp, 18080/tcp, 0.0.0.0:9042->9042/tcp   boring_bassi

$ docker exec -it a07f08c9c651 cqlsh 
```
The Docker image had resource issues with bulk workloads so switched to Linux VM testing.
```
<stdin>:1:Failed to import 20 rows: OverloadedErrorMessage - Request dropped due to backpressure overload: timeout exceeded.,  will retry later, attempt 1 of 5
```


## DSE Install Centos 7 (for exercise)
```
# cat /etc/redhat-release
CentOS Linux release 7.8.2003 (Core)

## Doc ref: https://docs.datastax.com/en/install/6.8/install/installRHELdse.html

# yum install java-1.8.0-openjdk

# java -version
openjdk version "1.8.0_242"
OpenJDK Runtime Environment (build 1.8.0_242-b08)
OpenJDK 64-Bit Server VM (build 25.242-b08, mixed mode)

# python --version
Python 2.7.5

# rpm -qa | grep libaio
libaio-0.3.109-13.el7.x86_64

cat <<EOF>> /etc/yum.repos.d/datastax.repo
[datastax] 
name=DataStax Repo for DataStax Enterprise
baseurl=https://rpm.datastax.com/enterprise/
enabled=1
gpgcheck=1
gpgkey=https://rpm.datastax.com/rpm/repo_key
EOF

# yum repolist
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: repo.uk.bigstepcloud.com
 * extras: mirrors.clouvider.net
 * updates: mirrors.clouvider.net
datastax                      | 2.5 kB  00:00:00
datastax/primary_db           | 656 kB  00:00:01
repo id                       repo name                                                                                           status
base/7/x86_64                 CentOS-7 - Base                          10,070
datastax                      DataStax Repo for DataStax Enterprise    1,468
extras/7/x86_64               CentOS-7 - Extras                        392
updates/7/x86_64              CentOS-7 - Updates                       159
repolist: 12,089

# yum makecache fast

# yum list dse*
Available Packages
dse.noarch                            6.8.0-1                datastax
dse-demos.noarch                      6.8.0-1                datastax
dse-full.noarch                       6.8.0-1                datastax
dse-libcassandra.noarch               6.8.0-1                datastax
dse-libgraph.noarch                   6.8.0-1                datastax
dse-libhadoop.noarch                  5.0.15-1               datastax
dse-libhadoop-native.i386             5.0.15-1               datastax
dse-libhadoop-native.x86_64           5.0.15-1               datastax
dse-libhadoop2-client.noarch          6.8.0-1                datastax
dse-libhive.noarch                    5.0.15-1               datastax
dse-liblog4j.noarch                   6.8.0-1                datastax
dse-libmahout.noarch                  5.0.15-1               datastax
dse-libpig.noarch                     5.0.15-1               datastax
dse-libsolr.noarch                    6.8.0-1                datastax
dse-libspark.noarch                   6.8.0-1                datastax
dse-libsqoop.noarch                   5.0.15-1               datastax
dse-libtomcat.noarch                  6.8.0-1                datastax

# yum install dse-full
==========================================================================================================
 Package                                Arch              Version             Repository            Size
==========================================================================================================
Installing:
 dse-full                               noarch            6.8.0-1             datastax              132 k
Installing for dependencies:
 dse                                    noarch            6.8.0-1             datastax              235 M
 dse-libcassandra                       noarch            6.8.0-1             datastax              79 M
 dse-libgraph                           noarch            6.8.0-1             datastax              249 M
 dse-libhadoop2-client                  noarch            6.8.0-1             datastax              71 M
 dse-liblog4j                           noarch            6.8.0-1             datastax              14 k
 dse-libsolr                            noarch            6.8.0-1             datastax              69 M
 dse-libspark                           noarch            6.8.0-1             datastax              436 M
 dse-libtomcat                          noarch            6.8.0-1             datastax              5.1 M

Transaction Summary
==========================================================================================================
Install  1 Package (+8 Dependent packages)

Total download size: 1.1 G
Installed size: 1.3 G
Downloading packages:
warning: /var/cache/yum/x86_64/7/datastax/packages/dse-full-6.8.0-1.noarch.rpm: Header V3 RSA/SHA256 Signature, key ID 10782bd9: NOKEY                ]  0.0 B/s | 122 kB  --:--:-- ETA
Public key for dse-full-6.8.0-1.noarch.rpm is not installed
(1/9): dse-full-6.8.0-1.noarch.rpm                    | 132 kB  00:00:01
(2/9): dse-libcassandra-6.8.0-1.noarch.rpm            |  79 MB  00:00:19
(3/9): dse-libgraph-6.8.0-1.noarch.rpm                | 249 MB  00:00:43
(4/9): dse-libhadoop2-client-6.8.0-1.noarch.rpm       |  71 MB  00:00:14
(5/9): dse-liblog4j-6.8.0-1.noarch.rpm                |  14 kB  00:00:00
(6/9): dse-libsolr-6.8.0-1.noarch.rpm                 |  69 MB  00:00:12
(7/9): dse-libspark-6.8.0-1.noarch.rpm                | 436 MB  00:01:09
(8/9): dse-libtomcat-6.8.0-1.noarch.rpm               | 5.1 MB  00:00:01
(9/9): dse-6.8.0-1.noarch.rpm                         | 235 MB  00:03:18
--------------------------------------------------------------------------
Total                                        5.8 MB/s | 1.1 GB  00:03:18
Retrieving key from https://rpm.datastax.com/rpm/repo_key
Importing GPG key 0x10782BD9:
 Userid     : "DataStax Engineering (2018) <dseng@datastax.com>"
 Fingerprint: 0f6b a21e fd0e 773a 61c1 87f8 0ff0 d860 1078 2bd9
 From       : https://rpm.datastax.com/rpm/repo_key
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : dse-libhadoop2-client-6.8.0-1.noarch     1/9
  Installing : dse-libcassandra-6.8.0-1.noarch          2/9
  Installing : dse-6.8.0-1.noarch                       3/9
  Installing : dse-libspark-6.8.0-1.noarch              4/9
  Installing : dse-libtomcat-6.8.0-1.noarch             5/9
  Installing : dse-libsolr-6.8.0-1.noarch               6/9
  Installing : dse-libgraph-6.8.0-1.noarch              7/9
  Installing : dse-liblog4j-6.8.0-1.noarch              8/9
  Installing : dse-full-6.8.0-1.noarch                  9/9
  Verifying  : dse-libspark-6.8.0-1.noarch              1/9
  Verifying  : dse-libtomcat-6.8.0-1.noarch             2/9
  Verifying  : dse-libcassandra-6.8.0-1.noarch          3/9
  Verifying  : dse-libsolr-6.8.0-1.noarch               4/9
  Verifying  : dse-libgraph-6.8.0-1.noarch              5/9
  Verifying  : dse-full-6.8.0-1.noarch                  6/9
  Verifying  : dse-6.8.0-1.noarch                       7/9
  Verifying  : dse-liblog4j-6.8.0-1.noarch              8/9
  Verifying  : dse-libhadoop2-client-6.8.0-1.noarch     9/9

Installed:
  dse-full.noarch 0:6.8.0-1

Dependency Installed:
  dse.noarch 0:6.8.0-1             dse-libcassandra.noarch 0:6.8.0-1     dse-libgraph.noarch 0:6.8.0-1      dse-libhadoop2-client.noarch 0:6.8.0-1     dse-liblog4j.noarch 0:6.8.0-1
  dse-libsolr.noarch 0:6.8.0-1     dse-libspark.noarch 0:6.8.0-1         dse-libtomcat.noarch 0:6.8.0-1

Complete!

# service dse start
Starting DSE daemon : dse
DSE daemon starting with only Cassandra enabled (edit /etc/default/dse to enable other features)

# service dse status
dse is running

# nodetool info
ID                     : 84bb5e50-f8dc-4f71-96d9-54917dc28275
Gossip active          : true
Native Transport active: true
Status                 : OK
Load                   : 194.08 KiB
Generation No          : 1588149061
Uptime (seconds)       : 163
Heap Memory (MB)       : 1612.35 / 2964.00
Off Heap Memory (MB)   : 0.01
Data Center            : Cassandra
Rack                   : rack1
Exceptions             : 0
Key Cache              : entries 0, size 0 bytes, capacity 100 MiB, 0 hits, 0 requests, NaN recent hit rate, 14400 save period in seconds
Row Cache              : entries 0, size 0 bytes, capacity 0 bytes, 0 hits, 0 requests, NaN recent hit rate, 0 save period in seconds
Counter Cache          : entries 0, size 0 bytes, capacity 50 MiB, 0 hits, 0 requests, NaN recent hit rate, 7200 save period in seconds
Chunk Cache            : entries 75, size 444 KiB, capacity 2.06 GiB, 75 misses, 594 requests, 0.874 recent hit rate, 1669.240 microseconds miss latency
Percent Repaired       : NaN%
Token                  : -7676947935534642756


# nodetool status
Datacenter: Cassandra
=====================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving/Stopped
--  Address    Load       Owns (effective)  Host ID                               Token                                    Rack
UN  127.0.0.1  194.08 KiB  100.0%            84bb5e50-f8dc-4f71-96d9-54917dc28275  -7676947935534642756                     rack1

# netstat -tulnp | egrep 'java'
tcp        0      0 127.0.0.1:9042          0.0.0.0:*               LISTEN      3618/java
tcp        0      0 127.0.0.1:7000          0.0.0.0:*               LISTEN      3618/java
tcp        0      0 127.0.0.1:7199          0.0.0.0:*               LISTEN      3618/java
tcp        0      0 127.0.0.1:40033         0.0.0.0:*               LISTEN      3618/java
tcp        0      0 127.0.0.1:8609          0.0.0.0:*               LISTEN      3618/java

# cqlsh -u dse -p dse -e "describe keyspaces;"

system_virtual_schema  system_schema  dse_leases          system_traces
dse_system_local       system_auth    system_backups      dse_perf
dse_security           system_views   dse_insights        dse_insights_local
solr_admin             system         system_distributed  dse_system
```


## Flight data parsing and loading

### Create keyspace called airport
```
# cqlsh -u dse -p dse -e "create keyspace airport with replication = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };"

# cqlsh -u dse -p dse -e "describe keyspace airport;"
CREATE KEYSPACE airport WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}  AND durable_writes = true;
```

### Example table structure
```
   id                  int PRIMARY KEY,
   year                int,
   day_of_month        int,
   fl_date             timestamp,
   airline_id          int,
   carrier             varchar,
   fl_num              int,
   origin_airport_id   int,
   origin              varchar,
   origin_city_name    varchar,
   origin_state_abr    varchar,
   dest_airport_id     varchar,
   dest_city_name      varchar,
   dest_state_abr      varchar,
   dep_time            timestamp,
   arr_time            timestamp,
   actual_elapsed_time timestamp,
   air_time            timestamp,
   distance            int
```

### Examine data set
```
# head -5 flights_from_pg.csv
3,2012,1,2012/11/11,19805,AA,1,12478,JFK,New York, NY,LAX,Los Angeles, CA,855,1142,347,330,2475
4,2012,2,2012/01/02,19805,AA,1,12478,JFK,New York, NY,LAX,Los Angeles, CA,921,1210,349,325,2475
5,2012,3,2012/01/03,19805,AA,1,12478,JFK,New York, NY,LAX,Los Angeles, CA,931,1224,353,319,2475
6,2012,4,2012/01/04,19805,AA,1,12478,JFK,New York, NY,LAX,Los Angeles, CA,904,1151,347,309,2475
7,2012,5,2012/01/05,19805,AA,1,12478,JFK,New York, NY,LAX,Los Angeles, CA,858,1142,344,306,2475

# wc -l flights_from_pg.csv
 1048575 flights_from_pg.csv
```

### Check id is unique
```
# cat flights_from_pg.csv | awk -F ',' '{print $1}' | sort -V | wc -l
1048576
# cat flights_from_pg.csv | awk -F ',' '{print $1}' | sort -u | wc -l
1048576
# uni
unicode_start  unicode_stop   uniq           unix_chkpwd    unix_update
# cat flights_from_pg.csv | awk -F ',' '{print $1}' | uniq -d flights_from_pg.csv
```

### Convert date to ISO YYYY-MM-DD from YYYY/MM/DD
```
cat flights_from_pg.csv | sed 's/\//-/g' > flights_data.csv
```

### Investigate field types, try date offsets as type int
```
# head -1 flights_data.csv
3,2012,1,2012-11-11,19805,AA,1,12478,JFK,New York, NY,LAX,Los Angeles, CA,855,1142,347,330,2475

# head -1 flights_data.csv | awk -F ',' '{ printf "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n",$1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16,$17,$18,$19 }'
3,2012,1,2012-11-11,19805,AA,1,12478,JFK,New York, NY,LAX,Los Angeles, CA,855,1142,347,330,2475

# head -1 flights_data.csv | awk -F ',' '{ printf "%d,%d,%d,%s,%d,%s,%d,%d,%s,%s,%s,%s,%s,%s,%d,%d,%d,%d,%d\n",$1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16,$17,$18,$19 }'
3,2012,1,2012-11-11,19805,AA,1,12478,JFK,New York, NY,LAX,Los Angeles, CA,855,1142,347,330,2475

## trim the US State code fields leading space:
# head -1 flights_data.csv | awk -F ',' 'function trim(f){gsub(/^ +| +$/,"", f);return f}{ printf "%d,%d,%d,%s,%d,%s,%d,%d,%s,%s,%s,%s,%s,%s,%d,%d,%d,%d,%d\n",$1,$2,$3,$4,$5,$6,$7,$8,$9,$10,trim($11),$12,$13,trim($14),$15,$16,$17,$18,$19 }'
3,2012,1,2012-11-11,19805,AA,1,12478,JFK,New York,NY,LAX,Los Angeles,CA,855,1142,347,330,2475

# cat flights_data.csv | awk -F ',' 'function trim(f){gsub(/^ +| +$/,"", f);return f}{ printf "%d,%d,%d,%s,%d,%s,%d,%d,%s,%s,%s,%s,%s,%s,%d,%d,%d,%d,%d\n",$1,$2,$3,$4,$5,$6,$7,$8,$9,$10,trim($11),$12,$13,trim($14),$15,$16,$17,$18,$19 }' > flights_data_cleaned.csv

```

### Create a flights table
```
cat <<EOF>> airport-flights-ddl.cql
CREATE TABLE IF NOT EXISTS airport.flights
  (id                  int PRIMARY KEY,
   year                int,
   day_of_month        int,
   fl_date             timestamp,
   airline_id          int,
   carrier             varchar,
   fl_num              int,
   origin_airport_id   int,
   origin              varchar,
   origin_city_name    varchar,
   origin_state_abr    varchar,
   dest                varchar,
   dest_city_name      varchar,
   dest_state_abr      varchar,
   dep_time            int,
   arr_time            int,
   actual_elapsed_time int,
   air_time            int,
   distance            int,
);
EOF

# cqlsh -u dse -p dse -f airport-flights-ddl.cql
# cqlsh -u dse -p dse -e "describe airport.flights;"
CREATE TABLE airport.flights (
    id int PRIMARY KEY,
    actual_elapsed_time int,
    air_time int,
    airline_id int,
    arr_time int,
    carrier text,
    day_of_month int,
    dep_time int,
    dest text,
    dest_city_name text,
    dest_state_abr text,
    distance int,
    fl_date timestamp,
    fl_num int,
    origin text,
    origin_airport_id int,
    origin_city_name text,
    origin_state_abr text,
    year int
) WITH additional_write_policy = '99PERCENTILE'
    AND bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
    AND compression = {'chunk_length_in_kb': '64', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND crc_check_chance = 1.0
    AND default_time_to_live = 0
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND nodesync = {'enabled': 'true', 'incremental': 'true'}
    AND read_repair = 'BLOCKING'
    AND speculative_retry = '99PERCENTILE';
```

### Bulk csv data load from file
```
# time cqlsh -u dse -p dse -e "COPY airport.flights(id,year,day_of_month,fl_date,airline_id,carrier,fl_num,origin_airport_id,origin,origin_city_name,origin_state_abr,dest,dest_city_name,dest_state_abr,dep_time,arr_time,actual_elapsed_time,air_time,distance) FROM './flights_data_cleaned.csv';"
Using 3 child processes

Starting copy of airport.flights with columns [id, year, day_of_month, fl_date, airline_id, carrier, fl_num, origin_airport_id, origin, origin_city_name, origin_state_abr, dest, dest_city_name, dest_state_abr, dep_time, arr_time, actual_elapsed_time, air_time, distance].
Processed: 1048576 rows; Rate:    4835 rows/s; Avg. rate:    4703 rows/s
1048576 rows imported from 1 files in 3 minutes and 42.942 seconds (0 skipped).

real	3m44.100s
user	9m36.773s
sys	0m27.404s

# cqlsh -u dse -p dse -e "select * from airport.flights where id in (3, 1048578);"

 id      | actual_elapsed_time | air_time | airline_id | arr_time | carrier | day_of_month | dep_time | dest | dest_city_name | dest_state_abr | distance | fl_date                         | fl_num | origin | origin_airport_id | origin_city_name | origin_state_abr | year
---------+---------------------+----------+------------+----------+---------+--------------+----------+------+----------------+----------------+----------+---------------------------------+--------+--------+-------------------+------------------+------------------+------
       3 |                 347 |      330 |      19805 |     1142 |      AA |            1 |      855 |  LAX |    Los Angeles |             CA |     2475 | 2012-11-11 00:00:00.000000+0000 |      1 |    JFK |             12478 |         New York |               NY | 2012
 1048578 |                 126 |      101 |      19790 |     2240 |      DL |            2 |     2134 |  MDW |        Chicago |             IL |      591 | 2012-01-02 00:00:00.000000+0000 |   2346 |    ATL |             10397 |          Atlanta |               GA | 2012

(2 rows)
```

## Table of flights leaving LAX, sorted by time
Create and populate a Cassandra table designed to list all flights leaving a particular airport, sorted by time  

Note that long running queries will hit the default cqlsh utility timeouts, extending these with client overrides:
```
# time /bin/cqlsh -e "select count(\*) from airport.flights;"
<stdin>:1:OperationTimedOut: errors={'127.0.0.1:9042': 'Client request timeout. See Session.execute[_async](timeout)'}, last_host=127.0.0.1:9042

real	0m11.154s
user	0m0.903s
sys	0m0.182s

# time /bin/cqlsh --connect-timeout=300 --request-timeout=180  -e "select count(*) from airport.flights;"

 count
---------
 1048576

(1 rows)

Warnings :
Aggregation query used without partition key


real	0m29.602s
user	0m0.923s
sys	0m0.172s

# alias cqlsh='/bin/cqlsh --connect-timeout=300 --request-timeout=180 '

```

### Queries without using partition keys is bad!

How many rows with flights originating from LAX?

```
# cqlsh -e "select count(*) from airport.flights where origin='LAX' allow filtering;"

 count
-------
 38822

(1 rows)

Warnings :
Aggregation query used without partition key
```
but :/
```
# cqlsh -e "paging off; select * from airport.flights where origin='LAX' allow filtering;"
Disabled Query paging.
<stdin>:1:ReadTimeout: Error from server: code=1200 [Coordinator node timed out waiting for replica nodes' responses] message="Operation timed out - received only 0 responses." info={'received_responses': 0, 'required_responses': 1, 'consistency': 'ONE'}
```
and :/
```
# cqlsh -e "paging off; capture 'LAX.out1'; select * from airport.flights where origin='LAX' allow filtering;"
Disabled Query paging.
Now capturing query output to 'LAX.out1'.
<stdin>:1:ReadTimeout: Error from server: code=1200 [Coordinator node timed out waiting for replica nodes' responses] message="Operation timed out - received only 0 responses." info={'received_responses': 0, 'required_responses': 1, 'consistency': 'ONE'}
[root@dse cql]# l LAX.out1
-rw-r--r--. 1 root root 0 Apr 29 15:19 LAX.out1

# cqlsh -e "paging 10000; capture 'LAX.out1'; select * from airport.flights where origin='LAX' allow filtering;"
Page size: 10000
Now capturing query output to 'LAX.out1'.
[root@dse cql]# wc -l LAX.out1
11115 LAX.out1

# cqlsh -e "paging 20000; capture 'LAX.out1'; select * from airport.flights where origin='LAX' allow filtering;"
Page size: 20000
Now capturing query output to 'LAX.out1'.
<stdin>:1:ReadTimeout: Error from server: code=1200 [Coordinator node timed out waiting for replica nodes' responses] message="Operation timed out - received only 0 responses." info={'received_responses': 0, 'required_responses': 1, 'consistency': 'ONE'}

```
Can't see any errors in the backend logs, also checked that VM (12GB memory, 4 vcpu) is not running out of memory.  

## Create table and loading data via python

It's easier to manipulate dates via python than bash!

Here is an example of using python with the python cassandra-driver and panda

DSE documentation for the driver can be viewed here:  
https://docs.datastax.com/en/driver-matrix/doc/driver_matrix/common/driverMatrix.html
https://docs.datastax.com/en/developer/python-driver/3.23/installation/

Some information relating to pandas can be found here:  
https://pandas.pydata.org
https://www.datacamp.com/community/blog/python-pandas-cheat-sheet
https://www.datacamp.com/community/tutorials/python-data-science-cheat-sheet-basics

load_data.py
```
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

```

Preparing centos 7 os to run the load_data.py script:
```
# yum install -y python3-pip
# pip3 install cassandra-driver
# pip3 install pandas
# pip3 install python-lambda-local
```

Running the load_data.py script:
```
# python3 load_data.py
load_data.py:74: SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  df.dep_time[df.dep_time == 2400] = 0
load_data.py:75: SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  df.arr_time[df.arr_time == 2400] = 0
(1048576, 19)
#
# cqlsh -e "select count(*) from airport.flightlog;

 count
---------
 1048576

(1 rows)
```

airport.flightlog table definition:
```
# cqlsh -e "describe airport.flightlog;"

CREATE TABLE airport.flightlog (
    id int PRIMARY KEY,
    actual_elapsed_time int,
    air_time int,
    airline_id int,
    arr_time timestamp,
    carrier text,
    day_of_month int,
    dep_time timestamp,
    dest text,
    dest_city_name text,
    dest_state_abr text,
    distance int,
    fl_date timestamp,
    fl_num int,
    origin text,
    origin_airport_id int,
    origin_city_name text,
    origin_state_abr text,
    year int
) WITH additional_write_policy = '99PERCENTILE'
    AND bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
    AND compression = {'chunk_length_in_kb': '64', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND crc_check_chance = 1.0
    AND default_time_to_live = 0
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND nodesync = {'enabled': 'true', 'incremental': 'true'}
    AND read_repair = 'BLOCKING'
    AND speculative_retry = '99PERCENTILE';

```

## Materialized Views

Cassandra supports adding additional indexes onto a table containing base data, however this has performance implications with the clustering of data across the cluster.
A better solution is to use Materialized Views, which create a copy of the selected data stored and clustered as desired for the required queries.
Materialised Views have the benefit that they will be updated when data is changed in the source table vs importing separate tables from an external data source (csv in this test case) which would require updating independantly.

Materialized view for departures allowing queries on origin airport code:
```
# cqlsh -e "create materialized view airport.departures_mv as select * from airport.flightlog where origin is not null and id is not null primary key (origin, id);"
# cqlsh -e "describe airport.departures_mv;"

CREATE MATERIALIZED VIEW airport.departures_mv AS
    SELECT *
    FROM airport.flightlog
    WHERE origin IS NOT NULL AND id IS NOT NULL
    PRIMARY KEY (origin, id)
    WITH CLUSTERING ORDER BY (id ASC)
    AND additional_write_policy = '99PERCENTILE'
    AND bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
    AND compression = {'chunk_length_in_kb': '64', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND crc_check_chance = 1.0
    AND default_time_to_live = 0
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair = 'BLOCKING'
    AND speculative_retry = '99PERCENTILE';
```

Example query using the view departures_mv:
```
# cqlsh -e "select count(*) from airport.departures_mv where origin='SFO'"

 count
-------
 28386

(1 rows)

# cqlsh -e "select dep_time, origin, fl_num from airport.departures_mv where origin='SFO' limit 10;"

 dep_time                        | origin | fl_num
---------------------------------+--------+--------
 2012-01-20 00:32:00.000000+0000 |    SFO |     18
 2012-01-18 14:58:00.000000+0000 |    SFO |     20
 2012-01-28 14:54:00.000000+0000 |    SFO |     20
 2012-01-08 06:54:00.000000+0000 |    SFO |     24
 2012-01-25 06:55:00.000000+0000 |    SFO |     24
 2012-01-28 06:53:00.000000+0000 |    SFO |     24
 2012-01-17 22:13:00.000000+0000 |    SFO |    272
 2012-01-21 22:03:00.000000+0000 |    SFO |    272
 2012-01-23 23:33:00.000000+0000 |    SFO |    272
 2012-01-11 07:40:00.000000+0000 |    SFO |    312

(10 rows)
```

Materialized view for flight departure time window queries:
```
# cqlsh -e "create materialized view airport.dep_time_mv as select * from airport.flightlog where dep_time is not null and origin is not null and id is not null primary key (dep_time, id);"
# cqlsh -e "describe airport.dep_time_mv;"

CREATE MATERIALIZED VIEW airport.dep_time_mv AS
    SELECT *
    FROM airport.flightlog
    WHERE dep_time IS NOT NULL AND origin IS NOT NULL AND id IS NOT NULL
    PRIMARY KEY (dep_time, id)
    WITH CLUSTERING ORDER BY (id ASC)
    AND additional_write_policy = '99PERCENTILE'
    AND bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
    AND compression = {'chunk_length_in_kb': '64', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND crc_check_chance = 1.0
    AND default_time_to_live = 0
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair = 'BLOCKING'
    AND speculative_retry = '99PERCENTILE';
```

Example query using the view airport.dep_time_mv:
```
select dep_time, origin, fl_num from airport.dep_time_mv where origin='DFW' and dep_time >= '2012-01-20 10:00:00' and dep_time <= '2012-01-20 10:10' allow filtering;

 dep_time                        | origin | fl_num
---------------------------------+--------+--------
 2012-01-20 10:08:00.000000+0000 |    DFW |   1087
 2012-01-20 10:08:00.000000+0000 |    DFW |   4921
 2012-01-20 10:08:00.000000+0000 |    DFW |   1087
 2012-01-20 10:08:00.000000+0000 |    DFW |   4921
 2012-01-20 10:08:00.000000+0000 |    DFW |   1087
 2012-01-20 10:04:00.000000+0000 |    DFW |    493
 2012-01-20 10:04:00.000000+0000 |    DFW |    493
 2012-01-20 10:04:00.000000+0000 |    DFW |    493
 2012-01-20 10:05:00.000000+0000 |    DFW |    654
 2012-01-20 10:05:00.000000+0000 |    DFW |    654
 2012-01-20 10:05:00.000000+0000 |    DFW |    654
 2012-01-20 10:09:00.000000+0000 |    DFW |    689
 2012-01-20 10:09:00.000000+0000 |    DFW |    689
 2012-01-20 10:09:00.000000+0000 |    DFW |    689
 2012-01-20 10:10:00.000000+0000 |    DFW |    712
 2012-01-20 10:10:00.000000+0000 |    DFW |    712
 2012-01-20 10:10:00.000000+0000 |    DFW |    712
 2012-01-20 10:01:00.000000+0000 |    DFW |   1331
 2012-01-20 10:01:00.000000+0000 |    DFW |   1331
 2012-01-20 10:01:00.000000+0000 |    DFW |   1331
 2012-01-20 10:02:00.000000+0000 |    DFW |   1599
 2012-01-20 10:02:00.000000+0000 |    DFW |   1599
 2012-01-20 10:02:00.000000+0000 |    DFW |   1599
 2012-01-20 10:00:00.000000+0000 |    DFW |   2748
 2012-01-20 10:00:00.000000+0000 |    DFW |   2748

(25 rows)
```

## DSE Search
Documentation reference: https://docs.datastax.com/en/dse/6.7/dse-admin/datastax_enterprise/search/searchTOC.html

### Enable Search SOLR in DSE:

Uncomment SOLR_ENABLED and SPARK_ENABLED flags and set to 1 in /etc/default/dse file:
```
# egrep  "SOLR|SPARK" /etc/default/dse
#SOLR_ENABLED=0
SOLR_ENABLED=1
#SPARK_ENABLED=0
SPARK_ENABLED=1
#SPARK_HOME=your_spark_install_location
SPARK_CONF_DIR=/etc/dse/spark
```

Restart the dse init.d service:
```
# service dse stop

# sleep 5

# service dse start
Starting DSE daemon : dse
DSE daemon starting with Solr enabled (edit /etc/default/dse to disable)
DSE daemon starting with Spark enabled (edit /etc/default/dse to disable)

# sleep 10

# service dse status
dse is running

# nodetool status
Datacenter: SearchAnalytics
===========================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving/Stopped
--  Address    Load       Owns (effective)  Host ID                               Token                                    Rack
UN  127.0.0.1  367.49 MiB  100.0%            84bb5e50-f8dc-4f71-96d9-54917dc28275  -7676947935534642756                     rack1
```
Note the node type above is SearchAnalytics

```
# netstat -tulnp | grep java
tcp        0      0 127.0.0.1:9042          0.0.0.0:*               LISTEN      27802/java
tcp        0      0 127.0.0.1:7447          0.0.0.0:*               LISTEN      27802/java
tcp        0      0 127.0.0.1:8983          0.0.0.0:*               LISTEN      27802/java
tcp        0      0 127.0.0.1:7000          0.0.0.0:*               LISTEN      27802/java
tcp        0      0 127.0.0.1:5598          0.0.0.0:*               LISTEN      27802/java
tcp        0      0 127.0.0.1:5599          0.0.0.0:*               LISTEN      27802/java
tcp        0      0 127.0.0.1:7199          0.0.0.0:*               LISTEN      27802/java
tcp        0      0 127.0.0.1:8609          0.0.0.0:*               LISTEN      27802/java
tcp        0      0 127.0.0.1:7077          0.0.0.0:*               LISTEN      27802/java
tcp        0      0 127.0.0.1:7080          0.0.0.0:*               LISTEN      27802/java
tcp        0      0 127.0.0.1:7081          0.0.0.0:*               LISTEN      27802/java
tcp        0      0 127.0.0.1:7437          0.0.0.0:*               LISTEN      27802/java
tcp        0      0 127.0.0.1:43566         0.0.0.0:*               LISTEN      27802/java
tcp        0      0 127.0.0.1:37232         0.0.0.0:*               LISTEN      27802/java

# ls -latFrh /var/log/tomcat/
total 24K
drwxr-xr-x. 12 root      root      4.0K May  1 03:07 ../
-rw-r--r--.  1 cassandra cassandra    0 May  1 14:32 localhost.2020-05-01.log
-rw-r--r--.  1 cassandra cassandra    0 May  1 14:32 manager.2020-05-01.log
-rw-r--r--.  1 cassandra cassandra    0 May  1 14:32 host-manager.2020-05-01.log
drwxr-xr-x.  2 cassandra cassandra  134 May  1 14:32 ./
-rw-r--r--.  1 cassandra cassandra  17K May  1 14:38 catalina.2020-05-01.log

# cat /var/log/tomcat/catalina.2020-05-01.log | grep http
01-May-2020 14:38:29.436 INFO [DSE main thread] org.apache.coyote.AbstractProtocol.init Initializing ProtocolHandler ["http-bio-127.0.0.1-8983"]
01-May-2020 14:38:29.501 INFO [DSE main thread] org.apache.coyote.AbstractProtocol.start Starting ProtocolHandler ["http-bio-127.0.0.1-8983"]
```

### Creating a search index on a table

Doc reference: https://docs.datastax.com/en/dse/6.8/dse-dev/datastax_enterprise/search/searchIndexConfig.html

```
# cqlsh
Connected to Test Cluster at 127.0.0.1:9042.
[cqlsh 6.8.0 | DSE 6.8.0 | CQL spec 3.4.5 | DSE protocol v2]
Use HELP for help.
cqlsh> use airport;
cqlsh:airport> CREATE SEARCH INDEX ON airport.flightlog ;

Warnings :
Search index successfully created in distributed mode; executed index reload and reindex on all nodes in DC Solr.

cqlsh:airport> describe airport.flightlog;

CREATE TABLE airport.flightlog (
    id int PRIMARY KEY,
    actual_elapsed_time int,
    air_time int,
    airline_id int,
    arr_time timestamp,
    carrier text,
    day_of_month int,
    dep_time timestamp,
    dest text,
    dest_city_name text,
    dest_state_abr text,
    distance int,
    fl_date timestamp,
    fl_num int,
    origin text,
    origin_airport_id int,
    origin_city_name text,
    origin_state_abr text,
    solr_query text,
    year int
) WITH additional_write_policy = '99PERCENTILE'
    AND bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
    AND compression = {'chunk_length_in_kb': '64', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND crc_check_chance = 1.0
    AND default_time_to_live = 0
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND nodesync = {'enabled': 'true', 'incremental': 'true'}
    AND read_repair = 'BLOCKING'
    AND speculative_retry = '99PERCENTILE';
CREATE CUSTOM INDEX airport_flightlog_solr_query_index ON airport.flightlog (solr_query) USING 'com.datastax.bdp.search.solr.Cql3SolrSecondaryIndex';

cqlsh:airport> ALTER SEARCH INDEX CONFIG ON airport.flightlog SET autoCommitTime = 30000;
cqlsh:airport> DESCRIBE pending SEARCH INDEX CONFIG on airport.flightlog;

<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<config>
  <luceneMatchVersion>LUCENE_6_0_1</luceneMatchVersion>
  <dseTypeMappingVersion>2</dseTypeMappingVersion>
  <directoryFactory class="solr.StandardDirectoryFactory" name="DirectoryFactory"/>
  <indexConfig>
    <rt>false</rt>
  </indexConfig>
  <jmx/>
  <updateHandler>
    <autoSoftCommit>
      <maxTime>30000</maxTime>
    </autoSoftCommit>
  </updateHandler>
  <query>
    <filterCache class="solr.SolrFilterCache" highWaterMarkMB="2048" lowWaterMarkMB="1024"/>
    <enableLazyFieldLoading>true</enableLazyFieldLoading>
    <useColdSearcher>true</useColdSearcher>
    <maxWarmingSearchers>16</maxWarmingSearchers>
  </query>
  <requestDispatcher>
    <requestParsers enableRemoteStreaming="true" multipartUploadLimitInKB="2048000"/>
    <httpCaching never304="true"/>
  </requestDispatcher>
  <requestHandler class="solr.SearchHandler" default="true" name="search"/>
  <requestHandler class="com.datastax.bdp.search.solr.handler.component.CqlSearchHandler" name="solr_query"/>
  <requestHandler class="solr.UpdateRequestHandler" name="/update"/>
  <requestHandler class="solr.UpdateRequestHandler" name="/update/csv" startup="lazy"/>
  <requestHandler class="solr.UpdateRequestHandler" name="/update/json" startup="lazy"/>
  <requestHandler class="solr.FieldAnalysisRequestHandler" name="/analysis/field" startup="lazy"/>
  <requestHandler class="solr.DocumentAnalysisRequestHandler" name="/analysis/document" startup="lazy"/>
  <requestHandler class="solr.admin.AdminHandlers" name="/admin/"/>
  <requestHandler class="solr.PingRequestHandler" name="/admin/ping">
    <lst name="invariants">
      <str name="qt">search</str>
      <str name="q">solrpingquery</str>
    </lst>
    <lst name="defaults">
      <str name="echoParams">all</str>
    </lst>
  </requestHandler>
  <requestHandler class="solr.DumpRequestHandler" name="/debug/dump">
    <lst name="defaults">
      <str name="echoParams">explicit</str>
      <str name="echoHandler">true</str>
    </lst>
  </requestHandler>
</config>

cqlsh:airport> RELOAD SEARCH INDEX ON airport.flightlog;

Warnings :
Operation executed on all nodes in DC Solr.

# cqlsh -k airport -e "DESCRIBE ACTIVE SEARCH INDEX SCHEMA ON flightlog;"

<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<schema name="autoSolrSchema" version="1.5">
  <types>
    <fieldType class="org.apache.solr.schema.StrField" name="StrField"/>
    <fieldType class="org.apache.solr.schema.TrieDateField" name="TrieDateField"/>
    <fieldType class="org.apache.solr.schema.TrieIntField" name="TrieIntField"/>
  </types>
  <fields>
    <field indexed="true" multiValued="false" name="dest_city_name" type="StrField"/>
    <field indexed="true" multiValued="false" name="origin_city_name" type="StrField"/>
    <field docValues="true" indexed="true" multiValued="false" name="arr_time" type="TrieDateField"/>
    <field docValues="true" indexed="true" multiValued="false" name="distance" type="TrieIntField"/>
    <field docValues="true" indexed="true" multiValued="false" name="origin_airport_id" type="TrieIntField"/>
    <field docValues="true" indexed="true" multiValued="false" name="fl_date" type="TrieDateField"/>
    <field docValues="true" indexed="true" multiValued="false" name="year" type="TrieIntField"/>
    <field docValues="true" indexed="true" multiValued="false" name="dep_time" type="TrieDateField"/>
    <field indexed="true" multiValued="false" name="dest" type="StrField"/>
    <field docValues="true" indexed="true" multiValued="false" name="actual_elapsed_time" type="TrieIntField"/>
    <field docValues="true" indexed="true" multiValued="false" name="air_time" type="TrieIntField"/>
    <field indexed="true" multiValued="false" name="origin" type="StrField"/>
    <field indexed="true" multiValued="false" name="dest_state_abr" type="StrField"/>
    <field indexed="true" multiValued="false" name="origin_state_abr" type="StrField"/>
    <field indexed="true" multiValued="false" name="carrier" type="StrField"/>
    <field docValues="true" indexed="true" multiValued="false" name="fl_num" type="TrieIntField"/>
    <field docValues="true" indexed="true" multiValued="false" name="day_of_month" type="TrieIntField"/>
    <field docValues="true" indexed="true" multiValued="false" name="id" type="TrieIntField"/>
    <field docValues="true" indexed="true" multiValued="false" name="airline_id" type="TrieIntField"/>
  </fields>
  <uniqueKey>id</uniqueKey>
</schema>

```

### SOLR Query via CQL

Quick tests:
```
# cqlsh -k airport -e "select * from flightlog where solr_query='id:3';"

 id | actual_elapsed_time | air_time | airline_id | arr_time                        | carrier | day_of_month | dep_time                        | dest | dest_city_name | dest_state_abr | distance | fl_date                         | fl_num | origin | origin_airport_id | origin_city_name | origin_state_abr | solr_query | year
----+---------------------+----------+------------+---------------------------------+---------+--------------+---------------------------------+------+----------------+----------------+----------+---------------------------------+--------+--------+-------------------+------------------+------------------+------------+------
  3 |                 347 |      330 |      19805 | 2012-11-11 11:42:00.000000+0000 |      AA |            1 | 2012-11-11 08:55:00.000000+0000 |  LAX |    Los Angeles |             CA |     2475 | 2012-11-11 00:00:00.000000+0000 |      1 |    JFK |             12478 |         New York |               NY |       null | 2012

(1 rows)

# cqlsh -k airport -e "select dep_time, origin, fl_num from airport.flightlog where solr_query='dep_time:["2012-01-20T10:00:00Z" TO "2012-01-20T10:10:00Z"] AND origin:DFW';"

 dep_time                        | origin | fl_num
---------------------------------+--------+--------
 2012-01-20 10:04:00.000000+0000 |    DFW |    493
 2012-01-20 10:05:00.000000+0000 |    DFW |    654
 2012-01-20 10:09:00.000000+0000 |    DFW |    689
 2012-01-20 10:10:00.000000+0000 |    DFW |    712
 2012-01-20 10:08:00.000000+0000 |    DFW |   1087
 2012-01-20 10:01:00.000000+0000 |    DFW |   1331
 2012-01-20 10:02:00.000000+0000 |    DFW |   1599
 2012-01-20 10:08:00.000000+0000 |    DFW |   4921
 2012-01-20 10:00:00.000000+0000 |    DFW |   2748
 2012-01-20 10:04:00.000000+0000 |    DFW |    493
 2012-01-20 10:05:00.000000+0000 |    DFW |    654
 2012-01-20 10:09:00.000000+0000 |    DFW |    689
 2012-01-20 10:10:00.000000+0000 |    DFW |    712
 2012-01-20 10:08:00.000000+0000 |    DFW |   1087
 2012-01-20 10:01:00.000000+0000 |    DFW |   1331
 2012-01-20 10:02:00.000000+0000 |    DFW |   1599
 2012-01-20 10:08:00.000000+0000 |    DFW |   4921
 2012-01-20 10:00:00.000000+0000 |    DFW |   2748
 2012-01-20 10:04:00.000000+0000 |    DFW |    493
 2012-01-20 10:05:00.000000+0000 |    DFW |    654
 2012-01-20 10:09:00.000000+0000 |    DFW |    689
 2012-01-20 10:10:00.000000+0000 |    DFW |    712
 2012-01-20 10:08:00.000000+0000 |    DFW |   1087
 2012-01-20 10:01:00.000000+0000 |    DFW |   1331
 2012-01-20 10:02:00.000000+0000 |    DFW |   1599

(25 rows)

# cqlsh -k airport -e "select count(*) from flightlog where solr_query='origin:HNL AND year:2012 AND day_of_month:25';"

 count
-------
   288

(1 rows)

cqlsh:airport> select count(*) from flightlog where solr_query ='fl_date:"2012-01-25T00:00:00Z"';

 count
-------
 33821

(1 rows)

cqlsh:airport> select count(*) from flightlog where solr_query ='origin:HNL';

 count
-------
  9156

(1 rows)
cqlsh:airport> select count(*) from flightlog where solr_query ='origin:HNL AND fl_date:"2012-01-25T00:00:00Z"';

 count
-------
   288

(1 rows)


# cqlsh -e "CREATE SEARCH INDEX ON airport.airport_codes;"
# cqlsh -e "describe airport_codes;"

CREATE TABLE airport.airport_codes (
    airport_code text PRIMARY KEY,
    count int,
    solr_query text
) WITH additional_write_policy = '99PERCENTILE'
    AND bloom_filter_fp_chance = 0.01
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
    AND compression = {'chunk_length_in_kb': '64', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND crc_check_chance = 1.0
    AND default_time_to_live = 0
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND nodesync = {'enabled': 'true', 'incremental': 'true'}
    AND read_repair = 'BLOCKING'
    AND speculative_retry = '99PERCENTILE';
CREATE CUSTOM INDEX airport_airport_codes_solr_query_index ON airport.airport_codes (solr_query) USING 'com.datastax.bdp.search.solr.Cql3SolrSecondaryIndex';

# cqlsh -e "select count(*) from airport_codes where solr_query='airport_code:A*';"

 count
-------
    22

(1 rows)

```

### SOLR Query via web console
```
$ curl http://localhost:8983/solr/airport.flightlog/select?q=id:3&wt=json

<response>
  <lst name="responseHeader">
    <int name="status">0</int>
    <int name="QTime">2</int>
  </lst>
  <result name="response" numFound="1" start="0">
    <doc>
      <int name="id">3</int>
      <int name="fl_num">1</int>
      <int name="distance">2475</int>
      <int name="year">2012</int>
      <date name="dep_time">2012-11-11T08:55:00Z</date>
      <str name="origin">JFK</str>
      <int name="airline_id">19805</int>
      <str name="dest">LAX</str>
      <int name="day_of_month">1</int>
      <str name="origin_city_name">New York</str>
      <str name="dest_state_abr"> CA</str>
      <str name="carrier">AA</str>
      <str name="dest_city_name">Los Angeles</str>
      <date name="fl_date">2012-11-11T00:00:00Z</date>
      <int name="actual_elapsed_time">347</int>
      <date name="arr_time">2012-11-11T11:42:00Z</date>
      <int name="origin_airport_id">12478</int>
      <int name="air_time">330</int>
      <str name="origin_state_abr"> NY</str>
    </doc>
  </result>
</response>
```

### SPARK-SQL example: Originating airport that had the most flights on 2012-01-23
```
# dse spark-sql -e "select fl_date,origin,count(*) as sum from airport.flightlog where fl_date=to_date('2012-01-23 00:00:00') group by fl_date, origin order by fl_date,sum desc limit 5;"
The log file is at /home/centos/.spark-sql-shell.log
2012-01-23 00:00:00	ATL	2155
2012-01-23 00:00:00	ORD	1860
2012-01-23 00:00:00	DFW	1827
2012-01-23 00:00:00	DEN	1342
2012-01-23 00:00:00	LAX	1287
Time taken: 41.578 seconds, Fetched 5 row(s)
```

## Accessing the SPARK Console

Doc reference: https://docs.datastax.com/en/dse/5.1/dse-dev/datastax_enterprise/spark/dseSearchAnalyticsWikipediaDemo.html

```
# dse spark
The log file is at /root/.spark-shell.log
Creating a new Spark Session
Spark context Web UI available at http://dse.glocal.lab:4040
Spark Context available as 'sc' (master = dse://?, app id = app-20200501185541-0000).
Spark Session available as 'spark'.
Spark SqlContext (Deprecated use Spark Session instead) available as 'sqlContext'
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 2.4.0.13
      /_/

Using Scala version 2.11.12 (OpenJDK 64-Bit Server VM, Java 1.8.0_242)
Type in expressions to have them evaluated.
Type :help for more information.

scala> :help
All commands can be abbreviated, e.g., :he instead of :help.
:edit <id>|<line>                                              edit history
:help [command]                                                print this summary or command-specific help
:history [num]                                                 show the history (optional num is commands to show)
:h? <string>                                                   search the history
:imports [name name ...]                                       show import history, identifying sources of names
:implicits [-v]                                                show the implicits in scope
:javap <path|class>                                            disassemble a file or class name
:line <id>|<line>                                              place line(s) at the end of history
:load <path>                                                   interpret lines in a file
:paste [-raw] [path]                                           enter paste mode or paste a file
:power                                                         enable power user mode
:quit                                                          exit the interpreter
:replay [options]                                              reset the repl and replay all previous commands
:require <path>                                                add a jar to the classpath
:reset [options]                                               reset the repl to its initial state, forgetting all session entries
:save <path>                                                   save replayable session to a file
:sh <command line>                                             run a shell command (result is implicitly => List[String])
:settings <options>                                            update compiler options, if possible; see reset
:silent                                                        disable/enable automatic printing of results
:type [-v] <expr>                                              display the type of an expression without evaluating it
:kind [-v] <expr>                                              display the kind of expression's type
:warnings                                                      show the suppressed warnings from the most recent line which had any
:showSchema [all]|<keyspace_name>|<keyspace_name> <table_name> show Cassandra schema

scala> ^D
scala> :quit
```

### WIP: SPARK batch update to change all airport codes from 'BOS' to 'TST'

Some docs..  
https://docs.datastax.com/en/dse/6.8/dse-dev/datastax_enterprise/spark/usingSparkSession.html
https://docs.datastax.com/en/dse/6.8/dse-dev/datastax_enterprise/spark/usingDSESpark.html
https://docs.datastax.com/en/dse/6.8/dse-dev/datastax_enterprise/spark/usingSparkContext.html
https://docs.datastax.com/en/dse/6.8/dse-dev/datastax_enterprise/spark/sparkRemoteCommands.html
https://github.com/datastax/spark-cassandra-connector/tree/master/doc

```
scala> spark.sql("select count(*) from airport.flightlog")
scala> res0.collect().foreach(println)
[1048576]

scala> spark.sql("select count(*) from airport.flightlog where origin='BOS'")
res15: org.apache.spark.sql.DataFrame = [count(1): bigint]

scala> res15.collect().foreach(println)
[19874]

scala> spark.sql("select count(*) from airport.flightlog where origin='TST'")
res17: org.apache.spark.sql.DataFrame = [count(1): bigint]

scala> res17.collect().foreach(println)
[0]

scala> spark.sql("update airport.flightlog set origin='TST' where origin='BOS'")
org.apache.spark.sql.catalyst.parser.ParseException:
mismatched input 'update' expecting {'(', 'SELECT', 'FROM', 'ADD', 'DESC', 'WITH', 'VALUES', 'CREATE', 'TABLE', 'INSERT', 'DELETE', 'DESCRIBE', 'EXPLAIN', 'SHOW', 'USE', 'DROP', 'ALTER', 'MAP', 'SET', 'RESET', 'START', 'COMMIT', 'ROLLBACK', 'REDUCE', 'REFRESH', 'CLEAR', 'CACHE', 'UNCACHE', 'DFS', 'TRUNCATE', 'ANALYZE', 'LIST', 'REVOKE', 'GRANT', 'LOCK', 'UNLOCK', 'MSCK', 'EXPORT', 'IMPORT', 'LOAD'}(line 1, pos 0)

== SQL ==
update airport.flightlog set origin='TST' where origin='TST'
^^^

  at org.apache.spark.sql.catalyst.parser.ParseException.withCommand(ParseDriver.scala:241)
  at org.apache.spark.sql.catalyst.parser.AbstractSqlParser.parse(ParseDriver.scala:117)
  at org.apache.spark.sql.execution.SparkSqlParser.parse(SparkSqlParser.scala:48)
  at org.apache.spark.sql.catalyst.parser.AbstractSqlParser.parsePlan(ParseDriver.scala:69)
  at org.apache.spark.sql.SparkSession.sql(SparkSession.scala:642)
  ... 60 elided

scala> spark.sql("UPDATE airport.flightlog SET origin='TST' WHERE origin='BOS'")

```
So can't perform update via scala _search_ console, what about the spark-sql console..

```
$ dse spark-sql -e "select count(*) from airport.flightlog where origin='BOS'"
The log file is at /home/centos/.spark-sql-shell.log
19874
Time taken: 16.435 seconds, Fetched 1 row(s)

$ dse spark-sql -e "select count(*) from airport.flightlog where origin='TST'"
The log file is at /home/centos/.spark-sql-shell.log
0
Time taken: 16.687 seconds, Fetched 1 row(s)

$ dse spark-sql -e "update airport.flightlog set origin='TST' where origin='BOS'"
The log file is at /home/centos/.spark-sql-shell.log
Error in query:
mismatched input 'update' expecting {'(', 'SELECT', 'FROM', 'ADD', 'DESC', 'WITH', 'VALUES', 'CREATE', 'TABLE', 'INSERT', 'DELETE', 'DESCRIBE', 'EXPLAIN', 'SHOW', 'USE', 'DROP', 'ALTER', 'MAP', 'SET', 'RESET', 'START', 'COMMIT', 'ROLLBACK', 'REDUCE', 'REFRESH', 'CLEAR', 'CACHE', 'UNCACHE', 'DFS', 'TRUNCATE', 'ANALYZE', 'LIST', 'REVOKE', 'GRANT', 'LOCK', 'UNLOCK', 'MSCK', 'EXPORT', 'IMPORT', 'LOAD'}(line 1, pos 0)

== SQL ==
update airport.flightlog set origin='TST' where origin='BOS'
^^^
```
Hmm :/

