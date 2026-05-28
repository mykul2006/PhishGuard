import re
import tldextract

def analyze_url(url):

    warnings=[]

    if len(url)>50:
        warnings.append("Long URL")

    if re.search(r'\d+\.\d+\.\d+\.\d+',url):
        warnings.append("IP address used")

    ext=tldextract.extract(url)

    bad_tlds=['xyz','top','tk']

    if ext.suffix in bad_tlds:
        warnings.append("Suspicious TLD")

    return warnings