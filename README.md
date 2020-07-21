# cidrsubnet
Implementation of the cidrsubnet function used by terraform. 
Explanation follows here - https://www.terraform.io/docs/configuration/functions/cidrsubnet.html

### Installation

If a cli tool is required:

```bash
wget https://raw.githubusercontent.com/DannyLee12/cidrsubnet/master/cidrsubnet.py
chmod +x cidrsubnet.py
mv cidrsubnet.py /usr/local/bin/cidrsubnet
```

### Usage

```bash
cidrsubnet prefix newbits netnum

> cidrsubnet "172.16.0.0/12" 4 2
172.18.0.0/16
> cidrsubnet "10.1.2.0/24"  4 15
10.1.2.240/28
```
