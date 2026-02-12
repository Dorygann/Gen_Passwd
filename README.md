# Gen_Passwd

```
usage: genpasswd.py [-h] [-l | --length LENGTH] [-S | --no-special] [-A | --no-ambiguous]
[-U | --no-uppercase] [-L | --no-lowercase] [-D | --no-digits] [-c | --count COUNT]

options:
  -h, --help           Show this help message and exit
  -l, --length LENGTH  Password length (default: 12)
  -S, --no-special     Disable special characters
  -A, --no-ambiguous   Disable ambiguous characters
  -U, --no-uppercase   Disable uppercase letters
  -L, --no-lowercase   Disable lowercase letters
  -D, --no-digits      Disable digits
  -c, --count COUNT    Generate x passwords (default: 1)
```

## Examples

```
you> python3 genpasswd.py -S -l 50 -c 3 
// Generating 3 passwords of 50 chars without special characters

CISCOgs0BurpYpTL18IULB8cZTIcwyx8nQMGrnNNY0cvuwLNPa
jKfCrb7ewXtjKIUVzZK4ByokJ0qiMoET3K0DNBysgBGt5GbJXf
2uLoiY0vQTOosodG15MOAXcsEz1nn33rz1KXzac4kbLH1Z0eU1
```
