from django import forms
from django.db.models.base import Model
from django.forms import fields
from . import models
from datetime import date


class pfform(forms.ModelForm):
    class Meta:
        model = models.Dprofile
       # fields ='__all__'
        fields = ['firstname',
           'middlename',
           'lastname',
           'familyname',
           'Homeowner',
           'relationtoHomeowner',
           'fathername',
           'mothername',
           'dateofbirth',  
           'age',
           'gender',
           'education',
           'educationcertification',
           'educationislamic',
           'skill',
           'occupation',
           'pravasi',
           'area',
           'address',
           'contactno',
           'bloodgroup',
           'email',
           'martialstatus',
           'spousedetails',
           'spouseoccupation',
           'noofkids',
           'disablities',
           'previousmahallu',
           'covidvaccine',
           'otherdetails',
        #    'userid', 
        #    'lastmodifieduserid',
        #    'registrationdate',
        #    'lastmodifieddate',
           ]
        widget=  {
              'dateofbirth': forms.TextInput(attrs={'type': 'date'}),
            }
       
        labels = {
           'firstname': '📍✍🏻<br> <strong>What is your name ? </strong> <br> നിങ്ങളുടെ പേര് എന്ത് ?',
           'middlename': '<strong>Your Second Name </strong><br> നിങ്ങളുടെ രണ്ടാം പേര് ഉണ്ടെങ്കിൽ അത് നൽകുക ',
           'lastname': '<strong>Do you have Nickname ? </strong><br> നിങ്ങള്ക്ക് വിളിപ്പേരോ, നിങ്ങളെ അറിയപ്പെടുന്ന മറ്റു വല്ല പേരോ ഉണ്ടെങ്കിൽ അത് നൽകുക ',
           'familyname': '<strong>What is your Family Name | Surname </strong> <br> നിങ്ങളുടെ വീട്ടു പേര് തെരഞ്ഞെടുക്കുക. <br> <sup>നൽകിയ ലിസ്റ്റിൽ നിങ്ങളുടെ വീട്ടു പേര് ഇല്ല എങ്കിൽ ആദ്യം അത് ചേർക്കുക </sup>',
           'Homeowner':'📍✍🏻<br><strong>Home owner / Head of family ?</strong><br> കുടുംബനാഥയുടെ/കുടുംബനാഥന്റെ പേര്  ',
           'relationtoHomeowner':'📍✍🏻<br><strong>Relation to Home owner</strong><br>കുടുംബനാഥ/കുടുംബനാഥനുമായുള്ള ബന്ധം<br><sup>മകൻ, മകൾ, മരുമകൻ, മരുമകൾ, പേരമകൻ, പേരമകൾ Etc</sup>',
           'fathername': '📍✍🏻<br><strong>Who is your Father ?</strong><br> നിങ്ങളുടെ പിതാവിന്റെ പേര് നൽകുക ',
           'mothername': '📍✍🏻<br><strong>What is your Mother Name</strong> </br> നിങ്ങളുടെ മാതാവിന്റെ പേര് നൽകുക ',
           'dateofbirth': '📍✍🏻<br><strong>Date Of Birth</strong> </br>നിങ്ങളുടെ ജനന തിയതി',  
           'age': '<br><strong>How old are you ? </strong> </br>ഇപ്പോൾ നിങ്ങള്ക്ക് എത്ര വയസ് ആയി  ',
           'gender': '📍✍🏻<br><strong>What is your Gender</strong> </br> നിങ്ങൾ ആണോ / പെണ്ണോ ' ,
           'education': '<strong>Give your accademic education details</strong></br>നിങ്ങളുടെ വിദ്യാഭാസം</br><sup> നിങ്ങളുടെ ഉയർന്ന വിദ്യാഭ്യാസവും കൂടെ വിഭാഗവും നൽകുക</br> Eg: 10, +2, Degree Bcom, PG Sociology Etc  </sup>',
           'educationcertification':'<strong>Give your certification details</strong></br>സ്കൂൾ / കോളേജ് വിദ്യാഭ്യാസത്തിനു പുറമെ നിങ്ങൾ നേടിയിട്ടുള്ള സെർട്ടിഫൈഡ് കോഴ്സ്കൾ തുടങ്ങിയവയുടെ പൂർണ വിവരം ഓരോന്നും കോമയോ നമ്പറോ നൽകി വേർതിരിച്ചു നൽകുക  </br><sup>Eg: Diploma, NET, SET Etc  </sup>',
           'educationislamic': '<strong>Islamic Education</strong></br>നിങ്ങളുടെ മത വിദ്യാഭ്യാസത്തിന്റെ പൂർണ വിവരം നൽകുക </br><sup>ഓരോന്നും കോമായിട്ടു വേർതിരിച്ചു നല്കാൻ ശ്രമിക്കുക </sup>',
           'skill': '<strong>What kind of skills you have ?</strong> </br>നിങ്ങളുടെ നൈപുണ്യം എന്തൊക്കെ ?</br> <sup> ഏതൊക്കെ മേഖല കളിലാണ് നിങ്ങളുടെ നൈപുണ്യം വിനിയോഗിക്കുന്നത്  എല്ലാത്തിന്റെയും പൂർണ വിവരം നൽകുക </sup>',
           'occupation': '<strong>What is your occupation ?</strong> </br>നിങ്ങളുടെ ജോലി സംബദ്ധമായ മുഴുവൻ വിവരങ്ങളും നൽകുക',
           'pravasi': '<strong>If you are an expatriate now or in the past, please provide full details</strong> </br> നിങ്ങൾ ഇപ്പോൾ അല്ലങ്കിൽ മുമ്പ് പ്രവാസി ആണെങ്കിൽ അതിന്റെ പൂർണ വിവരങ്ങൾ നൽകുക </br> <sup>Eg:Saudi Arabia Riyad 1998-2015 Sales man in company name,</br> UAE Dubai 2008-2019 Driver in company name, </br>Oman Salala 2019-Still Etc</sup>',
           'area': '📍✍🏻<br><strong>Which area you are living in Irumbuchola Mahallu ?</strong></br>ഇരുമ്പു ചോല മഹല്ലിന്റെ ഏത് ഭാഗത്താണ് നിങ്ങൾ താമസിക്കുന്നത്</br><sup>നിങ്ങൾ താമസിക്കുന്ന ഏരിയ ഇതിൽ ഇല്ലങ്കിൽ ആദ്യം അത് ചേർക്കുക </sup>',
           'address': '<strong>Please give your full address</strong></br>നിങ്ങളുടെ പൂർണ വിലാസം നൽകുക',
           'contactno': '📍✍🏻<br><strong>Please provide your Contact No</strong></br>നിങ്ങളുടെ ഫോൺ നമ്പർ നൽകുക</br><sup> മൊബൈൽ നമ്പർ ഇല്ലാത്ത കുട്ടികൾ സ്ത്രീകൾ എന്നിവർ അവരുടെ രക്ഷിതാക്കളുടെ നമ്പർ നൽകുക </sup>',
           'bloodgroup': '<strong>Do you know your Blood Group ?</strong></br>നിങ്ങളുടെ രക്ത ഗ്രൂപ്പ് അറിയുമെങ്കിൽ അത് നൽകുക ',
           'email': '<strong>Please give your Email Address </strong></br>നിങ്ങളുടെ ഇമെയിൽ അഡ്രസ് നൽകുക ',
           'martialstatus': '📍✍🏻<br><strong>Martial Status</strong>',
           'spousedetails': '<strong>What is your spouse details if you are married ?</strong></br>നിങ്ങൾ വിവാഹിതനാണെങ്കിൽ നിങ്ങളുടെ ഇണയുടെ വിവരങ്ങൾ  നൽകുക</br><sup>വിവരങ്ങൾ യഥാക്രമം ഈ രീതിയിൽ നൽകുക </br> പേര്, ഉപ്പയുടെ വീട്ടു പേര് ഉപ്പയുടെ പേര്, ഉമ്മയുടെ വീട്ടു പേര് ഉമ്മയുടെ പേര്, സ്ഥലം മഹല്ലിന്റെ പേര്</sup> ',
           'spouseoccupation': '<strong>Spouse Occupation</strong>',
           'noofkids': '<strong>How many Kids You have ?</strong>',
           'disablities': '<strong>Do you have any disablities ?</strong> </br> നിങ്ങൾക് ഏതെങ്കിലും വിധത്തിലുള്ള   അംഗവൈകല്യം, പ്രധാന രോഗങ്ങൾ, സ്ഥിരമായ പ്രയാസങ്ങൾ എന്നിവ ഉണ്ടെങ്കിൽ അതിന്റെ വിവരങ്ങൾ നൽകുക ',
           'previousmahallu': '<strong>If you were in other mahallu then give previous Mahallu details. </strong></br>ഇരുമ്പുചോല മഹല്ലിലേക്കു നിങ്ങൾ താമസം മാറിയതാണെങ്കിൽ മുമ്പത്തെ മഹല്ലിന്റെ വിവരങ്ങൾ നൽകുക ',
           'covidvaccine': '<strong>Did you take covid-19 vaccine ? </strong><br/> നിങ്ങൾ കോവിഡ് വാക്‌സിൻ എടുത്തിട്ടുണ്ടെങ്കിൽ അതിന്റെ വിവരങ്ങൾ നൽകുക  ',
           'otherdetails': '<strong>Give Some other details about You.</strong></br>നിങ്ങളു മായി ബന്ധപ്പെട്ട മറ്റു വല്ല വിവരങ്ങളും നൽകുക',
        }
        
class areaform(forms.ModelForm):
    class Meta:
        model = models.Area
        fields ='__all__'

class familyform(forms.ModelForm):
    class Meta:
        model = models.Family
        fields ='__all__'