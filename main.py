import time
import pymongo

MONGO_HOSTS_PORTS='host1:27017,host2:27017,host3:27017'
MONGO_PASSWORD='password#'
MONGO_REPLICA_SET='rset'
MONGO_USER='mongouser'
MONGO_DB='mongodb'


def timefunc(f):
    def f_timer(*args, **kwargs):
        start = time.time()
    result = f(*args, **kwargs)
    end = time.time()
    print end - start
    return result
    return f_timer

@timefunc
def do_mongo():
    client = MongoClient(MONGO_HOSTS_PORTS,
                         user=MONGO_USER,
                         password=MONGO_PASSWORD,
                         authSource=MONGO_DB)
    db = client.pymongo_test
    print db
