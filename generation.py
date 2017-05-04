import csv
import random
import datetime
import time

def way_one():
    print("way one done")
    in_file_one = open('way_one.csv', 'w')
    writer_one = csv.writer(in_file_one)
    local_time = datetime.datetime.time(datetime.datetime.now())
    try:
        writer_one.writerow(('Longitude', 'Latitude', 'Time'))
        for i in range(60000):
            writer_one.writerow((random.uniform(48.69300,48.71397), random.uniform(44.50172, 44.52881),local_time))
    finally:
        in_file_one.close()

def way_two():
    print("way two done")
    in_file_two = open('way_two.csv', 'w')
    writter_two = csv.writer(in_file_two)
    local_time = datetime.datetime.time(datetime.datetime.now())
    local_time.replace(microsecond=0)
    try:
        writter_two.writerow(('Longitude', 'Latitude', 'Time'))
        for i in range(60000):
            writter_two.writerow((random.uniform(48.69340, 48.63684), random.uniform(44.50172, 44.43629), local_time))
    finally:
        in_file_two.close()

def way_three():
    print("way three done")
    in_file_three = open('way_three.csv', 'w')
    writter_three = csv.writer(in_file_three)
    local_time = datetime.datetime.time(datetime.datetime.now())
    try:
        writter_three.writerow(('Longitude', 'Latitude', 'Time'))
        for i in range(60000):
            writter_three.writerow((random.uniform(48.69340, 48.82432), random.uniform(44.50172,44.62706),local_time))
    finally:
        in_file_three.close()

