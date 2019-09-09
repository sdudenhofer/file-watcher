from ftplib import FTP


def fup(serv, port, user, pwd, file1, file2, location):
    connection = serv
    ftp = FTP()
    port = port
    username = user
    password = pwd
    ftp_census = file1
    ftp_demo = file2

    fc = open(ftp_census, 'rb')
    fd = open(ftp_demo, 'rb')
    stor_census = str("STOR" + fc)
    stor_demo = str("STOR" + fd)
    ftp.connect(connection, port)
    ftp.login(username, password)
    ftp.cwd(location)
    ftp.storbinary(stor_census, fc, 1024)

    fc.close()
    ftp.storbinary(stor_demo, fd, 1024)

    fd.close()