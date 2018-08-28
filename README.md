# PowerPanel (pwrstat) API 

This is a very simple REST API that wraps the PowerPanel pwrstat application for CyberPower battery backups. Only basic GET support for a single JSON object response for all parameters of the UPS are implemented.

# Usage

  - Clone GitHub repo to local computer.
  - Must have Linux PowerPanel application from CyberPower already downloaded (https://www.cyberpowersystems.com/product/software/powerpanel-for-linux/)
  - Place powerpanel_ver_amd64.deb file downloaded from above address in the folder containing this README, on your local computer.
  - Run Docker build, or use included Docker-Compose example. 
  - Note that you cannot use this GitHub repo as a Docker-Compose build context, due to needing to download a local copy of the CyberPower binary.
  - Access JSON response at http://<docker host IP>:5002/pwrstat

