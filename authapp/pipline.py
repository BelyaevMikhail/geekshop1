from datetime import datetime

from django.contrib.sites import requests
from django.utils import timezone

from authapp.models import ShopUserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend != 'vk-oauth2'
        return

    api_url = f"https://api.vk.com/method/users.get?fieleds=bdate,sex,about&access token={response['access_token']}"

    vk_response = requests.get(api_url)

    if vk_response.ststus_code != 200
        return

    vk_data = vk_response.json(['response'][0])

    if vk_data['sex']:
        if vk_data['sex'] ==2:
            user.shopuserprofile.gender = ShopUserProfile.MALE
        elif vk_data['sex'] ==1:
            user.shopuserprofile.gender = ShopUserProfile.FEMALE

    if vk_data['about']:
        user.shopuserprofile.about_me = vk_data['about']

    if vk_data['bdate']:
        b_date = datetime.strftime(vk_data['bdate'], '%d.%m.%Y').date()
        age = timezone.now().date().year - b_date.year
        if age < 100:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')
        user.age = age

    user.save()
