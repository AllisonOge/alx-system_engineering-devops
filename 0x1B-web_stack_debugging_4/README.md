web stack debugging 4

Challenge: How well is the Nginx web server setup under stress (Turns out it is bad due to failed requests count benchmarked by ApacheBench). Fix the Nginx server so that there are 0 failed request.

```
root@b5e791809f59:~# ab -c 100 -n 2000 localhost/
This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 200 requests
Completed 400 requests
Completed 600 requests
Completed 800 requests
Completed 1000 requests
Completed 1200 requests
Completed 1400 requests
Completed 1600 requests
Completed 1800 requests
Completed 2000 requests
Finished 2000 requests


Server Software:        nginx/1.4.6
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        201 bytes

Concurrency Level:      100
Time taken for tests:   2.887 seconds
Complete requests:      2000
Failed requests:        701
   (Connect: 0, Receive: 0, Length: 701, Exceptions: 0)
Non-2xx responses:      1299
Total transferred:      1079882 bytes
HTML transferred:       690111 bytes
Requests per second:    692.72 [#/sec] (mean)
Time per request:       144.358 [ms] (mean)
Time per request:       1.444 [ms] (mean, across all concurrent requests)
Transfer rate:          365.26 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.3      0       2
Processing:     1  140  50.1    103     296
Waiting:        1  140  49.9    103     296
Total:          3  140  49.9    103     296

Percentage of the requests served within a certain time (ms)
  50%    103
  66%    196
  75%    197
  80%    198
  90%    198
  95%    199
  98%    199
  99%    207
 100%    296 (longest request)
root@b5e791809f59:~#
```

Report shows 701 failed request when the server is stressed with 2000 requests at a rate of 100 request per time.

Requirements:
- Automate the solution with Puppet v3.4
- Files must pass puppet-lint version 2.1.1 without errors
- All files will be interpreted on Ubuntu 14.04 LTS

Hint:
- visit the log files

---

Install puppet-lint with the following commands
```
apt-get install -y ruby
gem install puppet-lint -v 2.1.1
```

---

Debugging

Output of /etc/log/nginx/error.log shows the following output, which suggest that the webserver is hitting the limit of how many file descriptors it's allowed to open
```
2024/04/18 18:40:27 [crit] 32#0: *3999 open() "/usr/share/nginx/html/index.html" failed (24: Too many open files), client: 127.0.0.1, server: localhost, request: "GET / HTTP/1.0", host: "localhost"
2024/04/18 18:40:27 [crit] 32#0: accept4() failed (24: Too many open files)
```

Next steps
- check the current limits on open files with command `ulimit`: `ulimit -n` for current session
- increase the file descriptor limits
