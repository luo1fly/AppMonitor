# AppMonitor项目文档 #
## 简介 ##
> 定时执行检查线上webservice服务是否正常，选取接口由测试提供并审核，目录结构：

	[root@fedora-minion AppMonitor]# tree .
	.
	├── conf
	│   ├── api.json
	│   ├── __init__.py
	│   └── logger.conf
	├── core
	│   ├── __init__.py
	│   └── main.py
	├── index.py
	├── logs
	├── README.md
	└── utils
	    ├── __init__.py
	    ├── mailhandler.py
	    └── soaphandler.py
## 技术实现 ##
1.	第三方模块suds：[https://fedorahosted.org/suds/wiki/Documentation](https://fedorahosted.org/suds/wiki/Documentation)
2.	Python多进程Pool：[https://docs.python.org/3/library/multiprocessing.html?highlight=pool#module-multiprocessing.pool](https://docs.python.org/3/library/multiprocessing.html?highlight=pool#module-multiprocessing.pool)
