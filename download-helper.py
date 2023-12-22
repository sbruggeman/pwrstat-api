from urllib.request import urlopen
import os
import re

print("Getting download options for PowerPanel:")
link="https://www.cyberpowersystems.com/product/software/powerpanel-for-linux/"

response=urlopen(link)
downloaded_source=str(response.read())

# defaults
distro="rpm"
architecture="64" 

# read from env 
if os.environ['DISTRO'] != distro:
    distro=os.environ['DISTRO']
if os.environ['ARCHITECTURE'] != architecture:
    architecture=os.environ['ARCHITECTURE']

print("Environment Variables:")
print("DISTRO=" + distro)
print("ARCHITECTURE=" + architecture)

# reroute download for generic linux
if distro == "linux":
    architecture=""
    distro="tar.gz"

pattern=re.compile(r'PPL_' + architecture + 'bit_v\d+\.\d+\.\d+\.' + distro)
found_matches=[]
matches=pattern.findall(downloaded_source)
for match in matches:
    if match in found_matches:
        continue
    found_matches.append(match)

if len(found_matches) == 1:
    pattern_search_url = '"https://.*?cloudfront.net\/software\/' + found_matches[0] + '"'
    pattern_search_url=re.compile(r'' + pattern_search_url)
    matches_url=pattern_search_url.findall(downloaded_source)
    found_url_matches=[]
    for match_url in matches_url:
        if ' ' in match_url:
            continue
        if match_url in found_url_matches:
            continue
        found_url_matches.append(match_url)
else:
    print("ERROR: No downloads for this Distro & Architecture found! [ERROR# 1000]")

if len(found_url_matches) == 1:
    final_url=found_url_matches[0].replace('"','')
    import urllib.request
    urllib.request.urlretrieve(final_url, found_matches[0])
else:
    print("ERROR: No downloads for this Distro & Architecture found! [ERROR# 1001]")