# bs_balance
A quick script to check your account balance in Berliner Sparkasse using Selenium and Firefox.

## Requirements
* Python 3
* Selenium
* Firefox

## Usage
Specify `LOGIN` and `PIN' values in `# User settings` section of `bs_balance.py`.


## Troubleshooting

### geckodriver
If you are getting geckdriver related errors when starting the script, follow these steps:

1. [Download latest geckdriver for your OS](https://github.com/mozilla/geckodriver/releases) and extract the executable somewhere in your system.

2. Update your system's PATH with geckodriver location.

#### On Linux:
`export PATH=$PATH:/path/to/dir/with/geckodriver/`

#### On Windows:
`setx path "%path%;path\to\dir\with\geckodriver\;"`

**You need to restart your Windows machine after that.**
