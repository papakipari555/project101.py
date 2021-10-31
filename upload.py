import dropbox






class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'DMjh8wezfB0AAAAAAAAAAZQ_nMDyEOVdSnJfN_25UKI4sJazmaDL8cVvbKqsj5lA'
    transferData = TransferData(access_token)

    file_from = input ("enter file name: ")
    file_to = input ("ENTER THE COMPLETE ADDRESS OF THE FILE : ")

    # API v2
    transferData.upload_file(file_from, file_to)

    print ("file has been moved")
main()
