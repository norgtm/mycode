#!/usr/bin/env python3
# Accept any variation of the same 3 letter hostname

## Collect hostname
hostname = input('Please enter a hostname: ')

## Make it a common name
lower_hostname = hostname.lower()

## Test the common name
if lower_hostname == 'mtg':
    print('The hostname was found to be',hostname)
    print(hostname,'matches expected config')
    print('Exiting the script')
exit()
