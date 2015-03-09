import requests,re

class A:
	def __init__(self,url):
		self.resp=requests.get(url)
		self.buf=self.resp.content
	def get_link(self):
		temp=[]
		temp=re.findall("<img.*?>",self.buf,re.S)
		self.all_link=temp
		
	def get_link_count(self):
		if hasattr(self,"all_link")==False:
			self.get_link()
		return len(self.all_link)

a1=A("http://www.sina.com.cn")
print a1.get_link_count()
'''a2=A("http://www.sohu.com")
print a2.get_link_count()
class B(A):
	pass
b1=B("http://www.sina.com.cn")
print b1'''