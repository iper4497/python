import urllib2
def getPage(self, a):
		pageURL = 'http://www.' + str(a)                  
		req = urllib2.Request(pageURL)
		print 'Opening ' + pageURL
		resp = urllib2.urlopen(req)
		self.page += 1
		try:
			page = resp.read()
		except httplib.IncompleteRead, e: #??IncompleteRead??
			print 'IncompleteRead ' + pageURL
			page = e.partial
		return page
getPage('google.es')