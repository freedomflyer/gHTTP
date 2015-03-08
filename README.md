# gHTTP
## About
gHTTP is a simple HTTP download client written in Python. 

## Usage
You will find a simple example in main.py. General usage is as follows:

```
url = "https://www.google.com/logos/doodles/2015/international-womens-day-2015-6218590910939136.2-hp.jpg"
gHTTP = gHTTP()
gHTTP.get(url)

with open('testimage.jpg', 'a') as the_file:
    the_file.write(gHTTP.raw_body_data)
```




