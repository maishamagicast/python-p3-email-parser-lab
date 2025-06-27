# your code goes here!
import re
class EmailAddressParser:
    def __init__(self,email):
        self.email=email
        
    def parse(self):
        parts=self.email.replace(',',' ').split()
        email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        sorted_emails=sorted(set(filter(email_pattern.fullmatch,parts)))
        return sorted_emails