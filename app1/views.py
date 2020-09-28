from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    capitalize=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremove','off')
    extraspaceremover=request.POST.get('extraspaceremove','off')
    if removepunc=="on" and (len(djtext)>0):
        punctuations="!@#$%^&*()_+:;?><,./\{}[]"
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
                param={'purpose':'Removed Punctuatios','analyzed_text':analyzed}
                djtext=analyzed
    if capitalize=="on":
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.upper()
            param={'purpose':'Changed to Uppercase','analyzed_text':analyzed}
            djtext=analyzed
    if newlineremover=="on":
        analyzed=''
        for char in djtext:
            if char !="\n" and char!='\r':
                analyzed=analyzed+char
                param={'purpose':'Removed Newline','analyzed_text':analyzed}
                djtext=analyzed
    if extraspaceremover=="on":
        analyzed=''
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
                param = {'purpose': 'Removed Extra space', 'analyzed_text': analyzed}
        djtext=analyzed
    if (removepunc!="on" and extraspaceremover!="on" and newlineremover!="on" and capitalize!="on"):
        return HttpResponse('error')
    return render(request,'analyzetext.html',param)
