from datetime import datetime, timedelta

class Node:
    def __init__(self, key):
        sched_time, duration, name_of_job = key.split(",")
        raw_sched_time = datetime.strptime(sched_time, '%H:%M')
        key = raw_sched_time.time()
        end_time = (raw_sched_time + timedelta(minutes=int(duration))).time()
        self.data = key # key = time
        self.scheduled_end = end_time
        self.duration = duration
        self.name_of_job = name_of_job.rstrip()
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return f"Time: {self.data}, Duration: {self.duration}, End: {self.scheduled_end}, Jobname: {self.name_of_job}"


class BSTDemo:
    pass

