#!/usr/bin/python

import whois

target = "google.com.br"

querywhois = whois.query(target)

print(querywhois.name)
print(querywhois.creation_date)
print(querywhois.expiration_date)
print(querywhois.last_updated)
print(querywhois.registrar)


