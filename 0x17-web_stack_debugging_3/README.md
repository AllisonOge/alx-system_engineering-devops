web stack debugging 3 readme

Challenge: Debug a Wordpress website running on a LAMP (Linux, Apache, MySQL, and PHP) stack. Find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of bash).

```bash
root@f2081466fca1:/# curl -Is 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 12 Apr 2024 20:57:09 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html

root@f2081466fca1:/#
```

Requirements:
- Automate the solution using Puppet v3.4
- Files must pass puppet-lint version 2.1.1 without errors
- All files will be interpreted on Ubuntu 14.04 LTS

Hint:
-  `strace` can attach to a current running process
- You can use `tmux` to run `strace` in one window and `curl` in another one

----
Install puppet-lint with the following commands
```bash
apt-get install -y ruby
gem install puppet-lint -v 2.1.1
```
