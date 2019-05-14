from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image,Category,Location



global locations,categories
locations=["NationalPark","Gymstore", "ParadiceLost",
"TreebeadsTexas",
            "MombasaCity"]
categories=["Diet","Fashion","Exercise"]


# Create your views here.
def index (request):
    '''
    Handles requests for the homepage
    renders index.hmtl with the following params title, photos, locations and categories
    '''

    title = 'Welcome'
    photos = Image.objects.all()
    return render(request, 'index.html',{"title": title,"photos": photos,"locations":locations,"categories":categories})



def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_by_Category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',
                      {"message": message, "photos": searched_image, "locations": locations, "categories": categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message, "locations": locations, "categories": categories})


def get_image_by_location(request,loc):
    # check if the input field exists and that ic contains data
    searched_images = Image.filter_by_Location(loc)
    caption = f'{loc}'
    if len(searched_images) == 0:
        searched_images = Image.all_photos()
        searched_image = Image.search_by_Category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": searched_image,"locations":locations,"categories":categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message,"locations":locations,"categories":categories})



    return render(request, 'locations.html', {"photos": searched_images,"caption":caption,"locations":locations,"categories":categories})

def category_results(request, cat):
    # check if the input field exists and that ic contains data
    searched_images = Image.filter_by_Category(cat)
    caption = f'{cat}'
   
    return render(request, 'index.html', {"photos": searched_images,"caption":caption,"locations":locations,"categories":categories})
           
           


