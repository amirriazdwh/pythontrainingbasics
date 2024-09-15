import concurrent.futures
import queue
import logging
from time import time

def executejob(q, brow, batchrunid):
    while not q.empty():
        job = q.get()
        try:
            # Your job execution logic here
            pass
        except Exception as e:
            logging.error(f"Error executing job {job}: {e}")
        finally:
            q.task_done()

def main():
    start = time()
    q = queue.Queue()

    # Till the time job failure count stays less than the batch threshold, the below loop will work
    while failjobcnt <= brow.batch_jobfail_threshold:
        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=brow.batch_parallelism) as executor:
                for i in range(brow.batch_parallelism):
                    executor.submit(executejob, q, brow, batchrunid)
                for x in jdatacur:
                    q.put(x)
                    logging.info('putting x value %s', x)
                q.join()
            break
        except Exception as e:
            logging.error(e)
            continue
    end = time()
    logging.info(f"Total execution time: {end - start} seconds")

if __name__ == "__main__":
    main()
