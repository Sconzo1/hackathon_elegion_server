from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'countries', CountryView)
# router.register(r'companies', CompanyView)
# router.register(r'agreements', AgreementView)
# router.register(r'representatives', RepresentativeView)
# router.register(r'agreement_types', AgreementTypeView)

urlpatterns = router.urls
