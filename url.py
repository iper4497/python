import pycurl
import urllib
 
url = 'https://trisquel.info'
 
post_vars = { 'name': 'minipost',
              'pass': 'RinDedgoofOnekOovVeducarvebrej',
              'form_id': 'user_login'}
 
c = pycurl.Curl()
c.setopt(pycurl.URL, url)
c.setopt(pycurl.POSTFIELDS, urllib.urlencode(post_vars))
c.setopt(pycurl.COOKIEJAR, 'cookie.txt') 
c.perform()
c.close()
