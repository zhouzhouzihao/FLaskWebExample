# Python期末作业技术文档
github:[点击跳转](https://github.com/zhouzhouzihao/FLaskWebExample)  
pytonanywhere[点击跳转]('')  
本次作业设计主要以flask为后台，前端界面用jinja2及js实现了web服务器前后数据的交互
## HTML档描述

### 一、FLASK 描述
* 1、html文件分为
  show_table.html: 配合web.py文件中的show_table函数传入前端的变量进行判断显示不同的表格数据
  graph(1/2/3/4/5/6/7).html: 选择下拉框与后台代码交互生成图表的html
  
- 2、flask逻辑描述
  1.后台代码的编写
  1）@app.route('/')
      def index():
          return redirect(url_for('show_table', type='DMTX'))
     代码实现了首页加载的跳转功能，直接跳转到表格界面
   2）@app.route('/show/<string:type>/', methods=['GET'])这行代码的路由时/show/.*？
      接受前端传来的show/后面的type的值，并且进行判断执行不同的函数，显示不同的表格数据
   3）利用pyecharts函数生成图表，函数名如下：
      timeline_pie1 图表1
      timeline_pie2 图表2
      timeline_bar1 图表3
      timeline_bar2 图表4
      line_base1 图表5
      line_base2 图表6
      timeline_map 图表7
   4）@app.route('/graph/<string:no>', methods=['GET'])用来接收前端传来的/graph/(no)中的get请求判断图表编号
      主要逻辑为前端下拉框变化后执行MM_jumpMenu('parent',this,0)js函数，获取每个option标签中的value值并根据value值实现页面的跳转，graph(no)接收       前端传来的url中的no值进行判断在执行相应的图表生成函数最后用render_template函数使用模板，显示图表。
### 二、FLask动作表述：
     进入首页自动跳转到/show/DMTX, 选择下拉框进行跳转， 点击查看地下水跳转到/show/DXS
