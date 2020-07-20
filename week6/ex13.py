import ftplib

myURL = 'periship.sharefileftp.com'
myUserName = 'periship/jack.wang888@gmail.com'
myPassword = 'Sharefile.123'

file_orig = 'CompanyABC/Test/ABC_Company.txt'

with ftplib.FTP(myURL, myUserName, myPassword) as ftp:
    try:
        res = ftp.rename(file_orig, 'CompanyABC.txt')
    except ftplib.all_errors as error:
        print(f'Error renaming file on server: {error}')

print("Done with renaming!")

file_orig = 'CompanyABC/IN/newfile2.png'
with ftplib.FTP(myURL, myUserName, myPassword) as ftp:
    try:
        ftp.sendcmd('TYPE I') # "Image" or binary data
        s = ftp.size(file_orig)
        print(f"File size is: {s}")
    except ftplib.all_errors as error:
        print(f'Error checking image size: {error}')
    try:
        ftp.sendcmd('TYPE A')  # "ASCII" text
        print(f"ASCII file size is: {ftp.size(file_orig)}")
    except ftplib.all_errors as error:
        print(f"Error checking text file size: {error}")