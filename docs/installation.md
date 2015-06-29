# Installing Dusty

## Requirements
You must have the following installed in order to run Dusty:

 * nginx
 * Virtualbox
 * boot2docker
 * Docker Compose

Not all versions of these programs will work with Dusty.  Dusty
will warn you if you have a version installed that may be too old.
We recommend brew-installing the latest versions of each of these
programs:
```
which nginx || brew install nginx
which boot2docker || brew install boot2docker
which docker-compose || brew install docker-compose
```

## Installation

To download and install Dusty, run:
```
bash -c "`curl -L https://github.com/gamechanger/dusty/releases/download/0.1.3/install.sh`"
```

This script will install Dusty as a service and run the preflight check to ensure that all
dependencies are installed. If the script throws an error, make sure to resolve that before
continuing.

If that worked, [continue to Setup.](setup.md)