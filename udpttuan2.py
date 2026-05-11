import threading
import queue
import time
import random

class Chef(threading.Thread):
    def __init__(self, name, task_queue, lock):
        super().__init__()
        self.name = name
        self.task_queue = task_queue
        self.lock = lock

    def run(self):
        while True:
            try:
                dish = self.task_queue.get(timeout=2)
            except queue.Empty:
                print(f"{self.name} hết việc, nghỉ!")
                break

            cook_time = random.randint(1, 5)

            with self.lock:
                print(f"{self.name} bắt đầu nấu {dish} ({cook_time}s)")

            time.sleep(cook_time)

            with self.lock:
                print(f"{self.name} hoàn thành {dish}")

            self.task_queue.task_done()

def main():
    task_queue = queue.Queue()
    lock = threading.Lock()

    dishes = [f"Món {i}" for i in range(1, 21)]

    for dish in dishes:
        task_queue.put(dish)

    num_chefs = 3

    chefs = []
    for i in range(num_chefs):
        chef = Chef(f"Đầu bếp {i+1}", task_queue, lock)
        chef.start()
        chefs.append(chef)

    task_queue.join()

    print("\nTất cả món đã nấu xong!")

if __name__ == "__main__":
    main()