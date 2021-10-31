import dropbox 
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token= access_token

    def upload_file(self,file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)    
        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path=os.path.join(root, filename)
                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)
                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
def main():
    access_token = 'DMjh8wezfB0AAAAAAAAAAZQ_nMDyEOVdSnJfN_25UKI4sJazmaDL8cVvbKqsj5lA'
    transferData = TransferData(access_token)

    file_from = str(input ("enter file name: "))
    file_to = input ("ENTER THE COMPLETE ADDRESS OF THE FILE : ")

    # API v2
    transferData.upload_file(file_from, file_to)

    print ("file has been moved")
main()