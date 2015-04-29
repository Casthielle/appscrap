# SCRAPY
App python to extract account balance and transactions from banks. It's a fork of Ruby gem bank_scrap made by diacode.


## Supported banks


| Operations      |  BBVA  |  Mercantil  |
|-----------------|:------:|:-----------:|
| Account Balance |    ✓   |      ✓      |
|  Transactions   |    ✓   |      ✓      |

Interested in any other bank? Open a new Issue and we'll try to help.


## Background and motivation

Most banks do not offer public APIs and the only way to access your data (balance and transactions) is through their websites ... and most of the websites of banks are a nightmare.

We are developers and we do not want to waste time doing things that are able to automate. Having to make 20 clicks in a horrible site just to check the amount of money we have is not something we like.


## Installation

### From Git

You can check out the latest source from git:

    git clone https://github.com/Casthielle/SCRAPY.git


## Requirements

To perform operations on the BBVA bank, you need to add the details of your code card on file ' /src/scrapy.py ' in codecard variable. For example:

And get its balance:
```python
codecard = {
			"A1":"106", "A2":"745", "A3":"078", "A4":"584", "A5":"396", "A6":"818", "A7":"537", "A8":"577", "A9":"184", "A10":"380",
			"B1":"555", "B2":"103", "B3":"740", "B4":"924", "B5":"131", "B6":"482", "B7":"028", "B8":"116", "B9":"040", "B10":"282",
			"C1":"434", "C2":"608", "C3":"027", "C4":"452", "C5":"194", "C6":"085", "C7":"633", "C8":"058", "C9":"427", "C10":"897",
			"D1":"126", "D2":"477", "D3":"292", "D4":"583", "D5":"052", "D6":"275", "D7":"951", "D8":"162", "D9":"162", "D10":"709",
			"E1":"917", "E2":"549", "E3":"889", "E4":"154", "E5":"316", "E6":"903", "E7":"874", "E8":"892", "E9":"136", "E10":"587",
			"F1":"997", "F2":"146", "F3":"524", "F4":"056", "F5":"402", "F6":"290", "F7":"848", "F8":"690", "F9":"133", "F10":"522",
			"G1":"149", "G2":"089", "G3":"109", "G4":"390", "G5":"546", "G6":"016", "G7":"669", "G8":"509", "G9":"812", "G10":"419",
			"H1":"974", "H2":"639", "H3":"670", "H4":"119", "H5":"646", "H6":"272", "H7":"565", "H8":"489", "H9":"207", "H10":"049"
		}
```

## Usage

### From terminal
#### Bank account balance

###### BBVA | Mercantil

    $ python scrapy.py YOUR_BANK balance --user YOUR_BANK_USER --password YOUR_BANK_PASSWORD

or

	$ python scrapy.py YOUR_BANK balance -u YOUR_BANK_USER -p YOUR_BANK_PASSWORD

#### Last Transactions
###### BBVA | Mercantil

    $ python scrapy.py YOUR_BANK transactions --user YOUR_BANK_USER --password YOUR_BANK_PASSWORD

or

	$ python scrapy.py YOUR_BANK transactions -u YOUR_BANK_USER -p YOUR_BANK_PASSWORD


If you don't want to pass your user and password everytime you can define them in your .bash_profile by adding:

    export SUSER=YOUR_BANK_USER
    export SPASSWORD=YOUR_BANK_PASSWORD


## Contributing

1. Fork it ( https://github.com/SCRAPY/SCRAPY/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

## Thanks

Thanks to Javier Cuevas (@javiercr) and Diacode for his bank_scrap gem.
And Thanks also to madrid.rb and codersvenezuela.com