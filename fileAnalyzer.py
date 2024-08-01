import pefile

def analyze_pe(file_path):
    try:
        pe = pefile.PE(file_path)
        print("File Name:", file_path)
        print("File Type:", pe.FILE_HEADER.Machine)
        print("Entry Point:", hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint))
        # Ekstra bilgi ekleyin: section headers, imports, exports, dlls, vb.
        for section in pe.sections:
            print(f"Section: {section.Name.decode().strip()}")
    except FileNotFoundError:
        print("Error: File not found.")
    except pefile.PEFormatError:
        print("Error: File is not a valid PE file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python file_analyzer.py [file_path]")
        sys.exit(1)
    file_path = sys.argv[1]
    analyze_pe(file_path)