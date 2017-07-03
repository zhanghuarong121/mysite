from django.template.loader import get_template
from django.http import HttpResponse,Http404
from django.template import Template,Context
from django.shortcuts import render_to_response
import datetime
import MySQLdb
def book_list(request):
    db=MySQLdb.connect(user='root',db='mydb',passwd='zhanghuarong',host='localhost')
    cursor=db.cursor()
    cursor.execute('select name from books order by name')
    names=[row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('book_list.html',{'names':names})
def hello(request):
    return HttpResponse("Hello world")
def my_homepage_view(request):
    return HttpResponse("Page not found")
def current_datetime(request):
    now=datetime.datetime.now()
    t=get_template('mytemplate.html')
    c=Context({'current_time':now})
    #html=t.render({'current_time':now})
    html=t.render(c)
    return HttpResponse(html)
    #return render_to_response('mytemplate.html',{'current_time':now})
def hours_ahead(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    html="<html><body>In %s hour(s),it will be %s.</body></html>"%(offset,dt)
    return HttpResponse(html)
