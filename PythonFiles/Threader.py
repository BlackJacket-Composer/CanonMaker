import threading
from music21 import *
from queue import Queue
import time
from PythonFiles import Canon_Maker as CM

wtc1_Bfmin = converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/Bach WTC1 Bfmin.xml')
WTC = '/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Bach WTC Subjects/'


list_songs = []
for root, dirs, files in os.walk(wtc):
    for file_name in files:
        path = os.path.join(root, file_name)
        tempStream = converter.parse(path)
        list_songs.append(tempStream)
print_lock = threading.Lock()

def exampleJob(worker):
    CM.multi_tester(worker)
    with print_lock:
        print(threading.current_thread().name,worker)

q = Queue()

def threader():
    while True:
        worker = q.get()
        exampleJob(worker)
        q.task_done()

for x in list_songs:
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

start = time.time()

for worker in range(20):
    q.put(worker)

q.join()

print('Entire job took:', time.time() - start, 'seconds')