# prefect-show

Some demo flow using http://prefect.io

## Getting started

* Require modern python 3
* Install prefect (see https://docs.prefect.io/core/getting_started/installation.html)

```
pip install prefect
```

* Configure scheduling on a local server: 
```
# Cf. https://docs.prefect.io/orchestration/tutorial/overview.html#install-prefect
prefect backend server
prefect server start
```

* Or configure to another already running

```
$ prefect backend server
$ cat ~/.prefect/config.toml
[server]
host = "http://bench.ovh"
```


* Run any demo flow

```
python demo/cron.me.py run
```