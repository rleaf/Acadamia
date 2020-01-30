from javax.servlet.http import HttpServlet
from string import Template 

class hello(HttpServlet):
	def doGet(self, request, response):
		response.contentType = "text/html"
		out  = response.writer
		a = ['joe','sally','sue']
		s1 = a[0]
		s2 = a[1]
		for s in a:
			out.print(s + '-')
		
		buff = "<html><head></head><body>"
		buff += "<h1>Greetings from a jylet</h1>"
		x = 10
		if x == 10: 
			buff += '<h4>x is 10</h4>'
		
		s = Template('$who likes $what')
		d = dict(who='tim',what='money')
		d['who'] = 'fred'
		d['what'] = 'euros'
		
		d = {'who': 'James', 'what': 'francs'}
		buff += "<h3>" + s.substitute(d) + "</h3>"
		buff += "</body></html>"
		out.print(  buff )
	
	
