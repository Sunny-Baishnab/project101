import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,fileFrom,fileTo):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            relative_path = os.path.relpath(local_path,file_from)
            dropbox_path = os.path.join(file_to,relative_path)
        with open(local_path,'rb') as f:
            dbx.files_upload(f.read(),dropbox_path, mode = WriteMode('overwrite'))
def main():
    access_token = '9gpGJEBnAtAAAAAAAAAAAYuqejxhgTu3oL6E2X5meaxCkzqw4WHuddNg-t4DX6A4'
    transferData = TransferData(access_token)

    file_from = input('enter your folder name which you want to transfer')
    file_to = input('enter the destination path')

    transferData.uploadFiles(file_from,file_to)

    print('folder has been uploaded')

main()