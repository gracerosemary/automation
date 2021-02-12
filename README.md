# Automation

**Author**: Grace Choi
**Version**: 1.0.0

PR Link: 

## Overview
Given a document potential-contacts, find and collect all email addresses and phone numbers.  

## Getting Started  
project: `poetry new automation`  
assets folder: `potential-contacts.txt`

## Architecture
- Regex  
- Poetry   
- Shutil  
- Pytest  

## API
`read-file`: Read file and return content.  
`parse-numbers`: Parse the phone numbers from the text file and return it formatted in xxx-yyy-zzzz. Filter the phone for dupes and sort it in ascending order. If no area code found, give it an area code of (206).  
`parse-emails`: Parse email addresses from file and return in ascending order.  
`save`: Save the parsed emails and phone numbers to a new file in the assets folder.  

## Tests
1. test phone output  
2. test email output  
3. test phone regex pattern  
4. test email regex pattern  

## Change Log
02-10-2021 9:30pm - Finished Code  
02-11-2021 10:35pm - Finished Tests  
