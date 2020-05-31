from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    #use GET insted of post when you want to visible the url public or not too long unneseserry texts
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    capital = request.POST.get('capital','off')
    newline = request.POST.get('newline','off')
    space = request.POST.get('space','off')
    
    
    if removepunc == 'on':
        analyzed = ""
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'Analyzed_text': analyzed, 'purpose': 'your punctuation free list is : '}
        #return render(request,'analyze.html',params)        
        djtext = analyzed        
    if capital == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'Analyzed_text': analyzed,'purpose': 'your all capital list is : '}
        #return render(request,'analyze.html',params)
        djtext = analyzed
    if newline == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'Analyzed_text': analyzed,'purpose': 'your without newline list is : '}
        #return render(request,'analyze.html',params)
        djtext = analyzed
    if space == 'on':
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'Analyzed_text': analyzed,'purpose': 'your without newline list is : '}
        #return render(request,'analyze.html',params)          
        
    if(removepunc != 'on' and capital != 'on' and newline != 'on' and space != 'on'):
        return HttpResponse("please keep the remove punc button on ")

    return render(request,'analyze.html',params)    
