# PowerPanel API (pwrstat-api)

This is a very simple REST API that wraps the PowerPanel pwrstat application for CyberPower uninterruptible power supplies. Only basic GET support for a single JSON object response for all parameters of the UPS are implemented.

## Important Note!

The latest versions of this container disable the auto turn off features for power failure and low battery that is configured by default for pwrstat. 

# Usage

## Using pre-built Docker Image
- Configuration example: [docker-compose.yaml](prebuilt-docker-compose.yaml)

## Building Manually
  - Clone GitHub repo to local computer.
  - Must have Linux PowerPanel application from CyberPower already downloaded (https://www.cyberpowersystems.com/product/software/powerpanel-for-linux/)
  - Place powerpanel_ver_amd64.deb OR PPL-*-64bit.deb (newer) file downloaded from above address in the folder containing this README, on your local computer.
  - Run Docker build, or use [docker-compose.yaml](build-example-docker-compose.yaml), the included Docker-Compose example. 
  - Access JSON response at http://<docker host IP>:5002/pwrstat
