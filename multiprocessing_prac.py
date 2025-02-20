import multiprocessing
import time

def worker(i):
    print(f'Worker {i} Started Working!')
    time.sleep(3)
    print(f'Worker {i} ended work!')

def apply_multiprocess():
    processes = []
    for i in range(1,11):
        p = multiprocessing.Process(target=worker, args=[i])
        p.start()
        processes.append(p)

    print('All processes have finished their work!')

if __name__ == '__main__':
    apply_multiprocess()