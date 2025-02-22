import PyPDF2  # Corrected module name
import optparse
from termcolor import colored

def meta_data(filename):
    try:
        with open(filename, 'rb') as file:
            pdf = PyPDF2.PdfReader(file)  # Use PdfReader instead of PdfFileReader
            data = pdf.metadata  # Use .metadata to get document info

            if data:
                for metadata in data:
                    print(colored(f"[+] {metadata}: {data[metadata]}", "green"))
            else:
                print(colored("[-] No metadata found in this PDF.", "red"))

    except FileNotFoundError:
        print(colored("[-] File not found. Check the path and try again.", "red"))
    except Exception as e:
        print(colored(f"[-] An error occurred: {e}", "red"))

def main():
    parser = optparse.OptionParser(colored("[*] Usage: python pdf_metadata.py -f <file.pdf>", "red"))
    parser.add_option("-f", dest="foption", type="string", help="Specify PDF file")
    (options, args) = parser.parse_args()

    if options.foption is None:
        print(parser.usage)
        exit(0)
    else:
        meta_data(options.foption)

if __name__ == "__main__":
    main()
