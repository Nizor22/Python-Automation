# The img_downloader.py is using threads to download images faster
Since downloading images takes time to recieve a respond from the server, 
the script goes over other links to speed up the proccess. 
    1) Takes the links from the links.txt & adds them to a list.
    2) Uses ThreadPool and .map function to iterate over all the links and for each call the download_image function.
    3) Downloads the images to the working directory.

# TO USE 
Change the links in the links.txt to the links of the images you want to download.