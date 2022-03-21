import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BDZtPx8p_cGSDlEQvVQiAyo7Grt0ml--bkhQcsmrFIdVJb5x0T5OsNtTT4RoOZGXW1j_iaJfMezAVxJYJcpGHpNI15s788reL1NQ2I4Cowk4R74xjGoPLTCQAm00R7yMy1UWbXk'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer:")
    file_to = input("Enter the file path to upload to dropbox:")

    transferData.upload_file(file_from, file_to)
    print("file has been moved")