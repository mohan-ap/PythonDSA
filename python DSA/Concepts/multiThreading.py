import threading

def cube(num):
    print("Thread name {}".format(threading.currentThread().name))
    c=num*num*num
    for i in range(5):
        print("cube is {}".format(c))

def square(num):
    print("Thread name {}".format(threading.currentThread().name))
    s=num*num
    for i in range(5):
        print("square of a number is {}".format(s))

if __name__=="__main__":
    t1=threading.Thread(target=cube,args=(2,))
    t2=threading.Thread(target=square,args=(3,))
    print("Thread name {}".format(threading.currentThread().name))    #to get current thread name
    t1.start()
    t2.start()

    t1.join()
    t2.join()


#creating thread pools

import concurrent.futures

def worker():
    for i in range(5):
         print("working")

if __name__=="__main__":
    pool=concurrent.futures.ThreadPoolExecutor()
    pool.submit(worker)
    pool.submit(worker)
    pool.shutdown(wait=True)
    print("main thread")
