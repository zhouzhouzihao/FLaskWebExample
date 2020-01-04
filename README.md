
本次采用flask作为后台jinja2作为前端与后台逻辑代码进行交互，后台代码分为2部分， 
1. html制作
2. flask代码编写


1.html制作，采用简单的table标签和select标签呈现界面内容
2.flask代码编写
1）路由及说明: 1.show/DXS/ 展示地下水信息
              2.show/DMTX/显示地面塌陷信息
              3.show_graph/(1/2/3/4/5/6/7)展示图标信息
2）图表生成采用pyecharts

