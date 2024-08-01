import os

def check_file_permissions(file_path):
    try:
        file_info = os.stat(file_path)
        permissions = oct(file_info.st_mode & 0o777)  # Sadece izinler
        print(f"File: {file_path}")
        print(f"Permissions: {permissions}")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python activity_monitor.py [file_path]")
        sys.exit(1)
    file_path = sys.argv[1]
    check_file_permissions(file_path)