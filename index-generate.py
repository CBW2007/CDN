'''
	Name: index-generate
	Programing language: Python3
	Copyright: CC BY-SA 4.0
	Author: CBW2007,QAQAutoMaton
	Date: 2019/04/15
	Description: 以老K的博客中的代码为基础进行完善的代码，可以自动生成索引。 
'''
import os
import io
title='CBW2007的CDN'
blacklist=['.git','index.html','CNAME','404.html']
def make(s):
	d=os.listdir('.')
	with open('index.html','w') as f:
		f.write('<!DOCTYPE html>\n')
		f.write('<html lang="zh-CN">\n')
		f.write('<head>\n')
		f.write('	<meta charset="GB2312">\n')
		f.write('	<title>{0}</title>\n'.format(title))
		f.write('	<link rel="icon" href="/logo.png"/>\n')
		f.write('</head>\n')
		f.write('<body>\n')
		f.write('	<h1><center>{0}</center></h1>\n'.format(title))
		f.write('	<h2>{0}  的索引</h2>\n'.format(s))
#		f.write('<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>{0}</title></head><body><h1>{0}</h1><ul>\n'.format(title))
#		f.write('<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>{0}的索引</title></head><body><h2>{0}的索引</h1><ul>\n'.format(s))
		if(s!='/'):
			f.write('<a href="../">返回上层目录</a>')
		f.write('<ul>\n')
		for i in d:
			if(not(i in blacklist)):
				if(os.path.isdir(i)):
					os.chdir(i)
					make(s+i+'/')
					os.chdir('..')
					f.write('<li><a href="{0}">{0}/</a></li>\n'.format(i))
				else:
					f.write('<li><a href="{0}">{0}</a></li>\n'.format(i))
		f.write('</ul>')
		f.write('<hr>')
		f.write('我的博客：<a href="https://www.cbw2007.tk/">https://www.cbw2007.tk/</a>，欢迎光临！</br>\n')
		f.write('<center>Powered by GitHubPages</center>\n')
		
		print('[INFO] The index of \'{0}\' generated.'.format(s))
make('/')
print('[INFO] Done!')