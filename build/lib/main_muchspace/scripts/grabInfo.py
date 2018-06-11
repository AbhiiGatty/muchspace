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

