import threading
import requests
from scripts.byteSize import human_byte_size

""" Main fuction to gather info about URL """
def grab_info(URL, globalvars):
    if URL not in [' ','']:      # Ignoring any whitespaces within the list
        try:
            File_Size = int(requests.get(URL, stream=True).headers['Content-length']) # Get only the headers not the entire content
            globalvars['Progress'] += globalvars['Rate']
            globalvars['Processed_URLs'] = globalvars['Processed_URLs'] + 1
            globalvars['Total_Size'] += File_Size
            print('URLs Done:{0}/{1} File Size:{2} Total Size:{3} Progress:{4:.2f}%'.format(globalvars['Processed_URLs'], globalvars['Total_URLs'], human_byte_size(File_Size), human_byte_size(globalvars['Total_Size']), globalvars['Progress']))
        except requests.exceptions.ConnectionError as err:
            print(err)
        except requests.exceptions.HTTPError as err:
            print(err)
        except:
            # List_Of_Invalid_URLs.append(URL)
            print('invalid')

""" Creating a threading list using list and starting all threads """
def thread_series_creator(List_Of_URLs, globalvars, function_name=None):
    start = 0
    weight = end = (globalvars['Total_URLs']%500)
    if function_name is None:
        print("ERROR: No function threads to create! Try a function_name to thread_creator_series Method!")
        return 
    while True:
        if start > globalvars['Total_URLs']:
            break
        threads = [threading.Thread(target=function_name, args=(URL, globalvars))for URL in List_Of_URLs[start:end]]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        start = end
        end = end + weight