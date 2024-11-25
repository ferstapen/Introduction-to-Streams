import threading
import time
from datetime import datetime

def write_words(word_count, file_name):
    for i in range(1, word_count + 1):
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(f'Какое-то слово № {i}')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_stop = datetime.now()
time_func = time_stop - time_start
print(f'Работа потоков {time_func}')

time_start_flow = datetime.now()
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(10, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(10, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(10, 'example8.txt'))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

time_stop_flow = datetime.now()
time_func_flow = time_stop_flow - time_start_flow
print(f'Работа потоков {time_func_flow}')
