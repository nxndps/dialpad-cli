# dialpad-cli
Dialpad CLI Utilities

## Install

1. `pip3 install -r requirements.txt`

2. You will need an API key to user the CLI Utilities. You have two methods to
supply this key. 
- Create or update `.dp.env` in the local directory add the line `dptoken=XXXXXXXXX` .
- Create the ENV variable `dptoken` with the API key value.

3. Enjoy!

## Usage
Most of the utilites have a `-h` help command line option with the available arguments.
Some of the utilites have no available options.

The output of the utilites will be sent to stdout for data and stderr for
log messages. With this in mind, in most cases where the is not an explicit
export file, you may use a pipe or redirect to capture the data.

eg:
```shell
% src/office_license.py > output.log
{
 "additional_number_lines": "0", 
 "contact_center_lines": "6", 
 "fax_lines": "1", 
 "room_lines": "2", 
 "sell_lines": "4", 
 "talk_lines": "10", 
 "tollfree_additional_number_lines": "0", 
 "tollfree_room_lines": "0", 
 "uberconference_lines": "0"
}
```
you could also capture both 
`src/office_license.py >> output.log 2>&1` 
or send to `tee`
`src/office_license.py  2>&1 | tee output.log`

The output by default JSON so having jq available is recommended.
eg: To retrieve the number of remaining Contact Center Licenses 
`src/office_license.py | jq -r '.contact_center_lines'`

## Copyright
Copyright 2022 Dialpad, Inc. Permission is hereby granted, free of charge, to
any person obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


