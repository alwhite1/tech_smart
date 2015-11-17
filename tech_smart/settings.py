"""
Django settings for tech_smart project.

"""
# ~*~ coding: utf-8 ~*~

import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '^q^ttcr2znw8*-s5mwmzc(j#@rf^wk^&@y5sqc*il_+t07ota6'

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce',
    'stp',
    'to',
    'e2e',
    'tastypie',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tech_smart.urls'

WSGI_APPLICATION = 'tech_smart.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tech_smart',
        'USER': 'tech',
        'PASSWORD': 'askldh1D21498',
        'HOST': 'localhost',
    }
}

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "collected_static")
MEDIA_URL = '/media/'
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "/media/tiny_mce/"),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
)
ADMIN_MEDIA_PREFIX = 'usr/local/lib/python2.7/dist-packages/django/contrib/admin/static/admin/',
TINYMCE_JS_URL = STATIC_URL + "tiny_mce/tiny_mce.js"
TINYMCE_JS_ROOT = STATIC_URL + "/tiny_mce"
TINYMCE_SPELLCHECKER = False
TINYMCE_PLUGINS = [
    'safari',
    'table',
    'advlink',
    'advimage',
    'iespell',
    'inlinepopups',
    'media',
    'searchreplace',
    'contextmenu',
    'paste',
    'wordcount'
]
TINYMCE_DEFAULT_CONFIG={
    'theme' : "advanced",
    'plugins' : ",".join(TINYMCE_PLUGINS), # django-cms
    'language' : 'ru',
    "theme_advanced_buttons1" : "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,styleselect,formatselect,fontselect,fontsizeselect,|,spellchecker",
    "theme_advanced_buttons2" : "cut,copy,paste,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,image,cleanup,code,|,forecolor,backcolor,|,insertfile,insertimage",
    "theme_advanced_buttons3" : "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr",
    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_toolbar_align' : "left",
    'theme_advanced_statusbar_location' : "bottom",
    'theme_advanced_resizing' : True,
    'table_default_cellpadding': 2,
    'table_default_cellspacing': 2,
    'cleanup_on_startup' : False,
    'cleanup' : False,
    'paste_auto_cleanup_on_paste' : False,
    'paste_block_drop' : False,
    'paste_remove_spans' : False,
    'paste_strip_class_attributes' : False,
    'paste_retain_style_properties' : "",
    'forced_root_block' : False,
    'force_br_newlines' : False,
    'force_p_newlines' : False,
    'remove_linebreaks' : False,
    'convert_newlines_to_brs' : False,
    'inline_styles' : False,
    'relative_urls' : False,
    'formats' : {
        'alignleft' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-left'},
        'aligncenter' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-center'},
        'alignright' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-right'},
        'alignfull' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-justify'},
        'strikethrough' : {'inline' : 'del'},
        'italic' : {'inline' : 'em'},
        'bold' : {'inline' : 'strong'},
        'underline' : {'inline' : 'u'}
    },
    'pagebreak_separator' : "",
    # Drop lists for link/image/media/template dialogs
    'template_external_list_url': 'lists/template_list.js',
    'external_link_list_url': 'lists/link_list.js',
    'external_image_list_url': 'lists/image_list.js',
    'media_external_list_url': 'lists/media_list.js',
    #
    #'file_browser_callback':'tinyDjangoBrowser'
}
