import ftplib
import os

myURL = 'periship.sharefileftp.com'
myUserName = 'periship/jack.wang888@gmail.com'
myPassword = 'Sharefile.123'

with ftplib.FTP(myURL) as ftp:
    file_orig = 'CompanyABC/IN/newfile2.png'
    file_copy = 'AAAAA.png'

    try:
        ftp.login(myUserName, myPassword)
        # ftp.cwd('CompanyABC/IN')
        # wdir = ftp.pwd()
        # print(wdir)

        with open(file_copy, 'wb') as fp:
            res = ftp.retrbinary('RETR ' + file_orig, fp.write)
            print(f"Result: {res}")
            if not res.startswith('226'):
                print('Download failed')
                if os.path.isfile(file_copy):
                    os.remove(file_copy)

    except ftplib.all_errors as e:
        print('FTP error:', e)

        if os.path.isfile(file_copy):
            os.remove(file_copy)

print("Done!")
