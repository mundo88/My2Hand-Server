from django.http import JsonResponse
import json
from pytube import Playlist

def story(request):
    context = [{
        'story': {
            'url': 'https://cdn.dribbble.com/users/301809/screenshots/13946426/mushrooms_dribbble-01_1x.png',
            'thumbnail': 'https://cdn.dribbble.com/users/301809/screenshots/13946426/mushrooms_dribbble-01_1x.png',
            'id': 1
        },
        'user': {
            'profile_picture': 'https://cdn.dribbble.com/users/39185/screenshots/2624995/ghostinlove_r_1x.jpg',
            'name': 'David Dang'
        }
    },
        {
        'story': {
            'url': 'https://cdn.dribbble.com/users/788099/screenshots/8586859/girl_swimsuit_kit8-net_1x.png',
            'thumbnail': 'https://cdn.dribbble.com/users/788099/screenshots/8586859/girl_swimsuit_kit8-net_1x.png',
            'id': 2
        },
        'user': {
            'profile_picture': 'https://cdn.dribbble.com/users/1044993/screenshots/11918320/adventure-dog_dribbble_1x.png',
            'name': 'Minh Phèng'
        }
    },
        {
        'story': {
            'url': 'https://cdn.dribbble.com/users/3178178/screenshots/7013817/the_caravan_by_patryk_wojciechowicz_1x.png',
            'thumbnail': 'https://cdn.dribbble.com/users/3178178/screenshots/7013817/the_caravan_by_patryk_wojciechowicz_1x.png',
            'id': 3
        },
        'user': {
            'profile_picture': 'https://cdn.dribbble.com/users/305512/screenshots/2869642/pikachu_1x.png',
            'name': 'Quinn Cu'
        }
    },
        {
        'story': {
            'url': 'https://cdn.dribbble.com/users/175166/screenshots/9878330/coronavirus_1x.jpg',
            'thumbnail': 'https://cdn.dribbble.com/users/175166/screenshots/9878330/coronavirus_1x.jpg',
            'id': 4
        },
        'user': {
            'profile_picture': 'https://cdn.dribbble.com/users/1355613/screenshots/15252730/____3_1x.jpg',
            'name': 'Trần Tú'
        }
    },
        {
        'story': {
            'url': 'https://cdn.dribbble.com/users/301809/screenshots/13946426/mushrooms_dribbble-01_1x.png',
            'thumbnail': 'https://cdn.dribbble.com/users/301809/screenshots/13946426/mushrooms_dribbble-01_1x.png',
            'id': 5
        },
        'user': {
            'profile_picture': 'https://cdn.dribbble.com/users/39185/screenshots/2624995/ghostinlove_r_1x.jpg',
            'name': 'David Dang'
        }
    },
        {
        'story': {
            'url': 'https://cdn.dribbble.com/users/719060/screenshots/11211105/rogers_drib2_1x.jpg',
            'thumbnail': 'https://cdn.dribbble.com/users/719060/screenshots/11211105/rogers_drib2_1x.jpg',
            'id': 6
        },
        'user': {
            'profile_picture': 'https://cdn.dribbble.com/users/719060/screenshots/11211105/rogers_drib2_1x.jpg',
            'name': 'Khum co ten'
        }
    },
        {
        'story': {
            'url': 'https://cdn.dribbble.com/users/301809/screenshots/13946426/mushrooms_dribbble-01_1x.png',
            'thumbnail': 'https://cdn.dribbble.com/users/301809/screenshots/13946426/mushrooms_dribbble-01_1x.png',
            'id': 7
        },
        'user': {
            'profile_picture': 'https://cdn.dribbble.com/users/39185/screenshots/2624995/ghostinlove_r_1x.jpg',
            'name': 'David Dang'
        }
    },
        {
        'story': {
            'url': 'https://cdn.dribbble.com/users/511174/screenshots/3315405/wonderboat_1x.gif',
            'thumbnail': 'https://cdn.dribbble.com/users/511174/screenshots/3315405/wonderboat_1x.gif',
            'id': 8
        },
        'user': {
            'profile_picture': 'https://cdn.dribbble.com/users/511174/screenshots/3315405/wonderboat_1x.gif',
            'name': 'Lung thi Ling'
        }
    },
        {
        'story': {
            'url': 'https://cdn.dribbble.com/users/31752/screenshots/2872268/dunn_s_motors_skull_v4_1x.jpg',
            'thumbnail': 'https://cdn.dribbble.com/users/31752/screenshots/2872268/dunn_s_motors_skull_v4_1x.jpg',
            'id': 9
        },
        'user': {
            'profile_picture': 'https://cdn.dribbble.com/users/31752/screenshots/2872268/dunn_s_motors_skull_v4_1x.jpg',
            'name': 'Thái Sơn'
        }
    },
        {
        'story': {
            'url': 'https://cdn.dribbble.com/users/59947/screenshots/5099288/muti_1x.jpg',
            'thumbnail': 'https://cdn.dribbble.com/users/59947/screenshots/5099288/muti_1x.jpg',
            'id': 10
        },
        'user': {
            'profile_picture': 'https://cdn.dribbble.com/users/59947/screenshots/5099288/muti_1x.jpg',
            'name': 'Camay'
        }
    }
    ]
    return JsonResponse({'data': context})


def posts(request):
    f = open('api/data/posts.json',encoding='utf-8')
    posts = json.load(f)
    return JsonResponse(posts)

def categories(request):
    f = open('api/data/categories.json',encoding='utf-8')
    categories = json.load(f)
    return JsonResponse(categories)
def category(request,category_id=1):
    f = open('api/data/categories.json',encoding='utf-8')
    categories = json.load(f)['categories']
    category = [x for x in categories if x.get('id') == category_id]
    return JsonResponse(category[0])
def products(request):
    f = open('api/data/products.json',encoding='utf-8')
    products = json.load(f)
    return JsonResponse(products)
def product(request,product_id=12):
    f = open('api/data/products.json',encoding='utf-8')
    products = json.load(f)['products']
    product = [x for x in products if x.get('id') == product_id]
    return JsonResponse(product[0])
def users(request):
    f = open('api/data/users.json',encoding='utf-8')
    users = json.load(f)
    return JsonResponse(users)
def user(request,user_id=1):
    f = open('api/data/users.json',encoding='utf-8')
    users = json.load(f)['users']
    user = [x for x in users if x.get('id') == user_id]
    return JsonResponse(user[0])

def youtubePlaylist(request):
    # p = Playlist('https://www.youtube.com/watch?v=11XkLOIsLHI&list=PLn7c8RY7CfPbs_XTnBFv7Z72f8J9ghWY-').videos
    # data = []
    # for video in p:
    #     streams = video.streams
    #     itag = streams.get_by_itag(137)
    #     if itag is not None:
    #         data.append({'url':itag.url}) 
    # youtube = {
    #     'youtube':data
    # }
    f = open('api/data/youtube.json',encoding='utf-8')
    youtube = json.load(f)
    return JsonResponse(youtube)