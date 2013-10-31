from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from . import views


def redirect_doc(uri):
    return RedirectView.as_view(
        url='https://developer.mozilla.org/docs%s' % uri)

redirect_patterns = patterns('',
    url('^docs/firefox_os_guideline$',
        redirect_doc('/Web/Apps/Design'),
        name='ecosystem.ffos_guideline'),
    url('^docs/responsive_design$',
        redirect_doc('/Web_Development/Mobile/Responsive_design'),
        name='ecosystem.responsive_design'),
    url('^docs/patterns$',
        redirect_doc('/Web/Apps/Design/Responsive_Navigation_Patterns'),
        name='ecosystem.design_patterns'),
    url('^docs/review$',
        redirect_doc('/Web/Apps/Publishing/Marketplace_review_criteria'),
        name='ecosystem.publish_review'),
    url('^docs/hosted$',
        redirect_doc('/Web/Apps/Tutorials/General/Publishing_the_app'),
        name='ecosystem.publish_hosted'),
    url('^docs/submission$',
        redirect_doc('/Web/Apps/Publishing/Submitting_an_app'),
        name='ecosystem.publish_submit'),
    url('^docs/packaged$',
        redirect_doc('/Web/Apps/Developing/Packaged_apps'),
        name='ecosystem.publish_packaged'),
    url('^docs/intro_apps$',
        redirect_doc('/Web/Apps/Quickstart/Build/Intro_to_open_web_apps'),
        name='ecosystem.build_intro'),
    url('^docs/firefox_os$',
        redirect_doc('/Mozilla/Firefox_OS'),
        name='ecosystem.build_ffos'),
    url('^docs/manifests$',
        redirect_doc('/Web/Apps/FAQs/About_app_manifests'),
        name='ecosystem.build_manifests'),
    url('^docs/apps_offline$',
        redirect_doc('/Web/Apps/Offline_apps'),
        name='ecosystem.build_apps_offline'),
    url('^docs/game_apps$',
        redirect_doc('/Web/Apps/Developing/Games'),
        name='ecosystem.build_game_apps'),
    url('^docs/mobile_developers$',
        redirect_doc('/Web/Apps/Quickstart/Build/For_mobile_developers'),
        name='ecosystem.build_mobile_developers'),
    url('^docs/web_developers$',
        redirect_doc('/Web/Apps/Quickstart/Build/For_Web_developers'),
        name='ecosystem.build_web_developers'),
)

urlpatterns = redirect_patterns + patterns('',
    url('^$', views.landing, name='ecosystem.landing'),
    url('^partners$', views.partners, name='ecosystem.partners'),
    url('^support$', views.support, name='ecosystem.support'),
    url('^dev_phone$', views.dev_phone, name='ecosystem.dev_phone'),
    url('^docs/firefox_os_simulator$', views.firefox_os_simulator,
        name='ecosystem.firefox_os_simulator'),
    url('^docs/concept$', views.design_concept,
        name='ecosystem.design_concept'),
    url('^docs/fundamentals$', views.design_fundamentals,
        name='ecosystem.design_fundamentals'),
    url('^docs/ui_guidelines$', views.design_ui,
        name='ecosystem.design_ui'),
    url('^docs/deploy$', views.publish_deploy,
        name='ecosystem.publish_deploy'),
    url('^docs/quick_start$', views.build_quick,
        name='ecosystem.build_quick'),
    url('^docs/payments/status$', views.publish_payments,
        name='ecosystem.publish_payments'),
    url('^docs/badges$', views.publish_badges,
        name='ecosystem.publish_badges'),
    url('^docs/reference_apps$', views.build_reference,
        name='ecosystem.build_reference'),
    url('^docs/tools$', views.build_tools,
        name='ecosystem.build_tools'),
    url('^docs/app_generator$', views.build_app_generator,
        name='ecosystem.build_app_generator'),
    url('^docs/dev_tools$', views.build_dev_tools,
        name='ecosystem.build_dev_tools'),
    url('^docs/payments$', views.build_payments,
        name='ecosystem.build_payments'),

    url('^docs/apps/(?P<page>\w+)?$', views.apps_documentation,
        name='ecosystem.apps_documentation'),
)
