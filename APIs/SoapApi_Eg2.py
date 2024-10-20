import requests
import xml.etree.ElementTree as ET

#http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso


url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

countrycode = "US"
payload = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
      <sCountryISOCode>{countrycode}</sCountryISOCode>
    </CapitalCity>
  </soap:Body>
</soap:Envelope>"""
header = {
"Content-Type": "text/xml; charset=utf-8"
}

response = requests.request("POST",url=url,headers=header, data=payload)
print(response.status_code)
print(response.text)

root = ET.fromstring(response.content)
namespace = {'m':'http://www.oorsprong.org/websamples.countryinfo'}

#<m:CapitalCityResult>Washington</m:CapitalCityResult>
captialcity = root.find(".//m:CapitalCityResult",namespace).text
print(captialcity)