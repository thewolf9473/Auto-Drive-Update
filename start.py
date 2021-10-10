from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os
import schedule
from datetime import datetime
def google_auth():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth) 
    return gauth, drive

def upload_backup(drive, path):
    for file_name in os.listdir(path):
        try:
            f = drive.CreateFile({'parents': [{'id': '1-7S-bhxIQetJ3Y9rfIhh0FQIhc6Xpiis'}], 'title': file_name})
            f.SetContentFile(os.path.join(path, file_name))
            f.Upload()
            with open('log.txt', 'a') as file:
                file.write('Recorded at: %s ' %datetime.now())
                file.write('Succesfully Uploaded ')
                file.write(os.path.join(path, file_name))
            f = None
        except:
            with open('log.txt', 'la') as file:
                file.write('Recorded at: %s' %datetime.now())
                file.write('Backup Failed ')
                file.write(os.path.join(path, file_name))
def main():
    path = r"E:\courses\python\projects\opencv\backup"
    gauth, drive = google_auth()
    upload_backup(drive, path)

if __name__=="__main__":
    main()
    schedule.every().day.at("20:52").do(main)
    while True:
        schedule.run_pending()
