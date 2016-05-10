from concurrent import futures
from concurrent.futures import ThreadPoolExecutor


class ParallelTemplate():
    def __init__(self, workers=5):
        super().__init__()
        self.workers = workers

    def run(self, func, inputList):
        with ThreadPoolExecutor(max_workers=self.workers) as executor:
            futureItem = {executor.submit(func, item): item for item in inputList}
            resultList = list()
            for future in futures.as_completed(futureItem):
                try:
                    item = future.result()
                    resultList.append(item)
                except Exception as exc:
                    print("exception: " + str(exc))
            return resultList
