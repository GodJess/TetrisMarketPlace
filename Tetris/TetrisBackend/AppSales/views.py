from django.shortcuts import render, redirect
from Product.models import SalesMan, ProductModel, Snikers, cloth, CountProduct
from django.conf import settings
from Product.serializers import ProductSerializers
from django.http import JsonResponse
from rest_framework.response import Response
import json
import random



# Create your views here.
def main(request):
    salesMan = request.session.get(settings.SESSION_SALESMAN, {})
    product = json.dumps(ProductSerializers(ProductModel.objects.filter(salesman = salesMan.get('id')), many = True).data)

    data = {
        'product': product
    }
    return render(request, 'AppSales/salesApp.html', data)


def avtoriz(request):
    if request.method == "POST":
        request.session.pop(settings.SESSION_SALESMAN, None)
        activeUser = request.session.get(settings.SESSION_SALESMAN, {})
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        saler = SalesMan.objects.filter(phone=phone, password=password).first()
        print(saler)
        if saler:
            activeUser = {
               'id': saler.id ,'name': saler.salerName, 'shopName': saler.name, 'check': saler.countofmany, 'reting': saler.grade, 'logo': saler.user_img.url , 'header': saler.salesman_img.url , 
            }

            request.session[settings.SESSION_SALESMAN] = activeUser
            print('sucsess', activeUser['logo'], activeUser['header'])
            return redirect('main')
    return render(request, 'AppSales/avtoriz.html')


def register(request):
    return render(request, 'AppSales/register.html')


def LogOut(request):
    request.session.pop(settings.SESSION_SALESMAN, None)
    return redirect('main')


def AddProduct(request):
    activeSaler = request.session.get(settings.SESSION_SALESMAN, {})
    if request.method == "POST" and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        Success = False
        prod_name = request.POST.get('prod_name')
        prod_price = request.POST.get('prod_price')
        prod_discount = request.POST.get('prod_discount')
        prod_desc = request.POST.get('prod_desc')
        prod_date = request.POST.get('prod_date')
        prod_category = request.POST.get('prod_category')
        img1 = request.FILES['img1']
        img2 = request.FILES['img2']
        img3 = request.FILES['img3']

        linkToSize = Check()

        prod = ProductModel(
                name = prod_name, description = prod_desc, price = prod_price, img1 = img1, img2 = img2, img3 = img3,
                dateOfPublic = prod_date, discount = prod_discount, salesman = activeSaler['id'], type = prod_category, linkToSize = linkToSize 
        )
        prod.save()

        if prod_category == 'snikers':
            size36 = request.POST.get('36')
            size37 = request.POST.get('37')
            size38 = request.POST.get('38')
            size39 = request.POST.get('39')
            size40 = request.POST.get('40')
            size41 = request.POST.get('41')
            size42 = request.POST.get('42')
            size43 = request.POST.get('43')
            size44 = request.POST.get('44')
            size45 = request.POST.get('45')

            sizeSneakers = Snikers(
                indif = linkToSize, size36 = size36, size37 = size37, size38 = size38,
                size39 = size39, size40 = size40, size41 = size41, size42 = size42, size43 = size43, size44 = size44, size45 = size45
            )
            if sizeSneakers.save():
                Success = True


        elif prod_category == "shoes":
            s = request.POST.get('s')
            m = request.POST.get('m')
            l = request.POST.get('l')
            xl = request.POST.get('xl')
            xxl = request.POST.get('xxl')

            sizeCloth = cloth(indif = linkToSize, s = s, m =m, l=l, xl=xl, xxl=xxl)
            if sizeCloth.save():
                Success = True

        elif prod_category == 'product':
            count = request.POST.get('count')
            countProd = CountProduct(count = count, indif = linkToSize)
            if countProd.save():
                Success =True

        return JsonResponse({'success': Success})
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)
    

def Check():
    flag = True
    x = 0
    while(flag):
        x = random.randint(1, 10000000)
        if ProductModel.objects.filter(linkToSize = x).first():
            continue
        else:
            flag = False
    
    return x

def LoadPhoto(request):
    if request.method == "POST":
            salesMan = request.session.get(settings.SESSION_SALESMAN, {})
            photo = request.FILES.get('loadImg')
            slesman = SalesMan.objects.filter(id=salesMan.get('id')).first()

            if slesman:
                print('Пользователь найден')

                if photo.size > 0:
                    print('Длина отличная(:')
                    slesman.user_img.save(photo.name, photo, save=True)

                    salesMan['logo'] = slesman.user_img.url
                    request.session[settings.SESSION_SALESMAN] = salesMan

                    try:
                        slesman.save()
                        print('успешно')
                        return JsonResponse({'success': 'success'})
                    except Exception as e:
                        print(e)
                        return JsonResponse({'success': 'error'})
            return JsonResponse({'success': 'error'})
    else:
        return JsonResponse({'error': 'Invalid request method'})




    
