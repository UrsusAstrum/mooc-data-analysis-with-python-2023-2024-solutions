#!/usr/bin/env python3
import re

def acronyms(s):
    res = []
    s = re.sub(r'[^\w\s]','',s)
    words = s.split()
    for word in words:
        if word == word.upper() and len(word) >= 2 and not word.isnumeric():
            res.append(word)
    
    return res

def main():
    print(acronyms("""For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."""))


if __name__ == "__main__":
    main()
