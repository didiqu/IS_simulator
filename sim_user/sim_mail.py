import time
import random
from colorama import Style, Fore
from essential_generators import DocumentGenerator
from mailLib import smtp_connect, imap_connect, send_mail, read_mailbox, download_attachements, delete_old_emails, delete_all_emails

def mail_cycle(args):
    smtp_server_ip = args["smtp_server_ip"]
    imap_server_ip = args["imap_server_ip"]
    imap_login = args["login"]
    imap_password = args["password"]
    FROM = args["FROM"]
    TO = args["TO"]
    SUBJECT = args["subject"]
    MSG = args["msg"]
    ATTACHEMENTS = args["attachements"]

    gen = DocumentGenerator()
    actions = ["send_mail","read_mailbox","download_attachements","delete_all_emails"]
    for i in range(int(args["nb_actions"])):
        action = random.choices(actions, weights=[10,10,5,2])
        time.sleep(random.randint(10,30))
        if action == ["read_mailbox"]:
            print(" => "+str(action[0])+"            -- "+time.strftime("%H:%M:%S", time.localtime()))
            imap = imap_connect(imap_server_ip, imap_login, imap_password)
            read_mailbox(imap)
            imap.close()
            imap.logout()
        elif action == ["download_attachements"]:
            print(" => "+str(action[0])+" --   "+time.strftime("%H:%M:%S", time.localtime()))
            imap = imap_connect(imap_server_ip, imap_login, imap_password)
            download_attachements(imap)
            imap.close()
            imap.logout()
        elif action == ["delete_all_emails"]:
            print(" => "+str(action[0])+"       -- "+time.strftime("%H:%M:%S", time.localtime()))
            imap = imap_connect(imap_server_ip, imap_login, imap_password)
            delete_all_emails(imap)
            imap.close()
            imap.logout()
        elif action == ["send_mail"]:
            print(" => "+str(action[0])+"               -- "+time.strftime("%H:%M:%S", time.localtime()))
            smtp = smtp_connect(smtp_server_ip)
            if len(TO) >= 1:
                to = random.choice(TO)
            if SUBJECT == "":
                subject = gen.sentence()
            if MSG == "":
                msg = gen.paragraph()
            send_mail(smtp, FROM, to, subject, msg, ATTACHEMENTS)
            smtp.quit()



# args = {"smtp_server_ip":"10.159.8.12", 
#         "imap_server_ip":"10.159.8.12", 
#         "login":"hacker",
#         "password":"hacker123",
#         "FROM":"hacker@internet.local",
#         "TO":"hacker@internet.local",
#         "SUBJECT":"test",
#         "MSG":"This is my message",
#         "ATTACHEMENTS":[("file","hacker.exe")] #("image","chaton.jpg")
        
#         }
# mail_cycle(args)