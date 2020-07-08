import time
import concurrent.futures

start = time.perf_counter()


# Sleeps the program for {sec} second(s)
def do_something(secs):
	print(f'Sleeping {secs} second(s)...')
	time.sleep(secs)
	return f'Done Sleeping...{secs}'


with concurrent.futures.ThreadPoolExecutor() as executor:
	secs = [1, 2, 3, 4, 5]
	secs.sort(reverse=True)
# One way use builtin Methods and Comprehension lists
# This prints in the order completed(321 and then from completed back to start 123)
	# results = [executor.submit(do_something, sec) for sec in secs]
	# for f in concurrent.futures.as_completed(results):
	# 	print(f.result())
# Another way use Maps
# This prints in the order it started(321..321)
	results = executor.map(do_something, secs)
	for result in results:
		print(result)

finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} second(s)')

