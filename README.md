# prefect-show

Some demo flow using http://prefect.io

## Getting started

* Require modern python 3
* Install prefect (see https://docs.prefect.io/core/getting_started/installation.html)

```shell
pip install prefect
```

* Run any demo flow

```shell
$ python demo/cron.me.py run

[2021-01-14 15:06:11+0000] INFO - prefect.FlowRunner | Beginning Flow run for 'cron.me_flow'
[2021-01-14 15:06:11+0000] INFO - prefect.TaskRunner | Task 'script_name': Starting task run...
[2021-01-14 15:06:11+0000] INFO - prefect.TaskRunner | Task 'script_name': Finished task run for task with final state: 'Success'
[2021-01-14 15:06:11+0000] INFO - prefect.TaskRunner | Task 'ShellTask': Starting task run...
[2021-01-14 15:06:14+0000] INFO - prefect.TaskRunner | Task 'ShellTask': Finished task run for task with final state: 'Success'
[2021-01-14 15:06:14+0000] INFO - prefect.FlowRunner | Flow run SUCCESS: all reference tasks succeeded
```


## Registering and scheduling


* Configure scheduling on a local server: 
```shell
# Cf. https://docs.prefect.io/orchestration/tutorial/overview.html#install-prefect
prefect backend server
prefect server start
```

* Or configure to another already running

```shell
$ prefect backend server
$ cat ~/.prefect/config.toml
[server]
host = "http://bench.ovh"
```

* Schedule any demo flow and go check the server ui

```shell
python cron.me.py register
Result check: OK
Flow URL: http://localhost:8080/default/flow/1d1eb53b-0820-4d9d-a477-f15a01c78c2e
 └── ID: bc0733e6-8467-45ac-8abe-c3bdb22b16b7
 └── Project: demo
 └── Labels: ['steph-laptop']
```