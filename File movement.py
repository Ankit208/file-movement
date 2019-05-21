import os,shutil,pdb

dict_extension = {
    'text_extension':('.txt'),
    'audio_extension':('.mp3','.aac','.ogg','.wma','.m4a','.wav','.flac'),
    'video_extension':('.mp4','.mkv','.flv','.mpeg'),
    'python_extension':('.py'),
    'excel_extension':('.csv','.xls'),
    'website_extension':('.html','.css'),
    'image_extension':('.jpg'),
    
}

#this function will return list of doc of particular extension
def file_list(folder_path,file_extension):
    return[file for file in os.listdir(folder_path) for extension in file_extension if file.endswith(extension)]

folderpath=input('Enter file path : ') #lets input folder path

for file_type,file_extension in dict_extension.items():         #to read dictionary
    folder_name=file_type.split('_')[0]+'_files'
    folder_newpath=os.path.join(folderpath,folder_name)            #get new folder path
    
    if os.path.exists(folder_newpath):
        pass
    elif file_list(folderpath,file_extension):    
        os.mkdir(folder_newpath)
    else:
        pass
    
    for item in file_list(folderpath,file_extension):           #to get list of file of specfic type by calling function
        pdb.set_trace()    
        item_old_path = os.path.join(folderpath,item)
        item_new_path = os.path.join(folder_newpath,item)
        try:
            shutil.move(item_old_path,item_new_path)
        except:
            print('path missing')

