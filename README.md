# Tax Helper
Automate entering cryptocurrency transactions into TurboTax 2017 with Selenium

## Installation

Install [geckodriver](https://github.com/mozilla/geckodriver/) for Firefox automation

### on OSX
```bash
brew install geckodriver
```

### on Linux

[Download and install a release from the geckodriver repo](https://github.com/mozilla/geckodriver/releases)

Then install the python requirements:
```bash
pip install -r requirements.txt
```

## Usage

```bash
$ python -m taxhelper --h
usage: __main__.py [-h] --trades TRADES --credentials CREDENTIALS
                   [--start-index START_INDEX]

TurboTax Helper

optional arguments:
  -h, --help            show this help message and exit
  --trades TRADES       path to CSV file of trades
  --credentials CREDENTIALS
                        path to JSON credentials file
  --start-index START_INDEX
                        Begin at the index of trade in trades CSV. Useful for
                        when bot gets stuck and want to resume without
                        starting over
```

## Adding your credentials and trades

The automated browser will attempt to login to the TurboTax Web UI, so it'll need your username and password. It expects them
in the form of a JSON file like the provided `credentials.json`.

It expects the trades in the form of a CSV like the example provided in `dummy.csv` and `dummy.xlsx`. Your CSV should include only
trades you need to report. The required columns are the ones that ultimately go into TurboTax:
```
[
  "net_proceeds",
  "sell_datetime",
  "cost_basis",
  "purchase_datetime"
]
```

Check out `dummy.xlsx` to see how those some of those fields are calculated. I started by exporting by GDAX fills history and then manipulating
the CSV into this format
