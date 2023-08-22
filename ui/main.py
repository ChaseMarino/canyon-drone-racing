from UI import *
from consumer import *
from threading import Thread

def main():
    consumer_thread = Thread(target = consume)
    consumer_thread.start()
    init_ui()
    run_ui()


if __name__ == '__main__':
    # try:
        main()
    # except:
    #     print("err")