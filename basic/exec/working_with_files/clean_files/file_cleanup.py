import os

folder_original = os.path.expanduser('~/Desktop/')
folder_destination = os.path.expanduser('~/Desktop/CleanedUp')
os.makedirs(folder_destination, exist_ok=True)
for entry in os.scandir(folder_original):

    location_original = os.path.join(folder_original, entry.name)
    location_destination = os.path.join(folder_destination, entry.name)

    if os.path.isfile(location_original):
        os.rename(location_original, location_destination)






# entries = os.scandir(folder)
# for entry in entries:
#     if os.path.isfile(entry):
#         print('File:', entry.name)
#     elif os.path.isdir(entry):
#         print('Directory:',entry.name)




# create folders
# os.mkdir("/home/alexandre-s-ponte/Desktop")