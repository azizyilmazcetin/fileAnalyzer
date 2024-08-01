import yara

def scan_with_yara(file_path, rule_file):
    try:
        rules = yara.compile(filepath=rule_file)
        matches = rules.match(file_path)
        if matches:
            print(f"Matches found in {file_path}:")
            for match in matches:
                print("Yara Rule:", match.rule)
        else:
            print("No matches found.")
    except yara.YaraSyntaxError:
        print("Error: Yara rule file syntax error.")
    except yara.Error as e:
        print(f"Yara Error: {e}")
    except FileNotFoundError:
        print("Error: File or rule not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python yara_scanner.py [file_path] [rule_file]")
        sys.exit(1)
    file_path = sys.argv[1]
    rule_file = sys.argv[2]
    scan_with_yara(file_path, rule_file)