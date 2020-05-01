from concurrent.futures import ThreadPoolExecutor,as_completed
import random
import threading
import time


def test(s,key):
    print('s={},key={}'.format(s,key))
    threading.Event().wait(s)
    time.sleep(10)
    if key ==3:
        raise Exception('{} failed++++'.format(key))
    print('ok {}'.format(threading.current_thread()))

futures ={}

def run(fs):
    print('------run--------')
    while True:
        # time.sleep(1)
        print('+++++++++++++++start++++++++++++++')
        print('{}'.format(fs))
        for future in as_completed(fs):
            print(1,future.done())
            id = fs[future]
            try:
                print('id={}'.format(id),future.result())
            except Exception as e:
                print('e={}'.format(e))
                print(id,'failed')
threading.Thread(target=run,args=(futures,)).start()
#
with ThreadPoolExecutor(max_workers=3) as execctor:
    futures[execctor.submit(test,5,1)]= 1
    # futures[execctor.submit(test, 10, 2)] = 1
