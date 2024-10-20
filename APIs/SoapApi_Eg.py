import requests
import xml.etree.ElementTree as ET
#http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso


url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

countrycode = "IN"
payload = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <FullCountryInfo xmlns="http://www.oorsprong.org/websamples.countryinfo">
      <sCountryISOCode>{countrycode}</sCountryISOCode>
    </FullCountryInfo>
  </soap:Body>
</soap:Envelope>"""
header = {
"Content-Type": "text/xml; charset=utf-8"
}

response = requests.request("POST",url=url,headers=header, data=payload)
print(response.status_code)
print(response.text)

'''
200
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <m:FullCountryInfoResponse xmlns:m="http://www.oorsprong.org/websamples.countryinfo">
      <m:FullCountryInfoResult>
        <m:sISOCode>IN</m:sISOCode>
        <m:sName>India</m:sName>
        <m:sCapitalCity>New Delhi</m:sCapitalCity>
        <m:sPhoneCode>91</m:sPhoneCode>
        <m:sContinentCode>AS</m:sContinentCode>
        <m:sCurrencyISOCode>INR</m:sCurrencyISOCode>
        <m:sCountryFlag>http://www.oorsprong.org/WebSamples.CountryInfo/Flags/India.jpg</m:sCountryFlag>
        <m:Languages>
          <m:tLanguage>
            <m:sISOCode>hin</m:sISOCode>
            <m:sName>Hindi</m:sName>
          </m:tLanguage>
        </m:Languages>
      </m:FullCountryInfoResult>
    </m:FullCountryInfoResponse>
  </soap:Body>
</soap:Envelope>



'''


root = ET.fromstring(response.content)
namespace = {'m':'http://www.oorsprong.org/websamples.countryinfo'}

# langcode = root.find(".//m:sISOCode",namespace).text
# print(langcode)

country = root.find(".//m:sName",namespace).text
print(country)


languages = root.findall(".//m:Languages",namespace)
print(languages)
for lang in languages:
    langcode = lang.find(".//m:sISOCode", namespace).text
    langname = lang.find(".//m:sName", namespace).text
    print(langcode)
    print(langname)

