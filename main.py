import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

number = input("Digite o numero de celular no formato completo (codigo do pais e regional): ")

ch_number = phonenumbers.parse(number, "CH")

print(number)

print(geocoder.description_for_number(ch_number, "pt"))

service_number = phonenumbers.parse(number, "RO")

print(carrier.name_for_number(service_number, "pt"))