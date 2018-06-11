import threading
from scripts.grabInfo import grab_info

""" Creating a threading list using list and starting all threads """
def thread_series_creator(List_Of_URLs, globalvars):
    start = 0
    weight = end = (globalvars['Total_URLs']%500)
    while True:
        if start > globalvars['Total_URLs']:
            break
        threads = [threading.Thread(target=grab_info, args=(URL, globalvars))for URL in List_Of_URLs[start:end]]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        start = end
        end = end + weight