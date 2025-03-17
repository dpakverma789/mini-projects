
import os
os.chdir('F:\python_programs\Website Blocker')
try:
    import platform
    import hashlib
    import pytz
    from datetime import datetime
except ModuleNotFoundError:
    # with open(os.path.join(os.getcwd(), 'requirements.txt')) as file:
    #     package = [pack.strip('\n') for pack in file.readlines()]
    #     for pack in package:
    #         os.system(f'pip install {pack}')
    import platform
    import hashlib
    import pytz
    from datetime import datetime

# ============= Display Info ==========
print('\n\t\t{:-^40}'.format(' Website Blocker '))
print('\t\t{}'.format('Version - 1.3.1'))
print('\t\t{}'.format('A Project from Mini-Py Project'))
info = """
Instructions: 
1) For Adding new website directly write website name like "instagram.com".
2) For Deleting website write del or delete press enter, then website name like "instagram.com".
3) For Checking List of blocked website write check.
4) For exporting file write export.
5) For importing file write import press enter, then complete path of text file \
like "C:\\Users\\DEEPAK-PC\\Downloads\\block_website_file.txt" \n having list of website which should be blocked.
"""
print(info)
# ======================================

# flag for operating system
is_windows_os = True if platform.system() == 'Windows' else False

# selecting path according to OS
if is_windows_os:
    hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
    export_path = 'C:\\Users\\%s\\Downloads' % os.getlogin()
else:
    hosts_path = "/etc/hosts"
    export_path = '/home/%s/Downloads/' % os.getlogin()

# localhost IP
redirect = "127.0.0.1"


# write website to host file
def write(hosts_path, website_list, flag, redirect, is_windows_os) -> None:
    count = 0
    if is_windows_os:
        os.system('attrib -s -r -h %s' % hosts_path)
    for website in website_list:
        with open(hosts_path, 'r+', encoding='UTF-8') as host:
            count += 1
            file_data = host.readlines()
            file_data.sort()
            container = (line.strip('\n').strip(redirect).strip() for line in file_data if redirect in line)
            if website in container:
                if count == 1:
                    print('\n\tWebsite Already exist')
            else:
                if flag in ('yes', 'y'):
                    host.write(redirect + " " + website + "\n")
                    if count == 1:
                        print('\n\tWebsite Updated in the Block List!')
    if is_windows_os:
        os.system('attrib +s +r +h %s' % hosts_path)
    del container, website_list


# delete website from the host file
def delete(args) -> None:
    string = input('\n\nEnter the Website which Should be Un-Blocked: ')
    if is_windows_os:
        os.system('attrib -s -r -h %s' % hosts_path)
    try:
        with open(hosts_path, 'r+', encoding='UTF-8') as fp:
            file_data = fp.readlines()
            file_data.sort()
            content = (line for line in file_data if string not in line)
        with open(hosts_path, 'w+', encoding='UTF-8') as fpp:
            for i in content:
                if i == '#':
                    fpp.write('\n')
                fpp.write(i)
        if is_windows_os:
            os.system('attrib +s +r +h %s' % hosts_path)
        print('\n "%s" has been Un-Blocked' % string)
        del content
    except PermissionError as error:
        print(error)


# count the number of blocked website
def check_file(args) -> None:
    try:
        if is_windows_os:
            os.system('attrib -s -r -h %s' % hosts_path)
        with open(hosts_path, 'r+', encoding='UTF-8') as file:
            website_count = 0
            file_data = file.readlines()
            file_data.sort()
            for line in file_data:
                if redirect in line and 'www.' not in line:
                    website_count += 1
                    print(line, sep="", end="")
            print('\nTotal website: ', int(website_count))
        if is_windows_os:
            os.system('attrib +s +r +h %s' % hosts_path)
    except PermissionError as error:
        print(error)


# import the website list to host file
def import_host(hosts_path, redirect, is_windows_os) -> None:
    file_to_be_imported = input('Enter File path to be imported!: ')
    try:
        with open(file_to_be_imported, 'r+', encoding='UTF-8') as user_file:
            website_list = (line.strip('\n').strip(redirect).strip() for line in user_file.readlines() if redirect in line)
            flag = 'yes'
            write(hosts_path, website_list, flag, redirect, is_windows_os)
        print(f"Importing has been Successfully Completed, from \"{file_to_be_imported }\"")
        del website_list
    except PermissionError as error:
        print(error)


# export host file website list to txt file
def export_host(export_path) -> None:
    time_zone = pytz.timezone('Asia/Kolkata')
    today = datetime.now(time_zone)
    time_stamp = today.strftime("%d-%B-%Y--%H-%M")
    file_name = '-'.join((time_stamp, 'hosts.txt'))
    try:
        if is_windows_os:
            os.system('attrib -s -r -h %s' % hosts_path)
        with open(hosts_path, 'r+', encoding='UTF-8') as file:
            file_data = file.readlines()
            file_data.sort()
            container = (line.strip('\n').strip() for line in file_data if redirect in line
                         and 'www.' not in line)
        export_file_path = os.path.join(export_path, file_name)
        with open(export_file_path, 'w+', encoding='UTF-8') as export:
            for line in container:
                export.write(line)
                export.write('\n')
        print(f"Export Successfully Completed, Please find your file here \"{export_file_path}\"")
        if is_windows_os:
            os.system('attrib +s +r +h %s' % hosts_path)
        del container
    except PermissionError as error:
        print(error)


# websites That you want to block
operation = {'check': check_file, 'del': delete, 'export': export_host, 'import': import_host}
while True:
    website_list = []
    args = None
    WebSite = input('\n\nEnter the Website which Should be Blocked: ')
    if 'www' in WebSite:
        www_WebSite = WebSite[4:]
    elif WebSite in operation.keys():
        if WebSite == 'export':
            args = export_path
        if WebSite == 'import':
            args = (hosts_path, redirect, is_windows_os)
        operation[WebSite](args)
        continue
    else:
        www_WebSite = 'www.' + WebSite
    flag = input('\nAre You sure, to update "%s" on Block-list(Yes/Y): ' % WebSite if WebSite else '-').lower()
    website_list.extend((WebSite, www_WebSite))
    if is_windows_os:
        os.system('attrib -s -r -h %s' % hosts_path)
    try:
        write(hosts_path, website_list, flag, redirect, is_windows_os)
        del website_list
    except PermissionError as error:
        print(error)
