from urllib import request

goog_url = ''


def download_info(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str()
    lines = csv_str.split('\\n')
    dest_url = r'goog_csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_info(goog_url)