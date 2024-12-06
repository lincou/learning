import urllib.request

# 前半部分的链接
url_pre = 'https://www.yshblog.com'

# GET参数
params = {'wd': '测试'}
url_params = urllib.parse.urlencode(params)
url = f'{url_pre}?{url_params}'

# 发送请求
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

try:
    with open('test.txt', 'w', encoding='gbk') as f:
        f.write(html)
except UnicodeEncodeError:
    # 处理编码错误，例如替换无法编码的字符
    html = html.encode('gbk', 'replace').decode('gbk')
    with open('test.txt', 'w', encoding='gbk') as f:
        f.write(html)


