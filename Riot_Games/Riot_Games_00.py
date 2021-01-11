"""
This question was asked by Riot Games.

Design and implement a HitCounter class that keeps track of requests (or hits). It should support the following operations:

    record(timestamp): records a hit that happened at timestamp
    total(): returns the total number of hits recorded
    range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)

Follow-up: What if our system has limited memory?

"""
from time import time
from random import random, randrange
import bisect

REQUESTS_PER_FILE = 100


class PersistedFile:
    def __init__(self):
        self.start_timestamp = None
        self.stop_timestamp = None
        self.request_timestamps = list()

    def __repr__(self):
        return "start={}, end={}, size={}".format(
            self.start_timestamp, self.stop_timestamp, len(self.request_timestamps))


class RequestQuery:
    def __init__(self):
        self.current_file = PersistedFile()
        self.prev_files = list()

    def record(self, timestamp):
        if not self.current_file.start_timestamp:
            self.current_file.start_timestamp = timestamp
        self.current_file.request_timestamps.append(timestamp)
        self.current_file.stop_timestamp = timestamp

        if len(self.current_file.request_timestamps) == REQUESTS_PER_FILE:
            self.prev_files.append(self.current_file)
            self.current_file = PersistedFile()

    def total(self):
        return len(self.prev_files * REQUESTS_PER_FILE) + \
               len(self.current_file.request_timestamps)

    def range(self, lower, upper):
        all_files = self.prev_files + [self.current_file]
        start_times = [x.start_timestamp for x in all_files]
        stop_times = [x.stop_timestamp for x in all_files]

        start_file_index = bisect.bisect_left(start_times, lower) - 1
        stop_file_index = bisect.bisect_left(stop_times, upper)
        start_file = all_files[start_file_index]
        stop_file = all_files[stop_file_index]

        start_file_pos = bisect.bisect(start_file.request_timestamps, lower)
        stop_file_pos = bisect.bisect(stop_file.request_timestamps, upper)

        num_req = 0
        num_req += len(start_file.request_timestamps[start_file_pos:])
        num_req += len(stop_file.request_timestamps[:stop_file_pos])
        num_req += (stop_file_index - start_file_index) * REQUESTS_PER_FILE

        return num_req
