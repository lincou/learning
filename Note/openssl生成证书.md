- [openssl生成证书](#openssl生成证书)
  - [Windows下生成证书](#windows下生成证书)
    - [**生成CA私钥**](#生成ca私钥)
    - [**生成CA证书**](#生成ca证书)
    - [**生成ssl证书私钥**](#生成ssl证书私钥)
    - [**创建ssl证书私钥**](#创建ssl证书私钥)
    - [**生成结果**](#生成结果)
  - [**附检查证书有效期的命令**](#附检查证书有效期的命令)

# openssl生成证书

##  Windows下生成证书

 新建一个文件夹

 ### **生成CA私钥**
```
openssl genpkey -algorithm RSA -out myCA.key -pkeyopt rsa_keygen_bits:2048
```

 ### **生成CA证书**

 注意此处更新了个-days 3650，将ca证书有效期设置成1年，不加的话都是默认一个月
```
openssl req -new -x509 -sha384 -key myCA.key -out myCA.crt -days 365
```
生成如下：

```
[root@VM-4-15-centos ca]# openssl req -new -x509 -sha384 -key myCA.key -out myCA.crt
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
----
Country Name (2 letter code) [AU]:CN
State or Province Name (full name) [Some-State]:.
Locality Name (eg, city) []:.
Organization Name (eg, company) [Internet Widgits Pty Ltd]:.
Organizational Unit Name (eg, section) []:.
Common Name (e.g. server FQDN or YOUR name) []:pro.autojs.org
Email Address []:123456@qq.com
```
获取证书哈希值，
```
openssl x509 -subject_hash -in myCA.crt
```
生成如下：
```
[root@VM-4-15-centos ca]# openssl x509 -subject_hash -in myCA.crt
32a0c59b
-----BEGIN CERTIFICATE-----
MIID/zCCAuegAwIBAgIUHptUbjm8YgPGqUdfRUFfFeV1CIkwDQYJKoZIhvcNAQEM
BQAwgY4xCzAJBgNVBAYTAkNOMQ8wDQYDVQQIDAZGVUpJQU4xDzANBgNVBAcMBlBV
VElBTjERMA8GA1UECgwIV1VZQUtFSkkxEDAOBgNVBAsMB1hJQU5ZT1UxFzAVBgNV
BAMMDnByby5hdXRvanMub3JnMR8wHQYJKoZIhvcNAQkBFhA5NDIwMDE4NjBAcXEu
Y29tMB4XDTIzMDgxOTE0MTUzMFoXDTIzMDkxODE0MTUzMFowgY4xCzAJBgNVBAYT
AkNOMQ8wDQYDVQQIDAZGVUpJQU4xDzANBgNVBAcMBlBVVElBTjERMA8GA1UECgwI
V1VZQUtFSkkxEDAOBgNVBAsMB1hJQU5ZT1UxFzAVBgNVBAMMDnByby5hdXRvanMu
b3JnMR8wHQYJKoZIhvcNAQkBFhA5NDIwMDE4NjBAcXEuY29tMIIBIjANBgkqhkiG
9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwB/1EMfdNYTrmD0WlUK+PqDkezMj7iOABhLv
YEZ0RevCJ9XaBmS54JrklONljII4R3BjcZTb+gVzx6HmpsDm+9NN4xo2VpDXDMBx
dGxA9ZPuthRJsaOt9iHoV77Q9Z5JByj7qZS3ftkEfpd6N82IWDIwWSICd2/Akneb
Sk2IJnhB61aLvVpvvBKQKUBpSM753X85Msd8wWgZ5DI/DZEtBSRIyDr/PTK0mLS7
sOVUKLDan9G1H1UYK0zinVeJqPWc2IgvrhqlMgDutIQotzoY994zTejQ7Pp4mOVJ
iti2yY9DDVARYUjBbC8SiPSjX9TosEkgrfyQNruarkZs2uUJgQIDAQABo1MwUTAd
BgNVHQ4EFgQUFH6Iwyn8tqNR5mpn53VTta/WT+swHwYDVR0jBBgwFoAUFH6Iwyn8
tqNR5mpn53VTta/WT+swDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQwFAAOC
AQEAEXKGgsd0fvVCeVetCDJF9IUWVrvOEeYmjI1T4gHJcpDJKf6X1EPH91HMDNS0
p7rwj2hYHPrFfWL31VVyEk8WFcMs0i3hVLIk2+NcoRlHCnxzPwinqe8u91XDrh6w
qS6ywHj7vzR0fnRM92513WBfTmGEFsWKqVNr36MQ1wWP8iOSbMV55u/hG5Hxo6yn
fleMkY4L59PKMLURRNu8a5ek94vCcMhibIXUdjhsfsh9MfOTumovvzNnNBDsh/PN
WdTiXATuJSxvEtJiglnyKe/7jnIApclc7ofiMWmUXFHi8LABGt8pOPTgXyQR+ID3
dP8xfDFM2dx/j4H3OFuLRRLYGg==
-----END CERTIFICATE-----
```
生成的哈希值为32a0c59b，新建 32a0c59b.0，并将 myCA.crt 的内容复制进去

### **生成ssl证书私钥**
```
openssl genrsa -out localhost.key 2048
```
生成如下：
```
[root@VM-4-15-centos ca]# openssl genrsa -out localhost.key 2048
Generating RSA private key, 2048 bit long modulus
.................................................................+++
..........+++
e is 65537 (0x10001)
```

 ### **创建ssl证书私钥**
 ```
 openssl req -new -key localhost.key -out localhost.csr
 ```
 生成如下：
 ```
[root@VM-4-15-centos certs]# openssl req -new -key localhost.key -out localhost.csr
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:CN
State or Province Name (full name) [Some-State]:.
Locality Name (eg, city) []:.
Organization Name (eg, company) [Internet Widgits Pty Ltd]:.
Organizational Unit Name (eg, section) []:.
Common Name (e.g. server FQDN or YOUR name) []:pro.autojs.org
Email Address []:123456@qq.com
 
Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:autojs
An optional company name []:autojs
```
创建cert.ext,文件内容:
```
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names
 
[alt_names]
DNS.1 = pro.autojs.org
```
创建ssl证书CSR
```
openssl x509 -req -in localhost.csr -out localhost.crt -days 365 -CAcreateserial -CA myCA.crt -CAkey myCA.key -CAserial serial -extfile cert.ext
```
生成如下：
```
[root@VM-4-15-centos certs]# openssl x509 -req -in localhost.csr -out localhost.crt -days 3650 \
> -CAcreateserial -CA ../ca/myCA.crt -CAkey ../ca/myCA.key \
> -CAserial serial -extfile cert.ext
Signature ok
subject=C = CN, ST = ., L = ., O = ., OU = ., CN = pro.autojs.org, emailAddress = 123456@qq.com
Getting CA Private Key
```
使用CA验证一下证书是否通过
```
openssl verify -CAfile ../ca/myCA.crt localhost.crt
```
生成如下：
```
[root@VM-4-15-centos certs]#  openssl verify -CAfile ../ca/myCA.crt localhost.crt
localhost.crt: OK
```
### **生成结果**
--ca

----myCA.key

----myCA.crt

----32a0c59b.0

--certs

----localhost.key

----localhost.crt

----localhost.csr

----cert.ext

----serial

## **附检查证书有效期的命令**
两个crt文件都要检查（localhost.crt|myCA.crt）
```
openssl x509 -noout -dates -in crt文件路径
```