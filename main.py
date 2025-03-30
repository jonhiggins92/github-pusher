from datetime import datetime
import os

def modify_and_commit():
    # File to modify
    file_path = 'daily_log.txt'
    
    # Append current date and time to the file
    with open(file_path, 'a') as file:
        file.write(f"Update as of {datetime.now()}\n")
    
    # Git commands to add, commit, and push
    os.system('git add daily_log.txt')
    os.system('git commit -m "Daily auto-commit"')
    os.system('git push origin main')

if __name__ == "__main__":
    modify_and_commit()
