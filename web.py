from flask import Flask
from flask import render_template, redirect, url_for
import pandas as pd
import os

from pyecharts import options as opts
from pyecharts.charts import Bar, Page, Pie, Timeline, Line, Map
app = Flask(__name__)

#读数据

@app.route('/')
def index():
    return redirect(url_for('show_table', type='DMTX'))

@app.route('/show/<string:type>/', methods=['GET'])
def show_table(type):
    datas = []
    #判断类型读文件
    if type == 'DMTX':
        df = pd.read_csv('DMTX.csv', encoding='gbk')
        flag = 0
    elif type == "DXS":
        df = pd.read_csv('DXS.csv', encoding='gbk')
        flag = 1
    else:
        return '<font style="align:center;" size=36px color=red>505 请检查参数是否正确！！！</font>'
    #处理Nan
    df = df.fillna(0)
    for index, row in df.iterrows():
        datas.append(list(row))
    return render_template('show_table.html', datas=datas, flag=flag)

df2 = pd.read_csv('DXS.csv', encoding='gbk')
df = pd.read_csv('DMTX.csv',encoding='gbk')
x = [int(x) for x in df.columns.values[-9:]]


def timeline_pie1() -> Timeline:
    tl = Timeline()
    for i in range(2009, 2017):
        pie = (
            Pie()
                .add(
                "地面塌陷次数",
                list(zip(list(df.地区), list(df["{}".format(i)]))),
                rosetype="radius",
                radius=["30%", "55%"],
            )
                .set_global_opts(title_opts=opts.TitleOpts("中国各地区地面塌陷次数".format(i)))
        )
        tl.add(pie, "{}年".format(i))
    return tl


def timeline_pie2() -> Timeline:
    tl = Timeline()
    for i in range(2009, 2017):
        pie = (
            Pie()
                .add(
                "地下水水量",
                list(zip(list(df2.地区), list(df2["{}".format(i)]))),
                rosetype="radius",
                radius=["30%", "55%"],
            )
                .set_global_opts(title_opts=opts.TitleOpts("中国各地区地下水水量".format(i)))
        )
        tl.add(pie, "{}年".format(i))
    return tl


def timeline_bar1() -> Timeline:
    tl = Timeline()

    # 湖南地面塌陷次数
    N = list(df.loc[17].values)[-9:]
    # 广西地面塌陷次数
    G = list(df.loc[19].values)[-9:]
    # 河北地面塌陷次数
    B = list(df.loc[2].values)[-9:]
    # 江苏地面塌陷次数
    J = list(df.loc[9].values)[-9:]
    for i in range(2009, 2017):
        bar = (
            Bar()
                .add_xaxis(x)
                .add_yaxis("湖南", N)
                .add_yaxis("广西", G)
                .add_yaxis("河北", B)
                .add_yaxis("江苏", J)
                .set_global_opts(title_opts=opts.TitleOpts("中国部分地区{}年地面塌陷次数".format(i)))
        )
        tl.add(bar, "{}年".format(i))
    return tl


def timeline_bar2() -> Timeline:
    tl = Timeline()
    # 湖南地下水水量
    N2 = list(df2.loc[17].values)[-9:]
    # 广西地下水水量
    G2 = list(df2.loc[19].values)[-9:]
    # 河北地下水水量
    B2 = list(df2.loc[2].values)[-9:]
    # 江苏地下水水量
    J2 = list(df2.loc[9].values)[-9:]
    for i in range(2009, 2017):
        bar = (
            Bar()
                .add_xaxis(x)
                .add_yaxis("湖南", N2)
                .add_yaxis("广西", G2)
                .add_yaxis("河北", B2)
                .add_yaxis("江苏", J2)
                .set_global_opts(title_opts=opts.TitleOpts("中国部分地区{}年地下水水量".format(i)))
        )
        tl.add(bar, "{}年".format(i))
    return tl
#地面塌陷次数变化
def line_base1() -> Line:
    c = (
        Line()
            .add_xaxis(list(df.columns))
            .add_yaxis("湖南", list(df.loc[17]))
            .add_yaxis("广西", list(df.loc[19]))
            .add_yaxis("河北", list(df.loc[2]))
            .add_yaxis("江苏", list(df.loc[9]))

            .set_global_opts(title_opts=opts.TitleOpts(title="地面塌陷次数"))
    )
    return c

#地下水水量变化
def line_base2() -> Line:
    c2 = (
        Line()
            .add_xaxis(list(df2.columns))
            .add_yaxis("湖南", list(df2.loc[17]))
            .add_yaxis("广西", list(df2.loc[19]))
            .add_yaxis("河北", list(df2.loc[2]))
            .add_yaxis("江苏", list(df2.loc[9]))

            .set_global_opts(title_opts=opts.TitleOpts(title="地下水水量（亿立方米）"))
    )
    return c2


#地面塌陷地图可视化
def timeline_map() -> Timeline:
    tl = Timeline()
    for i in range(2009, 2017):
        map0 = (
            Map()
                .add(
                "地面塌陷", list(zip(list(df.地区), list(df["{}".format(i)]))), "china", is_map_symbol_show=False
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年地面塌陷".format(i), subtitle="",
                                          subtitle_textstyle_opts=opts.TextStyleOpts(color="red", font_size=18,
                                                                                     font_style="italic")),
                visualmap_opts=opts.VisualMapOpts(min_=0, max_=100),

            )
        )
        tl.add(map0, "{}年".format(i))
    return tl

def html_is_exits():
    if os.path.exists('templates/graph.html'):
        print(1)
        os.remove('templates/graph.html')

@app.route('/graph/<string:no>', methods=['GET'])
def graph(no):
    if int(no) >= 1 and int(no)<=7:
        if no == '1':

            timeline_pie1().render('templates/graph1.html')
        elif no == '2':

            timeline_pie2().render('templates/graph2.html')
        elif no == '3':

            line_base1().render('templates/graph3.html')
        elif no == '4':

            line_base2().render('templates/graph4.html')
        elif no == '5':

            timeline_bar1().render('templates/graph5.html')
        elif no == '6':

            timeline_bar2().render('templates/graph6.html')
        elif no == '7':

            timeline_map().render('templates/graph7.html')
        return render_template('graph'+ no +'.html')
    else:
        return '<font style="align:center;" size=36px color=red>505 请检查参数是否正确！！！</font>'



if __name__ == '__main__':
    app.run()