import os, platform, time, sys
print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mChecking For Update...')
os.system('git pull --quiet 2>/dev/null')
mrsaiim = platform.architecture()[0]
if mrsaiim == '64bit':
 print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mYour Device is 64bit');time.sleep(2)
 os.system('chmod 777 OFFLINE64 && ./OFFLINE64')
elif mrsaiim== '32bit':
 print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mYour Devive is 32bit');time.sleep(2)
 os.system('chmod 777 OFFLINE32 && ./OFFLINE32') 
try:
    import FBTools
except:
    os.system("pip install fbtoolsbox --quiet 2>/dev/null")
    from FBTools import Start
from FBTools import Start
import os
import time, random
from datetime import datetime

# ANSI escape codes for colors
class Colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"

logo = f'''{Colors.YELLOW}

███████╗ █████╗ ██╗██╗███╗   ███╗    ██████╗  █████╗      ██╗ █████╗ 
██╔════╝██╔══██╗██║██║████╗ ████║    ██╔══██╗██╔══██╗     ██║██╔══██╗
███████╗███████║██║██║██╔████╔██║    ██████╔╝███████║     ██║███████║
╚════██║██╔══██║██║██║██║╚██╔╝██║    ██╔══██╗██╔══██║██   ██║██╔══██║
███████║██║  ██║██║██║██║ ╚═╝ ██║    ██║  ██║██║  ██║╚█████╔╝██║  ██║
╚══════╝╚═╝  ╚═╝╚═╝╚═╝╚═╝     ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝                                                                                                                                                                                                                                                                                                                                                                    
{Colors.RESET}'''

def logx():
    print(logo)
    print(40 * '=')
    print(f"\t{Colors.BLUE}Author : S911M R9J9 P0ST L0AD3R{Colors.RESET}")
    print(40 * '=')

def login_with_cookies(cookie_file_path):
    try:
        with open(cookie_file_path, 'r') as file:
            cookies = file.readlines()
    except FileNotFoundError:
        exit(f'{Colors.RED}File not found at path: {cookie_file_path}{Colors.RESET}')

    return [Start(cookie=cookie.strip()) for cookie in cookies]

def bot_comment(fb_instances, comment_file_path, post_id, delay_time):
    while True:
        for FB in fb_instances:
            with open(comment_file_path, 'r') as file:
                lines = file.readlines()
                if lines:
                    random_line = random.choice(lines)
                    comment_text = random_line.strip()

                    Comment = FB.SpamCommentToPost(post=post_id, text=comment_text)
                    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    if 'status' in Comment and Comment['status'] == 'success':
                        print(f'{Colors.GREEN}Comment "{comment_text}" Sent at {current_time}{Colors.RESET}')
                        print(40 * '=')
                    else:
                        print(f'{Colors.RED}Comment "{comment_text}" Not Sent at {current_time}{Colors.RESET}')
                        print(40 * '=')
                    time.sleep(delay_time)
                else:
                    pass

def main():
    logx()
    cookie_file_path = input('Enter the path to your cookies text file: ')
    comment_file_path = input('Enter the path to your comments text file: ')
    post_id = input('Input ID Post: ')
    delay_time = int(input('Input delay time in seconds: '))

    fb_instances = login_with_cookies(cookie_file_path)
    bot_comment(fb_instances, comment_file_path, post_id, delay_time)
    
main()