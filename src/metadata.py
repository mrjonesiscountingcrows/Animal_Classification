import matplotlib.pyplot as pltimport osimport jsondata_folder = "data/animals"metadata = []total_image_count = 0for folder in os.listdir(data_folder):    folder_name = folder    for image in os.listdir(data_folder + "/" + folder_name):        total_image_count = total_image_count + 1        imageDict = {}        imageDict["unique_id"] = total_image_count        imageDict["image_name"] = image        imageDict["type"] = folder_name        metadata.append(imageDict)if os.path.exists("metadata.json"):    os.remove("metadata.json")for i in range(len(metadata)):    myDict = metadata[i]    print(myDict)    with open('metadata.json', 'a') as f:        json.dump(myDict, f)        f.write(os.linesep)