import time
import imghdr
import os
from gHTTP import gHTTP

url = "https://cdn3.vox-cdn.com/thumbor/P9YdxUVRmkY8Em797JBw0n7egos=/233x0:550x317/500x500/cdn0.vox-cdn.com/uploads/chorus_image/image/45691044/Screen_Shot_2015-02-14_at_10.57.41_AM.0.0.png"
url2 = "http://runnersonthego.com/Assets/img/rotg-logos/RunnersOTG-300x225.jpg"

gHTTP = gHTTP()
gHTTP.get(url)

# Create temp file, determine file type
with open('temp', 'a') as the_file:
    the_file.write(gHTTP.raw_body_data)
filetype = imghdr.what("temp")
os.remove("temp")

# Create filename and use determined filetype to write actual file
filename = time.time()
with open('received/%d.%s' % (time.time(),filetype), 'a') as the_file:
    the_file.write(gHTTP.raw_body_data)