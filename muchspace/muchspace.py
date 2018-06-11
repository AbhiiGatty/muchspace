#! /usr/bin/env python3

import fire
from pathlib import Path
import scripts.byteSize as sizesClass
import scripts.threadCreator as threadClass
class MuchSpace:
    """ Fire Class for muchspace Operations """
    def __init__(self):
        print("muchspace v0.1 Alpha")

    """ Function to stack the given directory based on extensions"""
    def getfilefrom(self, file_name):
        # Initialization
        globalvars = dict()
        #globalvars['Max_Retries'] = int(retry_no)
        globalvars['Total_Size'] = 0
        globalvars['Processed_URLs'] = 0
        #globalvars['Retry_Num'] = 0
        globalvars['Progress'] = 0
        globalvars['Total_URLs'] = 0
        globalvars['Rate'] = 0
        List_Of_URLs = []
        #List_Of_Invalid_URLs= []

        # Check if the file exists
        file_of_links = Path(file_name)
        if file_of_links.is_file():
            try:
                # Preprocessing
                with open(file_of_links,'r') as f: # Loading URLs into list for faster access
                    List_Of_URLs = list(set(f.read().splitlines()))    # Removing duplicates
                    globalvars['Total_URLs'] = len(List_Of_URLs)  # Total number of links
                globalvars['Rate'] = 100/globalvars['Total_URLs'] # Calculate each link percentage
            except IOError:
                print("IO Error : Unable to read from file")
                print("Exiting...")
                return
        else:
            print("Error! Invalid file path!")
            print("Exiting...")
            return


        # Running the list of URLs
        threadClass.thread_series_creator(List_Of_URLs=List_Of_URLs, globalvars=globalvars, function_name="grab_info")

        # Retrying if invalid links are found
        # while len(List_Of_Invalid_URLs) > 0:
        #     print("\nTotal unprocessed/invalid URLs: {}\n".format(len(List_Of_Invalid_URLs)))
        #     if Retry_Num < Max_Retries:
        #         Retry_Num += 1
        #         print("*******Retrying unprocessed URLs {}/{}*******\n".format(Retry_Num, max_retries))
        #         thread_series_creator(List_Of_Invalid_URLs)
        #     else:
        #         break

        # Final Report 
        print("******Final Diagnostic Report******")
        print("Total URLs: {0} Processed URLs: {1} Rate of completion: {2:.2f}%".format(globalvars['Total_URLs'], globalvars['Processed_URLs'], globalvars['Progress']))
        #print("Total no. of Invalid URLs: {}".format(len(List_Of_Invalid_URLs)))
        print("Total size of {}/{} links is: {}".format(globalvars['Processed_URLs'], globalvars['Total_URLs'], sizesClass.human_byte_size(globalvars['Total_Size']))) 
        

def main():
    fire.Fire(MuchSpace)

if __name__ == '__main__':
    main()
















  