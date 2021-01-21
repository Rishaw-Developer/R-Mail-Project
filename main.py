import datetime
import os
import sys
import time

print("Hy user , Welcome to the R-Maill where you send your mails to anyones you want")


class Email:
        
    def send_mail(self, sender_to_where,message):
        '''This method will send the message'''
        with open(f'{sender_to_where}.txt', "a") as send:
            send.write(f"At {datetime.datetime.now()} : {message}, \n")
            send.close()

    def create_account(self):
        '''This method will create an account if no account exists'''
        account_email = input("Enter your E-mail Address to create a new account: ")
        account_password = input("Enter your E-Mail Password to create an account: ")
        with open('login_signup.txt', 'a') as create:
            create.write(f'{account_email}\n')
            create.write(f'{account_password}\n')
            create.close()



    def login_account(self):
        account_email = input("Enter your E-Mail Address to login : ")

        if account_email in open('login_signup.txt').read():

            account_password = input("Enter your E-Mail Password to login : ")

            if account_password in open('login_signup.txt').read():

                main_senders()

            else:
                print('Hey thief this is wrong guess')



        else:
            print("E-mail is not found")



    def read_mails(self):
        what_to_read = input("Whose mails do you want to read : ")
        file_path = r'/media/rishaw/Local Disk/R-Mail Project/' + what_to_read + '.txt'
        if os.path.exists(file_path):
            with open(f'{what_to_read}.txt') as readbro:
                print(readbro.read())



    def delete_mail(self):
        game = input("Whose mails should be deleted: ")
        if os.path.exists(f"{game}.txt"):
            os.remove(f"{game}.txt")
        else:
            print("The file does not exist")



    def delete_account(self):
        decision_account = input("Are you sure[Y/N] : ")
        if decision_account == 'y' or 'Y':
            with open('login_signup.txt', 'wt') as delta_account:
                delta_account.write('')
                delta_account.close()

            print("Your account is deleted successfully")

        else:
            print('Your is not deleted')

Account = Email()


def main_senders():
    with open('login_signup.txt') as get_name:
        get = get_name.readline().split('.')
        print(f"Welcome {get[0]}")
        get_name.close()

    dence = False
    while dence is not True:
        print("\nEnter 's' to send the mail, 'r' to read the mails, 'c' to delete the account, 'd' to delete the mail contact, and 'q' to quite")

        select = input("Select : ")
        take = select.lower()
        if take == 's':
            where_to_get = input("Enter the mail : ")
            message = input("Enter your message here : ")
            Account.send_mail(where_to_get, message)



        elif take == 'r':
            Account.read_mails()



        elif take == 'd':
            Account.delete_mail()



        elif take == 'c':
            Account.delete_account()
            time.sleep(0.3)
            thakur = input("Type 'n' for create a new account and 'z' to exit : ")

            if thakur == 'n':
                main()

            elif thakur == 'z':
                sys.exit('You have quit the code')

            else:
                print("Invalid letter")


        elif take == 'q' or 'quite':
            dence = True



        else:
            print('LOL, INVALID')

def main():


    if os.stat("login_signup.txt").st_size == 0:
        Account.create_account()
        time.sleep(0.2)
        main_senders()
    else:
        Account.login_account()
        time.sleep(0.2)

if __name__ == '__main__':
    main()
