# Audible AAX downloader

This tool can help you download all your AAX files from Audible.

**Hint**: this tool only does the download part.
If you wish to convert your AAX files to MP3s, you also
need the following tools:
1) [audible-activator](https://github.com/inAudible-NG/audible-activator):
	this tool helps you to retrieve your activation bytes which you need
	to decode the AAX files to any other audio format
2) [AAXtoMP3](https://github.com/KrumpetPirate/AAXtoMP3):
	the tool that uses your downloaded AAX files and the activation
	bytes retrieved with audible-activator to decode your files
	to the most common audio formats

**Another hint**: This tool is specific to the German version of audible.
You should be able to adapt the script to any other language by replacing
the strings in the `list.py` script that the tool uses to identify
elements of the user interface. Pull Requests welcome!

## Installation

These scripts require pyhton3. 

Clone the repository. This tool requires the following python libraries:
* requests
* selenium + Firefox Webdriver
* progress

First, run `selenium_install.sh` to install the web driver.
Then run
```
pip install requests selenium progress
```
to install the required python packages.


## Usage

First, run `python list.py` to retrieve a list of your audiobooks
and the cookies required to authenticate yourself to audible.
The script will ask you for your audible email and password.
This may take a couple of minutes.

Then, run `python download.py`. The script will present you with a
list of your audiobooks and ask you which to download.
Select the numbers (separated by space) and hit enter.
You will see a progress bar for each file being downloaded.

After the script has finished, your current working directory
will contain the downloaded AAX files. See above for how 
to convert these to mp3 files.
