from threading import Thread
from time import perf_counter

primes = []


def get_primes(start: int, end: int):
    global primes
    for number in range(start, end):
        prime = True
        for i in range(2, number):
            if number % i == 0:
                prime = False
                break
        if prime:
            primes.append(number)


if __name__ == "__main__":
    while True:
        try:
            start_inp = int(input("Input start number: "))
            break
        except ValueError:
            print("Error! Input integer number")

    while True:
        try:
            end_inp = int(input("Input end number: "))
            break
        except ValueError:
            print("Error! Input integer number")

    start_time = perf_counter()

    gap = int((end_inp - start_inp) // 5)
    st1 = start_inp
    end1 = start_inp + gap
    st2 = end1
    end2 = st2 + gap
    st3 = end2
    end3 = st3 + gap
    st4 = end3
    end4 = st4 + gap
    st5 = end4
    end5 = end_inp + 1

    thread1 = Thread(target=get_primes(st1, end1))
    thread2 = Thread(target=get_primes(st2, end2))
    thread3 = Thread(target=get_primes(st3, end3))
    thread4 = Thread(target=get_primes(st4, end4))
    thread5 = Thread(target=get_primes(st5, end5))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()

    end_time = perf_counter() - start_time

    print(primes)
    print(len(primes))
    print(end_time)
