import math
import os
import logging
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

logging.basicConfig(level=logging.INFO, filename="4.2_integration.log", format="%(asctime)s - %(message)s")
def integrate(f, a, b, n_jobs, executor_type='sync', n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter

    if n_jobs == 1:
        if executor_type == 'sync':
            logging.info('Starting integration inside thread/process')
        else:
            logging.info('Starting integration with n_jobs=1')
        for i in range(n_iter):
            acc += f(a + i * step) * step
        return acc

    if executor_type == 'ThreadPoolExecutor':
        logging.info(f'Starting integration with n_jobs={n_jobs} using ThreadPoolExecutor')
        with ThreadPoolExecutor(max_workers=n_jobs) as executor:
            futures = [executor.submit(integrate, f, a + job * (b - a) / n_jobs, a + (job + 1) * (b - a) / n_jobs,
                                       n_jobs=1, n_iter=n_iter // n_jobs) for job in range(n_jobs)]
            for future in futures:
                acc += future.result()
            return acc

    if executor_type == 'ProcessPoolExecutor':
        logging.info(f'Starting integration with n_jobs={n_jobs} using ProcessPoolExecutor')
        with ProcessPoolExecutor(max_workers=n_jobs) as executor:
            futures = [executor.submit(integrate, f, a + job * (b - a) / n_jobs, a + (job + 1) * (b - a) / n_jobs,
                                       n_jobs=1, n_iter=n_iter // n_jobs) for job in range(n_jobs)]
            for future in futures:
                acc += future.result()
            return acc


if __name__ == '__main__':
    file = open("4.2_times.txt", "w")
    cpu_num = os.cpu_count()
    for n_jobs in range (1, cpu_num*2 + 1):
        file.write(f'n_jobs={n_jobs} \n')
        start = time.time()
        integrate(math.cos, 0, math.pi / 2, n_jobs, 'ThreadPoolExecutor')
        file.write(f'Thread time: {time.time() - start} \n')

        start = time.time()
        integrate(math.cos, 0, math.pi / 2, n_jobs, 'ProcessPoolExecutor')
        file.write(f'Process time: {time.time() - start} \n')