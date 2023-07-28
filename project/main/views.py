from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,StreamingHttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from main.models import News
from django.urls import reverse

def show_news(request):
    if request.method == 'POST':
        news_count = int(request.POST.get('news_count',5)) 
        all_news = News.objects.all()[0:news_count:1]
        context = {'all_news':all_news}
        return HttpResponse(get_template('show_news.html').render(context=context,request=request),status=200)
    elif request.method == 'GET':
        return HttpResponse(get_template('show_news.html').render(request=request),status=200)

def new_page(request,id):
    new = get_object_or_404(News,id=id)
    if new is not None:
        StringHtml = f'<h1 style="text-align:center;text-decoration:underline;color:black;">{new.title}</h1>\
            <p><strong>{new.body}</strong></p><br/><br/><br/><a href="/">Назад</a>'
        return StreamingHttpResponse(StringHtml)

def edit_page(request,id):
    if request.method == 'POST':
        NewData = request.POST
        OldData = News.objects.filter(id=id).first()
        OldData.title = NewData['title']
        OldData.body = NewData['body']
        OldData.save(update_fields=['title','body'])
        url = reverse('show_news')
        return redirect(url)
    else:
        old_data = News.objects.get(id=id)
        context = {'old_data':old_data}
        return render(request,template_name='edit_page.html',context=context)

def delete_new(request,id):
    News.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('show_news'),status=302,reason='show_updated_page')

def add_new(request):
    if request.method != 'GET':
        add = News.objects.create(
            title = request.POST['title'],
            body = request.POST['body']
        )
        add.save(update_fields=['title','body'])
        return redirect(reverse('show_news'))
    else:
        return render(request,'add_new.html')