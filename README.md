# http-benckmark

An open source load testing tool.

Define user behaviour with Python code, and swarm your system with millions of simultaneous users.

Based on http://locust.io

```console
$ git clone https://github.com/tiagorkrebs/http-benchmark.git
$ cd http-benchmark
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ ./run.sh
```

Go to http://localhost:8089

If you need a different behaviour make your own `locusfile.py`.
