from django.shortcuts import render
from .models import Data
import datetime
import random
# Create your views here.

imageLink = [
    "https://i.pinimg.com/736x/49/23/57/492357d5a3ea0e4f00b3294ab421b4c7.jpg",
    "https://i.pinimg.com/236x/c4/03/b5/c403b51c014e6753e327abd8e38269db.jpg",
    "https://64.media.tumblr.com/19bfb7fffae85f3fcb0a65e8c0851bcb/tumblr_pipeo8KbpW1xxxd2qo10_r1_400.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWwerNJX1QCowmFxmFs7KoBksGa0QQKEOBmw",
    "https://stickerswiki.ams3.cdn.digitaloceanspaces.com/Aldndosn/896455.512.webp",
    "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/3c8b03b6-013a-43d7-8b1e-e1c18852a527/dfthdd1-1bd38384-a330-4532-b6ba-2d9ecfd82d4a.png/v1/fill/w_250,h_250/oshi_no_ko_1_folder_by_rkasai14_dfthdd1-250t.png",
    "https://pbs.twimg.com/media/FMNfmj8WYAgT2si.jpg",
    "https://c4.wallpaperflare.com/wallpaper/89/543/779/anime-anime-girls-lycoris-recoil-nishikigi-chisato-inoue-takina-hd-wallpaper-preview.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxDUb0LpmHyTRqbsnXuuvmQaqKFydMeh1HvA",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiFpWwcWR9mhkJhRbNdQQHTRKFMxWnMWcT8w",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHf31DYC_7zxXdVV76-rfAY2Gm8DJX5lH0qQ",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiwDZaaetgFdlu5b6m_NrmP3HFDa-EO7SSXA",
    
]


def blog(request):
    # print(request)
    # if request.method == "POST":
    #     test = datetime.datetime.now().__str__()
    #     # print(test[:4], test[5:7], test[8:10], test[11:13], test[14:16])
    #     year = int(test[:4])
    #     mnt = int(test[5:7])
    #     dy = int(test[8:10])
    #     hr = int(test[11:13])
    #     mn = int(test[14:16])

    #     req_headers = request.META
    #     ip_addr = req_headers.get('REMOTE_ADDR')
    #     print(ip_addr)
    #     a = Data(textfield=request.POST['a'],time=datetime.datetime(year, mnt, dy, hr, mn, tzinfo=datetime.timezone.utc),sender=ip_addr)
    #     a.save()

    data = Data.objects.all().values()
    rel_data = []
    for x in data:
        rel_data.append([x["id"],x["textfield"],x["time"],x["sender"],random.choice(imageLink)])
        
    return render(request, 'main.html' ,{
        "data":rel_data,
    })