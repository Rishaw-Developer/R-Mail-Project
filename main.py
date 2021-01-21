import datetime
import os
import sys
import time

print("Hy user , Welcome to the R-Maill where you send your mails to anyones you want")


class Email:
        
    def send_mail(self, send_to_where, message):
        '''This method will send the message'''

        with open(f'{send_to_where}.txt', "a") as sending_message:
            sending_message.write(f"At {datetime.datetime.now()} : {message}, \n")
            sending_message.close()

    def create_account(self):
        '''This method will create an account if no account exists'''

        account_email = input("Enter your E-mail Address to create a new account: ")
        account_password = input("Enter your E-Mail Password to create an account: ")
        with open('login_signup.txt', 'a') as creating_account:
            creating_account.write(f'{account_email}\n')
            creating_account.write(f'{account_password}\n')
            creating_account.close()



    def login_account(self):
        '''This method will be used to login'''

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
        '''This method will be used to read the mails'''

        whose_mail = input("Whose mails do you want to read : ")
        file_path = r'/media/rishaw/Local Disk/R-Mail Project/' + whose_mail + '.txt'
        if os.path.exists(file_path):
            with open(f'{whose_mail}.txt') as reading_mail:
                print(reading_mail.read())



    def delete_mail(self):
        '''This method will be used to delete the all the mails of a specific email'''

        removing_mail = input("Whose mails should be deleted: ")
        if os.path.exists(f"{removing_mail}.txt"):
            os.remove(f"{removing_mail}.txt")
        else:
            print("The file does not exist")



    def delete_account(self):
        '''This method will delete the account and password of the user'''

        deleting_decision = input("Are you sure[Y/N] : ")
        if deleting_decision == 'y' or 'Y':
            with open('login_signup.txt', 'wt') as removing_account:
                removing_account.write('')
                removing_account.close()

            print("Your account is deleted successfully")

        else:
            print('Your is not deleted')

Account = Email()


def main_senders():
    '''This function controls the all sending, reading, and deleting of a account or mail'''
    with open('login_signup.txt') as user_name:
        get_name = user_name.readline().split('.')
        print(f"Welcome {get_name[0]}")
        user_name.close()

    ender = False
    while ender is not True:
        print("\nEnter 's' to send the mail, 'r' to read the mails, 'c' to delete the account, 'd' to delete the mail contact, and 'q' to quite")

        select = input("Select : ")
        take = select.lower()
        if take == 's':
            where_to_send = input("Enter the mail : ")
            message = input("Enter your message here : ")
            Account.send_mail(where_to_send, message)



        elif take == 'r':
            Account.read_mails()



        elif take == 'd':
            Account.delete_mail()



        elif take == 'c':
            Account.delete_account()
            time.sleep(0.3)
            last_decision = input("Type 'n' for create a new account and 'z' to exit : ")

            if last_decision == 'n':
                main()

            elif last_decision == 'z':
                sys.exit('You have quit the code')

            else:
                print("Invalid letter")


        elif take == 'q' or 'quite':
            ender = True



        else:
            print('LOL, INVALID')

def main():
    '''All the things of this program is starts from here'''


    if os.stat("login_signup.txt").st_size == 0:
        Account.create_account()
        time.sleep(0.2)
        main_senders()
    else:
        Account.login_account()
        time.sleep(0.2)

if __name__ == '__main__':
    main()
