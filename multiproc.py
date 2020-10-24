#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocess import Pool
from time import sleep
"""
  This is an example of process based parallelism.
  Note use of multiprocess from the Pathos library,
  not the more common multiprocessing library.

  https://pypi.org/project/pathos/

  Multiprocess uses dill for serialisation and
  supports class methods and other complexity.
"""

def worker_main(work):
    sleep(5)

def main():
    workers = 5
    while True:
        try:
            # Worklist contains data to be distributed
            worklist = []
            # Launch workers
            process = Pool(workers)
            # Map data to worker_main function
            process.map(worker_main, worklist)
            # Block until all work completed
            process.close()
            process.join()
        except Exception as ex:
            print(str(ex))

if __name__ == '__main__':
    main()
