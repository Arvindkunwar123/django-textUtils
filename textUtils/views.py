from django.http import HttpResponse
from django.shortcuts import render


class Pipe:
    def __init__(self):
        pass
        
    def index(self, request):
        return HttpResponse(render(request, "index.html"))

    def analyse(self, request):
        removePuncBool = request.GET.get("removePunc", "off")
        capFirstBool = request.GET  .get("capFirst", "off")
        newLineRemoveBool = request.GET.get("newLineRemove", "off")
        spaceRemoveBool = request.GET.get("spaceRemove", "off")
        charCountBool = request.GET.get("charCount", "off")

        result = request.GET.get("textArea", "No text provided")
        chars = None

        if removePuncBool == "on":
            result = self.removePunc(request, text=result)
            print(result)
        if spaceRemoveBool == "on":
            result = self.spaceRemove(request, text=result)
            print(result)
        if capFirstBool == "on":
            result = self.capFirst(request, text=result)
            print(result)
        if newLineRemoveBool == "on":
            result = self.newLineRemove(request, text=result)
            print(result)
        if charCountBool == "on":
            chars = self.charCount(request, text=result)
            results = {"result": result + f"\n\n\nNo. of characters: Including spaces = {chars['Including spaces']}\n \t\t\t   Without spaces = {chars['Without spaces']}"}
        else:
            results = {"result": result}

        return render(request, "analyse.html", results)

    def removePunc(self, request, text=""):
        if not text:
            return Tools(method="removePunc", text=request.GET.get("textArea", "No text provided")).removePunc()
        else:
            return Tools(method="removePunc", text=text).removePunc()

    def capFirst(self, request, text=""):
        if not text:
            return Tools(method="capFirst", text=request.GET.get("textArea", "No text provided")).capFirst()
        else:
            return Tools(method="removePunc", text=text).capFirst()

    def newLineRemove(self, request, text=""):
        if not text:
            return Tools(method="newLineRemove", text=request.GET.get("textArea", "No text provided")).newLineRemove()
        else:
            return Tools(method="removePunc", text=text).newLineRemove()

    def spaceRemove(self, request, text=""):
        if not text:
            return Tools(method="spaceRemove", text=request.GET.get("textArea", "No text provided")).spaceRemove()
        else:
            return Tools(method="removePunc", text=text).spaceRemove()

    def charCount(self, request, text=""):
        if not text:
            return Tools(method="charCount", text=request.GET.get("textArea", "No text provided")).charCount()
        else:
            return Tools(method="removePunc", text=text).charCount()


class Tools:
    def __init__(self, method, text=""):
        self.text = text

    def removePunc(self):
        puncs = r"""#$%@!^&*()_+=-[];',.`~/{}:"<>?\|"""
        for punc in puncs:
            self.text = self.text.replace(punc, "")
        
        return self.text
    
    def capFirst(self):
        self.text = self.text.capitalize()
        return self.text
    
    def newLineRemove(self):
        self.text = self.text.replace("\n", "")
        return self.text
    
    def spaceRemove(self):
        self.text = self.text.replace("  ", "")
        return self.text
    
    def charCount(self):
        return {"Including spaces": len(self.text),
                "Without spaces": len(self.text.replace(" ", ""))}
    
    
    
