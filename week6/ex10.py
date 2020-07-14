import ftplib

myURL = 'periship.sharefileftp.com'
myUserName = 'periship/jack.wang888@gmail.com'
myPassword = 'Sharefile.123'

# session = ftplib.FTP(myURL, myUserName, Password)
# with open('ftpsftp.py', 'r') as f:
#     session.storbinary('STOR %s' % 'remotefile.py', f)
# session.quit()

#ftplib.FTP_TLS
with ftplib.FTP(myURL, myUserName, myPassword) as ftp:
    # List files
    files = []
    ftp.dir(files.append)  # Takes a callback for each file
    for f in files:
        print(f)

    ftp.cwd('CompanyABC')
    wdir = ftp.pwd()
    print(wdir)

    print(f'For CompanyABC: ')
    files = []
    ftp.dir(files.append)  # Takes a callback for each file
    for f in files:
        print(f)

session = ftplib.FTP(myURL, myUserName, myPassword)
with open('docs/xmlfile-70_1.png', 'rb') as f:
    wdir = session.pwd()
    print(wdir)

    session.cwd('CompanyABC/IN')
    session.storbinary('STOR %s' % 'mstest1.png', f)
session.quit()


print("Done!")

