import os

target_file = '1.student.mark.py'
symlink_name = 'copy_of_lab1.py'

os.symlink(target_file, symlink_name)

if os.path.isLink(symlink_name):
    print(f"Symbolic link '{symlink_name}' created successfully")
else:
    print("Failed to create symbolic link")