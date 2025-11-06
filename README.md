[Goto the WIKI](https://github.com/tvgrabbers/tvgrabpyAPI/wiki)
 
# epgNL

epgNL is an API for creating xmltv compatible tv grabbers. It is the succesor of [tv_grab_py_API version 2.2](https://github.com/tvgrabbers/tvgrabnlpy)

## W.I.P (Work in progress)

This repository contains software that is in active development and is likely to change in the near future.

## Requirements

- Linux (Windows and Mac are untested at this time)
- Python 3.4 or higher

## Installation

- Download the latest release and unpack it into a directory
- Create a new virtual environment, called `venv`: `python -m venv venv`
- Activate virtual environment: `source venv/bin/activate`
* Install dependencies: `pip install -r requirements.txt`
- Run `python tv_grab_nl3.py --configure` to initialize the program. 
- Check the created configuration file ./epgNL/data/tv_grab_nl3.conf and activate the desired channels.
- Run `python tv_grab_nl3.py` with `--help` flag to see all options.

## Some features

- No need for anybody who wants to create a grabber to know much about Python. You mainly must write one or more json data_defs defining one or more sources. These are [DataTreeGrab data_defs](https://github.com/tvgrabbers/DataTree/wiki/data_def_language) with some specific extensions.
- All retrieved data is stored in an sqlite database which:
  - speeds up data retrieval
  - makes it possible to repeatetly access the data again while off-line  
 
- Extensive list of user-settable options to give a user maximum oportunity to adapt the program to his or her need.
- User setable genre translation tables with developer settable defaults.
- Multiple language support (currently English and Dutch).
- data_def updates are automatic.
- theTVDB.com lookup.
