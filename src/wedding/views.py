from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

context = {
    'title': 'Wedding',
}

def index(request):
    from os import listdir, pardir
    from os.path import isfile, join, dirname, abspath
    from math import ceil

    gallerypath = dirname(dirname(abspath(__file__))) + '/assets/img/gallery'
    thumb_gallerypath = gallerypath + '/thumbnails'

    # M = {x | x in S and x even}
    # this is read ( image for images in gallerypath and image is a file)
    images = list((img for img in listdir(gallerypath) if isfile(join(gallerypath, img))))
    thumbnails = list((thumb for thumb in listdir(thumb_gallerypath) if isfile(join(thumb_gallerypath, thumb))))
    num_images = ceil(len([f for f in listdir(gallerypath)if isfile(join(gallerypath, f))]) / 6)

    # gallery = Gallery(num_images, images, thumbnails)


    return render(request, 'wedding/index.html', {
        'page_to_load': 'wedding/home.html',
        'num_images': num_images,
        'images': images,
        'thumbnails': thumbnails,
        })

def accommodations(request):
    return render(request, 'wedding/index.html', { 'subpage': 'true', 'page_to_load': 'wedding/accommodations.html' } )


class Gallery:
    def __init__( num_images, images, thumbnails):
        self.num_images = num_images
        self.images = images
        self.thumbnails = thumbnails
