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
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        if self.root == None:
            self.root = key
            self.helpful_print(key, True)
        else:
            self._insert(self.root, key)

    def _insert(self, curr, key):
        if key.data > curr.data and key.data >= curr.scheduled_end:
            if curr.right_child == None:
                curr.right_child = key
                self.helpful_print(key, True)
            else:
                self._insert(curr.right_child, key)
        elif key.data < curr.data and key.scheduled_end <= curr.data:
            if curr.left_child == None:
                curr.left_child = key
                self.helpful_print(key, True)
            else:
                self._insert(curr.left_child, key)
        else:
            self.helpful_print(key, False)

    def helpful_print(self, key, succeeded):
        if succeeded: # If job succeeded
            print(f"Added:\t\t {key.name_of_job}")
            print(f"Begin:\t\t {key.data}")
            print(f"End:\t\t {key.scheduled_end}")
            print("-"*60)
        else: # If job failed
            print(f"Rejected:\t {key.name_of_job}")
            print(f"Begin:\t\t {key.data}")
            print(f"End:\t\t {key.scheduled_end}")
            print("Reason:\t Time slot overlap, please verify")
            print("-" * 60)

    def in_order(self):
        print("Full job schedule for today")
        print("-"*60)
        self._in_order(self.root)
        print("-"*60)

    def _in_order(self, curr):
        if curr:
            self._in_order(curr.left_child)
            print(curr)
            self._in_order(curr.right_child)

    def length(self):
        return self._length(self.root)

    def _length(self, curr):
        if curr is None:
            return 0
        return 1 + self._length(curr.left_child) + self._length(curr.right_child)

    def find_val(self, key):
        return self._find_val(self.root, key)

    def _find_val(self, curr, key):
        if curr:
            if key == curr.data:
                return curr # returning the node if found
            elif key < curr.data:
                return self.find_val(curr.left_child, key)
            else:
                return self._find_val(curr.right_child, key)
        return

    def min_right_subtree(self, curr):
        if curr.left_child == None:
            return curr
        else:
            return self.min_right_subtree(curr.left_child)

    def delete_val(self, key):
        pass




