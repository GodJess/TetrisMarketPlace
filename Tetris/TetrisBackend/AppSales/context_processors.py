from django.conf import settings

def dataUser(request):
    activeUser = request.session.get(settings.SESSION_SALESMAN, {})
    
    dataUser = {
        'id': activeUser.get('id', ''),
        "name": activeUser.get('name', ''),
        "shopName": activeUser.get('shopName', ''),
        "check": activeUser.get('check', ''),
        "reting": activeUser.get('reting', ''),
         "logo": activeUser.get('logo', ''),
        "header": activeUser.get('header', ''),
        'length': len(activeUser),
    }
    

    return {'dataUser': dataUser}