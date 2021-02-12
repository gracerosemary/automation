from automation import __version__
from automation.automation import parse_numbers, parse_emails, read_file
import re

def test_version():
    assert __version__ == '0.1.0'

def test_phone():
    filepath = 'assets/potential-contacts.txt'
    numbers = parse_numbers(filepath)
    actual = numbers[0]
    expected = '008-445-7591'
    assert actual == expected 

def test_email():
    filepath = 'assets/potential-contacts.txt'
    emails = parse_emails(filepath)
    actual = emails[0]
    expected = 'aaron84@gmail.com'
    assert actual == expected 

def test_phone_format():
    filepath = 'assets/potential-contacts.txt'
    numbers = parse_numbers(filepath)
    reg_num = bool(re.search(r"(\d{3})-(\d{3})-(\d{4})", str(numbers)))
    actual = reg_num
    expected = True
    assert actual == expected 

def test_email_format():
    filepath = 'assets/potential-contacts.txt'
    emails = parse_emails(filepath)
    reg_emails = bool(re.search(r"[\w\.-]+@[\w\.-]+", str(emails)))
    actual = reg_emails
    expected = True
    assert actual == expected 