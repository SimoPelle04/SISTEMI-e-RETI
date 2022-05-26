from threading import Thread
import time
#ereditarietà

class Mythread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name = name
        self.running = True

    def run(self):
        while self.running:
            print(f"Sono il thread {self.name}")
            time.sleep(1)

    def stop(self):
        self.running = False

def main():
    t1 = Mythread("Alice")
    t2 = Mythread("Bob")
    t1.start()
    t2.start()
    #              main
    #               |
    #               |
    #               |   t1.start()
    #               |____
    #     t1.start()|    |
    #           ____|    |
    #          |    |    |
    #          |    |    |
    #          |    |    |

    for _ in range(5):
        print("Sono il main Alice")
        print("Sono il main Bob")
        time.sleep(1)

    t1.stop()
    t2.stop()

    #.join appena il thread finisce allora i flussi vengono riuniti

    #               |  
    #               |t1.start()
    #               |    |
    #     t1.start()|    |
    #          |    |    |
    #          |    |    |
    #          |    |____|
    #          |____|
    #               |
    #               |
    #              main

    t1.join()
    t2.join()




if __name__=="__main__":
    main()