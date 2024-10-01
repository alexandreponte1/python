import os
import shutil
import datetime

source_directory = "./source"
backup_directory = "./backup"

def backup_directory_contents(source, backup):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_path = os.path.join(backup, f"backup_{timestamp}")
    try:
        shutil.copytree(source, backup_path)
        print(f"Backup completed: {backup_path}")
    except Exception as e:
        print(f"Backup failed: {e}")

def recover_backup(backup_path, destination):
    try:
        shutil.rmtree(destination)
        shutil.copytree(backup_path, destination)
        print(f"Recovery completed: {destination}")
    except Exception as e:
        print(f"Recovery failed: {e}")

if __name__ == "__main__":
    print("Choose an option: ")
    print("1. Backup")
    print("2. Recover")

    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        backup_directory_contents(source_directory, backup_directory)
    elif choice == "2":
        backup_list = os.listdir(backup_directory)
        print("Available backups: ")
        for idx, backup in enumerate(backup_list, start=1):
            print(f"{idx}. {backup}")
        backup_index = int(input("enter the backup index to recover: ")) - 1

        if 0 <= backup_index < len(backup_list):
            selected_backup = os.path.join(backup_directory, backup_list[backup_index])
            recover_backup(selected_backup, source_directory)
        else:
            print("Invalid backup index")
    else:
        print("Invalid choice, it's either 1 or 2")