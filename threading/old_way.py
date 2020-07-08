import threading
import time

start = time.perf_counter()


# Sleeps the program for {sec} second(s)
def do_something(secs):
	print(f'Sleeping {secs} second(s)...')
	time.sleep(secs)
	print(f'Done Sleeping...')


threads = []

# _ is a throw away variable(throw away=not used in a loop)
# Running the do_something(sleep) method 10 times, but actually sleeping only 1 second.
for _ in range(10):
	t = threading.Thread(target=do_something, args=[1])
	t.start()
	threads.append(t)
# Makes sure every thread finishes before going to the rest of the program
for thread in threads:
	thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')
