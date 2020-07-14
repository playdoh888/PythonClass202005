import ftplib

myURL = 'periship.sharefileftp.com'
myUserName = 'periship/jack.wang888@gmail.com'
myPassword = 'Sharefile.123'

file_orig = 'mstest1.png'

with ftplib.FTP(myURL, myUserName, myPassword) as ftp:
    try:
        ftp.cwd('CompanyABC/IN')
        wdir = ftp.pwd()
        print(wdir)

        ftp.delete(file_orig)
    except ftplib.all_errors as e:
        print(f'Error deleting file: {e}')

print("Done!")