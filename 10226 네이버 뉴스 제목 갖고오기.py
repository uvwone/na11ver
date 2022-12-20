#requests 모듈을 이용해서
#네이버 뉴스 메인화면에서 있는 뉴스들 제목 전체 가져오기
import requests
#headers없으면 네이버가 요청차단
headers = \
{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

url = 'http://www.todayhumor.co.kr/board/list.php?table=bestofbest'
site = requests.get(url, headers=headers)
source_data = site.text

count = source_data.count('<tr class="view')

def count(*pos1, source_data, extract_data):

       for i in range(count):
              pos1 = source_data.find('top">') + len('top">')
              source_data = source_data[pos1:]

              pos2 = source_data.find('</a>')
              extract_data = source_data[:pos2]

              pos3 = source_data.find('<span')
              source_data = source_data[pos3:]

              source_data = source_data[pos3+1:]
              print(i+1, extract_data.strip())
              
              return count
       
       #쌤 어케 해여
