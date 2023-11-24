
from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse



# Create your views here.


challenge_text = {
  "January": "The crisp winter air filled the streets with a sense of calm and tranquility.",
  "February": "As Valentine's Day approached, the city adorned itself with hues of red and pink.",
  "March": "Blossoms began to appear, signaling the arrival of spring and a new beginning.",
  "April": "Showers embraced the earth, bringing life to the flowers and a promise of renewal.",
  "May": "Under the warm sun, families gathered for picnics, creating memories amidst nature's beauty.",
  "June": "Schools closed, and the summer heat invited everyone to enjoy lazy afternoons by the beach.",
  "July": "Fireworks painted the night sky, celebrating independence and unity.",
  "August": "The sunsets became more vibrant, casting a golden glow over the landscapes.",
  "September": "Leaves started to change color, and a gentle breeze whispered the arrival of autumn.",
  "October": "Pumpkin patches and apple orchards came to life, inviting harvest festivities.",
  "November": "Families gathered around tables, expressing gratitude for the blessings of the year.",
  "December": "Snowflakes danced in the air, creating a magical winter wonderland for all to enjoy."
}


def index(request):
  
  months = list(challenge_text.keys())
  
  return render(request,"challenges/index.html", {"months" : months})
 
  


def monthly_challenge_numbers(requests, month):
    redirect_months = list(challenge_text.keys())
    
    if month > len(redirect_months) :
        return HttpResponseNotFound("Invalid month!!")
    
    r = redirect_months[month] # months[0]
    r_m = reverse("monthly_challenges", args = [r])  #/chalenges/january
    
    return HttpResponseRedirect(r_m)
    # print(redirect_months)
    
    # return HttpResponse(requests)
    


def monthly_challenge(request, month):
    
    try:
      result = challenge_text[month] # value of month 
      month = month

      return render(request,"challenges/challenge.html" , {"text" : result , "month" :
        month })
      # response_data = render_to_string("challenges/challenge.html")
      # return HttpResponse(response_data)  
    except:  
       raise Http404()


    
    