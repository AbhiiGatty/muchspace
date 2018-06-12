# import threading
from pathlib import Path
from multiprocessing.dummy import Pool as ThreadPool
from  more_itertools import unique_everseen
import requests, json, datetime
from scripts.byteSize import human_byte_size
           
# Initialization
Total_Size = 0
Processed_URLs = 0
Progress = 0
Total_URLs = 0
Rate = 0
Report = False
ReportJson = []

""" Main fuction to gather info about URL """
def url_info(URL):
    linkStatus = {}
    global Total_Size, Processed_URLs, Progress, Total_URLs, Rate, Report
    if URL not in [' ','']:      # Ignoring any whitespaces within the list
        try:
            File_Size = 0 # Initialize
            fileLink = requests.head(URL, stream=True) # Get the link header info
            fileLink.raise_for_status() # To catch 404 and 500 earlier
            # Why i use get instead of head, Source: https://stackoverflow.com/questions/14270698/get-file-size-using-python-requests-while-only-getting-the-header
            HEAD = requests.get(URL, stream=True).headers  # Invoked if 400 series
            File_Size = int(HEAD['Content-length']) # Get only the headers not the entire content
            Progress += Rate
            Processed_URLs = Processed_URLs + 1
            Total_Size += File_Size
            print('URLs Done:{0}/{1} File Size:{2} Total Size:{3} Progress:{4:.2f}%'.format(Processed_URLs, Total_URLs, human_byte_size(File_Size), human_byte_size(Total_Size), Progress))
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("Oops: Something Else",err)
        if Report is True:
            linkStatus['link'] = URL
            linkStatus['size'] = human_byte_size(File_Size)
            linkStatus['status'] = fileLink.status_code
            linkStatus['last-checked'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            ReportJson.append(linkStatus)


def thread_series_creator(List_Of_URLs):
    global Total_Size, Processed_URLs, Progress, Total_URLs, Rate, Report
    # Make the Pool of workers
    pool = ThreadPool(100) 
    # Open the urls in their own threads and return the results
    results = pool.map(url_info, List_Of_URLs)
    # close the pool and wait for the work to finish 
    pool.close() 
    pool.join()
    
def main(file_path, report=False):

    global Total_Size, Processed_URLs, Progress, Total_URLs, Rate, Report
    # If exist check if it is a file
    file_of_links = Path(file_path)
    if file_of_links.is_file():
            try:
                # Preprocessing
                with open(file_of_links,'r') as f: # Loading URLs into list for faster access
                    List_of_URLs = list(unique_everseen(f.read().splitlines()))    # Removing duplicates without changing order
                    Total_URLs = len(List_of_URLs)  # Total number of links
                    Rate = 100/Total_URLs # Calculate each link percentage
            except IOError:
                print("IO Error : Unable to read from file")
                print("Exiting...")
                return
    else:
        print("Error! Invalid file path!")
        print("Exiting...")
        return
    Report = report
    thread_series_creator(List_of_URLs)

    if Report is True: # Creating report 
        Date = datetime.date.today().strftime('%d.%b.%Y')
        with open("muchspace.Report."+Date+".json", "w") as write_file:
            json.dump(ReportJson, write_file, indent=4)

    # Final Console Report 
    print("******Final Diagnostic Report******")
    print("Total URLs: {0} Processed URLs: {1} Rate of completion: {2:.2f}%".format(Total_URLs, Processed_URLs, Progress))
    print("Total size of {}/{} links is: {}".format(Processed_URLs, Total_URLs, human_byte_size(Total_Size))) 

