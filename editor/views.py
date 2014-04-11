from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from editor.models import UserDetail



def get_countries():
    countries = []
    countries_file = open('/home/sahyadrivps/webapps/identities_editor/myproject/editor/countries.txt','r')
    f = countries_file.read()
    for i in f.split('\n'):
        countries.append(i)
    countries_file.close()
    return countries



@csrf_exempt
def registration_page(request):
    if request.method == 'POST':

        user = User.objects.create_user(first_name=request.POST['inputFirst'], last_name=request.POST['inputLast'], username=request.POST["inputUser"], email=request.POST['inputEmail'], password=request.POST['inputPassword'])
        user.save()
        user_detail = UserDetail.objects.create(username1=request.POST['inputUser'], country=request.POST['inputCountry'], age=request.POST['inputAge'])
        return HttpResponseRedirect("http://wie.sahyadrivps.webfactional.com/editor/registration_successful/")
        
    else:
        countries = get_countries()
        
        return render_to_response("registration_page.html", {'countries':countries,})
    


@csrf_exempt    
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
    	
        if user is not None and user.is_active:        
            auth.login(request, user)
            request.session['username'] = request.POST.get('username')
            return HttpResponseRedirect("http://wie.sahyadrivps.webfactional.com/editor/loggedin/")
        else:           
            return HttpResponseRedirect("http://wie.sahyadrivps.webfactional.com/editor/invalid/")
            
    else:
        profiles = []
        identities = User.objects.order_by('first_name')
        for i in identities:
            profiles.append([str(i.first_name), str(i.last_name) ,str(i.username)])
        return render_to_response("login_page.html",{'profiles':profiles,})



        	
def logging_out(request):
    auth.logout(request)
    return HttpResponseRedirect("http://wie.sahyadrivps.webfactional.com/editor/loggedout/")




@csrf_exempt    
def loggedin(request):
    if 'username' in request.session:
        if request.method == 'POST':
            edit_identity = User.objects.get(username=str(request.session['username']))
            edit_details = UserDetail.objects.get(username1=request.session['username'])
            edit_identity.first_name = request.POST.get('first_name')
            edit_identity.last_name = request.POST.get('last_name')
            edit_identity.email = request.POST.get('email')
            edit_detials = request.POST.get('age')
            edit_details.country = request.POST.get('country')
            edit_identity.save()
            edit_details.save()

        username = str(request.session['username'])
        identity = User.objects.get(username=username)
        details = UserDetail.objects.get(username1=username)
        first_name = identity.first_name
        last_name = identity.last_name
        email = identity.email
        country = details.country
        age = details.age
        countries = get_countries()

        return render_to_response('loggedin.html',{'username':username, 'first_name':first_name, 'last_name':last_name, 'email':email, 'country':country, 'age':age, 'countries':countries,})
    else:
        return render_to_response('not_logged_in.html')
    



def user_profile(request, username):
    username = str(username)
    identity = User.objects.get(username=username)
    details = UserDetail.objects.get(username1=username)
    first_name = identity.first_name
    last_name = identity.last_name
    email = identity.email
    country = details.country
    age = details.age

    return render_to_response('userprofile.html',{ 'first_name':first_name, 'last_name':last_name, 'email':email, 'country':country, 'age':age,})



def invalid(request):
    return render_to_response('invalid.html')



     
    
def registration_successful(request):
    return render_to_response('registration_successful.html')



	
def loggedout(request):
    return render_to_response('loggedout_page.html')
	
