import requests
headers = \
{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

for j in range(56):
      
      url = 'https://comic.naver.com/bestChallenge/detail?titleId=740571&no={0}'.format(j)
      site = requests.get(url, headers=headers)
      source_data = site.text

      pos01 = source_data.find('<!-- 뷰어  -->') + len('<!-- 뷰어  -->')
      source_data = source_data[pos01:]

      pos02 = source_data.find('<!-- //뷰어 -->')
      source_data = source_data[:pos02]

      count = source_data.count('<img src="')

      for i in range(count):

            pos1 = source_data.find('<img src="') + len('<img src="')
            source_data = source_data[pos1:]

            pos2 = source_data.find('" title="')            
            extract_data = source_data[:pos2]

            source_data = source_data[pos2+1:]

            file_name = '{0}{1}{2}.jpg'.format(j+1, '  ' ,i+1)
            ss = requests.get(extract_data, headers=headers)
            file = open(file_name, 'wb')
            file.write(ss.content)

            file.close()

            print(i+1, extract_data)
