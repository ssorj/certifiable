
- https://help.ubuntu.com/community/GnuTLS
- https://ubuntu.com/server/docs/security-certificates
- https://serverfault.com/questions/649990/non-interactive-creation-of-ssl-certificate-requests/650008
- https://devcenter.heroku.com/articles/ssl-certificate-self
- http://www.gerv.net/security/self-signed-certs/

A certificate contains a public key, plus other information

hypercorn main:star --certfile service.cert --keyfile service.key --debug

- https://superuser.com/questions/1451895/err-ssl-key-usage-incompatible-solution
