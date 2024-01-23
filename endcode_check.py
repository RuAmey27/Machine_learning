import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
    return result['encoding']

file_path = r"Table_4.xls"  # Replace with the path to your file
detected_encoding = detect_encoding(file_path)

print(f"The detected encoding of the file is: {detected_encoding}")
