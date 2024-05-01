import whois

res = whois.whois('harisudhan.me')
print("Overal Inforamtion = ",res)

domain_name = res.domain_name
regisetrar = res.registrar
updated_date = res.updated_date
creation_date = res.creation_date
expiration_date = res.expiration_date
name_servers = res.name_servers
status = res.status
organization = res.org
country = res.country
dnssec = res.dnssec
email = res.emails


