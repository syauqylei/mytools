# mytools
A tool to convert nginx error log to JSON and TEXT

### Installation

'''
 git clone https://github.com/syauqylei/mytools.git
 
 cd mytools
 
 pip install .
'''

### Basic Usage

check documentation in terminal
'''
mytools -h
'''

'''
Usage: mytools [OPTIONS] FILENAME

  mytools is a cli tool to convert nginx's error log to JSON and TXT file.

  Basic Usage :

      $ mytools /var/log/nginx/error.log -t json

      or

      $ mytools /var/log/nginx/error.log -t text

      or

      $ mytools /var/log/nginx/error.log -t json -o
      /var/log/nginx/error.json

      This command will generate text file as a default if -t or --type is
      not provided.

Options:
  -t, --type TEXT    output file's type
  -o, --output TEXT  output's path
  -h, --help         Show this message and exit.

'''
