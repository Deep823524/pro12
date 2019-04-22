from django.shortcuts import render

def show(request):

    return render(request, "index1.html")

def display(request):

    res = request.POST.getlist("cb")
    if len(res) == 0:
        data = {"pkk": "Please Select one"}
    elif len(res) == 1:
        if res[0] == "Movies":
            data = {"movies": ["Gully Boy", "Alita: Battle Angel", "The Surgical Strike", "Dev", "Manikarnika"]}
        elif res[0] == "Cartoon":
            data = {"cartoon": ["Bugs Bunny", "Mickey Mouse", "Tweety", "Popeye", "Daffy Duck"]}
        else:
            data = {"images": [".JPG", ".PNG", ".GIF", ".BMP", ".TIFF"]}
    elif len(res) == 2:
        if "Movies" in res and "Cartoon" in res:
            data = {"movies": ["Gully Boy", "Alita: Battle Angel", "The Surgical Strike", "Dev", "Manikarnika"],
                    "cartoon": ["Bugs Bunny", "Mickey Mouse", "Tweety", "Popeye", "Daffy Duck"]}
        elif "Movies" in res and "Images" in res:
            data = {"movies": ["Gully Boy", "Alita: Battle Angel", "The Surgical Strike", "Dev", "Manikarnika"],
                    "images": [".JPG", ".PNG", ".GIF", ".BMP", ".TIFF"]}
        else:
            data = {"cartoon": ["Bugs Bunny", "Mickey Mouse", "Tweety", "Popeye", "Daffy Duck"],
                    "images": [".JPG", ".PNG", ".GIF", ".BMP", ".TIFF"]}
    else:
        data = {"movies": ["Gully Boy", "Alita: Battle Angel", "The Surgical Strike", "Dev", "Manikarnika"],
                "cartoon": ["Bugs Bunny", "Mickey Mouse", "Tweety", "Popeye", "Daffy Duck"],
                "images": [".JPG", ".PNG", ".GIF", ".BMP", ".TIFF"]}

    return render(request, "details.html", data)

