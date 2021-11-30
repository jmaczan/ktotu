from os import system, path
from sys import exit
from constants import mac_addresses_scanner, ktotu, ktotu_path, ktotu_symlink_path,  rootPath, user_files_directory_path
def install():
    userPath = path.expanduser('~')
    disallow_root(userPath)
    
    create_user_files_directory(userPath)

    create_executables_directory()

    copy_executables_to_directory()
    
    create_ktotu_symlink()

    print('Installation completed')

def disallow_root(userPath):
    if(userPath == rootPath):
        print('Please run install script as not root.')
        exit()

def create_ktotu_symlink():
    if(not path.isfile(ktotu_symlink_path)):
        system('sudo ln -s '+ktotu_path+'/'+ktotu+' '+ktotu_symlink_path)

def copy_executables_to_directory():
    system('sudo cp '+ktotu+' '+ktotu_path)
    system('sudo cp '+mac_addresses_scanner+' '+ktotu_path)

def create_executables_directory():
    if(not path.isdir(ktotu_path)):
        system('sudo mkdir '+ktotu_path)
        return None
    
    remove_existing_executables()

def remove_existing_executables():
    ktotu_file_path = ktotu_path+'/'+ktotu+''
    mac_addresses_scanner_file_path = ktotu_path+'/'+mac_addresses_scanner+''

    if(path.isfile(ktotu_file_path)):
        system('sudo rm '+ktotu_file_path)

    if(path.isfile(mac_addresses_scanner_file_path)):
        system('sudo rm '+mac_addresses_scanner_file_path)

def create_user_files_directory(userPath):
    ktotu_user_files_path = userPath+'/'+user_files_directory_path
    if(not path.isdir(ktotu_user_files_path)):
        system('mkdir '+ktotu_user_files_path)

install()