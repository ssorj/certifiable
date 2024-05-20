# Certifiable

- https://help.ubuntu.com/community/GnuTLS
- https://ubuntu.com/server/docs/security-certificates
- https://serverfault.com/questions/649990/non-interactive-creation-of-ssl-certificate-requests/650008
- https://devcenter.heroku.com/articles/ssl-certificate-self
- http://www.gerv.net/security/self-signed-certs/
- https://en.wikipedia.org/wiki/Public_key_certificate

- A certificate contains a public key, plus other information

hypercorn main:star --certfile service.cert --keyfile service.key --debug

- https://superuser.com/questions/1451895/err-ssl-key-usage-incompatible-solution

openssl s_client -connect localhost:5672

https://stackoverflow.com/questions/19726138/openssl-error-18-at-0-depth-lookupself-signed-certificate

https://issues.apache.org/jira/browse/PROTON-2397

https://serverfault.com/questions/747525/what-does-verify-return1-mean-in-the-openssl-output

dnf install openssl gnutls-utils

- https://stackoverflow.com/questions/4024393/difference-between-self-signed-ca-and-self-signed-certificate
- A trust anchor does not have to be a CA certificate.  Any certificate can be be explicitly trusted.
- https://www.openssl.org/docs/man3.0/man1/openssl-verification-options.html

To look at

- https://github.com/FiloSottile/mkcert
- https://news.ycombinator.com/item?id=33383095

Todo

- Use explicit host and port with the s_client and s_server commands, so they work better as examples.
