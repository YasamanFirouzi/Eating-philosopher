import threading
import time
import random

class Philosopher(threading.Thread):
    def __init__(self, name, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while True:
            # The philosopher thinks randomly
            time.sleep(random.uniform(0, 1))
           # The philosopher checks whether the right fork and the left fork are empty or not
            if self.left_fork.acquire(blocking=False):
                if self.right_fork.acquire(blocking=False):
                   # The philosopher starts eating
                    print(self.name, "is eating.")
                    # The philosopher eats randomly
                    time.sleep(random.uniform(0, 1))
                    # The philosopher releases the right fork
                    self.right_fork.release()
           
                # After eating, the philosopher drops the left fork
                else:
                    self.left_fork.release()
            else:
                print(f"{self.name} is hungry.")


if __name__ == "__main__":
    # Create forks
    forks = [threading.Lock() for i in range(5)]
    # Creation of philosophers
    philosophers = [
        Philosopher("Philosopher {}".format(i), forks[i], forks[(i+1) % 5])
        for i in range(5)
    ]
    # The beginning of the process of eating philosophers
    for philosopher in philosophers:
        philosopher.start()
