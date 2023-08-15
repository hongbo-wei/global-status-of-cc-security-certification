from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from cc_statistic.models import ItSecChina as Isc
from cc_statistic.models import CommonCriteria as Cc
from cc_statistic.models import Niap as Ni
from cc_statistic.models import CcStatisticSpain as Sp
from cc_statistic.models import CertifiedProducts as CP


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the CC Statistic index")


def visual(request):

    # fetch all rows in Test database model
    data_list = Isc.objects.all()

    # total count from all databases
    # total_count = Cc.objects.count() + Isc.objects.count() + Ni.objects.count() + Sp.objects.count()
    total_count = CP.objects.count()

    # count the certification issued in specific year
    isc_2022 = Isc.objects.filter(issue_date__startswith='2022').count()
    isc_2021 = Isc.objects.filter(issue_date__startswith='2021').count()
    isc_2020 = Isc.objects.filter(issue_date__startswith='2020').count()
    isc_2019 = Isc.objects.filter(issue_date__startswith='2019').count()
    isc_2018 = Isc.objects.filter(issue_date__startswith='2018').count()
    isc_2017 = Isc.objects.filter(issue_date__startswith='2017').count()

    # count the certification according to its issue year
    cc_2022 = Cc.objects.filter(certification_date__contains='2022').count()
    cc_2021 = Cc.objects.filter(certification_date__contains='2021').count()
    cc_2020 = Cc.objects.filter(certification_date__contains='2020').count()
    cc_2019 = Cc.objects.filter(certification_date__contains='2019').count()
    cc_2018 = Cc.objects.filter(certification_date__contains='2018').count()
    cc_2017 = Cc.objects.filter(certification_date__contains='2017').count()

    # count the specific certification level
    eal_1 = Isc.objects.filter(level__startswith='EAL1').count()
    eal_2 = Isc.objects.filter(level__startswith='EAL2').count()
    eal_3 = Isc.objects.filter(level__startswith='EAL3').count()
    eal_4 = Isc.objects.filter(level__startswith='EAL4').count()
    eal_self = Isc.objects.filter(level__startswith='自主').count()

    # count schema from official Common Criteria website
    fr = Cc.objects.filter(scheme__startswith='FR').count()
    nl = Cc.objects.filter(scheme__startswith='NL').count()
    jp = Cc.objects.filter(scheme__startswith='JP').count()
    de = Cc.objects.filter(scheme__startswith='DE').count()
    us = Cc.objects.filter(scheme__startswith='US').count()
    ca = Cc.objects.filter(scheme__startswith='CA').count()

    # count assurance_level per country: i.e. EAL4 FR18
    pp = Isc.objects.filter(level__contains='').count()

    # Top 10 Laboratories

    # PP with product category, i.e. Protection Profile for Network Devices

    # PP and cPP: Collaborative PPs vs Non-Collaborative PPs, certifications using CPPs

    # Top 5 manufactures in China - middle right
    top_5 = Isc.objects.values('company').annotate(count=Count('*')).order_by('-count')[:5]

    # Top product categories - pie chart

    # Higher EAL manufactures: manufacturers and categories that obtained EAL6

    # Products uploaded to CC Portal vs products only in CB websites

    # return values so that front end (html) can use them.

    context = {'data_list': data_list,
               'top_5': top_5,
               'isc_2022': isc_2022,
               'isc_2021': isc_2021,
               'isc_2020': isc_2020,
               'isc_2019': isc_2019,
               'isc_2018': isc_2018,
               'isc_2017': isc_2017,
               'cc_2022': cc_2022,
               'cc_2021': cc_2021,
               'cc_2020': cc_2020,
               'cc_2019': cc_2019,
               'cc_2018': cc_2018,
               'cc_2017': cc_2017,
               'eal_1': eal_1,
               'eal_2': eal_2,
               'eal_3': eal_3,
               'eal_4': eal_4,
               'eal_self': eal_self,
               'fr': fr,
               'nl': nl,
               'jp': jp,
               'de': de,
               'us': us,
               'ca': ca,
               'total': total_count,
              }
    return render(request, 'cc_statistic/index.html', context)

