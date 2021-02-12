import re
import shutil

def read_file(filepath):
    """read file and return content
    """
    with open(filepath, 'r') as potential:
        contents = potential.read()
        return contents

def parse_numbers(filepath):
    """Parse the phone numbers from the text file and return it formatted in xxx-yyy-zzzz. If no area code found, give it an area code of (206). 

    Args:
        filepath (path): filepath

    Returns:
        list: list of phone numbers after being filtered of dupes, reformatted, and sorted
    """
    contents = read_file(filepath)
    numbers = re.findall(r"\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}", contents)

    for index, num in enumerate(numbers):
        if len(num) < 10:
            numbers[index] = '206' + num

    stripped_numbers = re.sub(r"[\s\[\]\(\)\.\-\']", "", str(numbers))
    formatted_numbers = re.sub(r"(\d{3})(\d{3})(\d{4})", r"\1-\2-\3", str(stripped_numbers))

    phones = list(map(str, formatted_numbers.split(',')))
    filtered_list = set(phones)
    sorted_list = sorted(filtered_list)
    return sorted_list

def parse_emails(filepath):
    """Parse email addresses from file. 

    Args:
        filepath (path): filepath

    Returns:
        list: list of email addresses from the file
    """
    contents = read_file(filepath)
    pattern = r"[\w\.-]+@[\w\.-]+"
    emails = re.findall(pattern, contents)
    filtered_list = list(set(emails))
    sorted_list = sorted(filtered_list)
    return sorted_list

def save():
    """Save the parsed emails and phone numbers to a new file in the assets folder.
    """
    with open('../assets/emails.txt', 'w+') as f:
        emails = parse_emails(filepath)
        f.write(str(emails))

    with open('../assets/phone_numbers.txt', 'w+') as f:   
        numbers = parse_numbers(filepath)
        f.write(str(numbers))

    try:
        shutil.copy('../assets/potential-contacts.txt', '../assets')
    except shutil.SameFileError:
        pass

if __name__ == "__main__":
    # filepath = '../assets/potential-contacts.txt'
    # print(parse_numbers(filepath))
    # print(len(parse_numbers(filepath)))
    # print(parse_emails(filepath))
    # print(len(parse_emails(filepath)))
    # save()
    pass

"""
Resource Credits:
email regex: https://stackoverflow.com/questions/17681670/extract-email-sub-strings-from-large-document
phone regex: https://stackoverflow.com/questions/16699007/regular-expression-to-match-standard-10-digit-phone-number
remove dupes from list: https://stackoverflow.com/questions/8200342/removing-duplicate-strings-from-a-list-in-python
same file error: https://stackoverflow.com/questions/57083594/disable-samefileerror-exception-in-shutil-copy
"""