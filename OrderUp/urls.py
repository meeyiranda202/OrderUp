from django.conf.urls import url , include
from OrderUp import views

urlpatterns = [
    url(r'^$',views.main, name ='main'),
    url(r'^createResturant$',views.createResturant,name='createResturant'), 
    url(r'^addResturant$',views.addResturant,name='addResturant'), 
    url(r'^viewresturant/(?P<id>\d+)$',views.viewresturant,name='viewresturant'),
    url(r'^addOrder/(?P<id>\d+)$',views.addOrder,name='addOrder'),
    url(r'^get_photo/(?P<id>\d+)$', views.get_photo, name='get_photo'), 
    url(r'^checkout/(?P<id>\d+)$', views.checkout ,name='checkout'), 
    url(r'^placeorder/(?P<id>\d+)$', views.placeorder ,name='placeOrder'), 
    url(r'^viewOrder/(?P<id>\d+)$', views.vieworder ,name='viewOrder'), 
    url(r'^myOrder/(?P<ordernumber>\d+)$', views.myorder ,name='myOrder'), 
    url(r'^findmyOrder$', views.findmyorder ,name='findmyOrder'), 
    url(r'^login$', views.login,name='login'), 
    url(r'^editOrder/(?P<id>\d+)$', views.editorder,name='editOrder'),                  
    url(r'^getlist/(?P<id>\d+)$',views.getlist,name='getlist'), 
    # url(r'^usermain$',bubbles_views.usermain, name ='usermain'), 
    # url(r'^register$',bubbles_views.register, name ='register'),
    # url(r'^addchat$', bubbles_views.addchat,name = 'addchat'),
    # url(r'^getlist$', bubbles_views.getlist,name='getlist'),
    # url(r'^logout$', auth_views.logout_then_login,name='logout'),
    # url(r'^gettime$', bubbles_views.gettime,name='gettime'),
    # url(r'^viewresult$', bubbles_views.viewresult,name='viewresult'),
    # url(r'^profile/(?P<id>\d+)$', bubbles_views.profile,name='profile'),
    # url(r'^add_Like/(?P<id>\d+)$', bubbles_views.addLikes,name='add_Like'),
    # url(r'^showresult$', bubbles_views.showresult,name='showresult'),
    # url(r'^share$', bubbles_views.share,name='share'),
    # url(r'^feedback$', bubbles_views.feedback,name='feedback'),
]