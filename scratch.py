
#Does not execute javascript
response = requests.get(YOUTUBE_TRENDING_URL)

#print('Status Code:',response.status_code)

#print('Output:',response.text[:1000])

#with open('trending.html','w') as f:
#  f.write(response.text)

doc = BeautifulSoup(response.text, 'html.parser')

print('Page title:',doc.title.text)

#Find all video divs
video_divs = doc.find_all('div', class_ = 'style-scope ytd-video-renderer')
print('Found {} videos'.format(len(video_divs)))