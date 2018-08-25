# docx-diary
This script allows the user to create, view and open docx files with a specific format (*see **Document formatting***).

## Getting Started

Once downloaded, run main.py using the command-line to start the script.

### Prerequisites

To use this script you will need the following:

```
Python 3.5+
python-docx 0.8.6+
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

## Built With

* [Python 3.5](https://docs.python.org/3.5/) - The programming language used.
* [python-docx 0.8.6](https://pypi.python.org/pypi/python-docx/0.8.6) - The library used by the script to create and edit data.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on this project's code of conduct, and the process for submitting pull requests.

## Author

**Joshua Booth** - [Joshua-Booth](https://github.com/Joshua-Booth)


## License

This project is licensed under the GPL-3.0 License - see the [LICENSE.md](LICENSE.md) file for details
