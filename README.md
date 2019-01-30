自助复制verdaccio库
========

> 从一个verdaccio搭建的npm库中下载所有的包，然后自动上传到另一个verdaccio目标库

基础环境
-----
> Python 3.6.4
> Python 2.7
> node v10.11.0

使用说明
-----
> 根据自己的需求，修改main.py中的原mpn地址，与包名的过滤条件。修改bat脚本中自定义内容

> 直接运行main.py文件,py文件会调用npm_test.bat批处理文件
	
> 如果需要修改目标库和上传的用户信息，请修改bat文件中的替换内容

> 如果py文件无法运行，可能里面使用的代理IP已失效，替换即可

> 如果是更新单个包，直接调用bat即可。格式：npm_test.bat packagename

注意事项
-----
> 1、如果遇到 node-gyp rebuild 报错，说明该包需要Python2.7，因为不支持node-gyp python3。
     解决方式：下载Python2.7,然后npm config set python /path/to/executable/python2.7