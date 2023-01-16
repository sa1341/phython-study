import requests
import csv
import datetime as dt

url = 'https://jsonplaceholder.typicode.com/posts'
requestData = requests.get(url)
jsonData = None

date = dt.datetime.now()
fileName = "tfpu9880_" + str(date.year) + str(date.month) + str(date.day) + ".csv"

# with문을 사용하면 with 블록(with 문에 속해있는 문장)을 벗어나는 순간 열린 파일 객체 f가 자동으로 close된다.
with open(fileName, 'w', newline = '') as output_file :
    f = csv.writer(output_file)
    f.writerow(['user_id', 'title'])

    if requestData.status_code == 200:
        jsonData = requestData.json()
        for post in jsonData:
            print(post)
            f.writerow([post['userId'], post['title']])
