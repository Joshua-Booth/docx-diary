# docx-diary
This script allows the user to create, view and open docx files with a specific format (*see **Document formatting***).

## Getting Started

Once downloaded, run main.py using the command-line to start the script.

### Prerequisites

To use this script you will need the following:

```
Python 3.5+
python-docx 0.8.6+
setuptools-40.2.0+
```

### Installing


##### Install

```
C:\docx-diary> python -m setup.py install
```

### Usage

##### Running the program

To run the program, run the following command where "your_text_file.txt" is a file in the directory from where the command is called, any encrypted/decrypted files will also be placed here.

**Example:**
*New Entry*
```
C:\>python -m docx-diary.__main__ -n
```


**Other commands can be found with:** *Help*
```
C:\>python -m docx-diary.__main__ -h
```


### Document formatting
**Data filenames are in the following format:**

{Day} {Month} {Day Number} {Year}

*Example:* 
```
Monday January 1 2018
```

**File data is in the following format:**

```
{Day}, {Month} {Day Number}, {Year} {Time} {Period}
{Message}
```

*Example:*
```
Monday, January 1, 2018 7:30 PM
Today is the first day of January!
```

## Distribution

To distribute this package, locate the directory containing [setup.py](setup.py) and run the following command:

````
C:\>python setup.py sdist
````

Note: Use the format flag ( --format) to select a different file format.

## Built With

* [Python 3.5](https://docs.python.org/3.5/) - The programming language used.
* [python-docx 0.8.6](https://pypi.python.org/pypi/python-docx/0.8.6) - The library used by the script to create and edit data.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on this project's code of conduct, and the process for submitting pull requests.

## Author

**Joshua Booth** - [Joshua-Booth](https://github.com/Joshua-Booth)


## License

This project is licensed under the GPL-3.0 License - see the [LICENSE.md](LICENSE.md) file for details
