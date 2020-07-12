import requests
import time
import concurrent.futures


def download_image(img_url):
	img_bytes = requests.get(img_url).content
	img_name = f'{img_url.split("/")[4]}.jpg'
	with open(img_name, 'wb') as img_file:
		img_file.write(img_bytes)
		print(f'{img_name} was downloaded')


def main():
	start = time.perf_counter()
	img_urls = []
	with open('links.txt', 'r') as file:
		for line in file.readlines():
			img_urls.append(line.strip('\n'))
	# Calls the function with every url in the list
	with concurrent.futures.ThreadPoolExecutor() as executor:
		executor.map(download_image, img_urls)

	finish = time.perf_counter()
	print(f'Finished in {round(finish - start, 2)} seconds')


if __name__ == '__main__':
	main()
