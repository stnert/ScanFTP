import ftplib

def anonLogin(hostname)
try:
ftp = ftplib.FTP(hostname)
ftp.login('anonymous')
print('\n' [+] str(hostname)+ 'FTP Anonymous Login allowed')
ftp.quit()
 return True
except Exception:
    print('\n'[-] 'FTP Anonymous Login blocked'
    return False

    __name__ == '__main__':

    anonLogin()

    //Pingue o domínio desejado em um tty, em seguida adicione o dominio no anonLogin
