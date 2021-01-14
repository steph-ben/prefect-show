"""
A quick demo of three little shell tasks
"""
import sys
from pathlib import Path

import prefect
from prefect import Flow, task
from prefect.schedules import Schedule
from prefect.schedules.clocks import CronClock
from prefect.tasks.shell import ShellTask


shelltask = ShellTask()
with Flow("cron.me_flow") as flow:
    script_name = prefect.Parameter("script_name", default="date >> /tmp/cron.me; sleep 3")
    shelltask(command=script_name)


if __name__ == "__main__":
    cmd = "run"
    if len(sys.argv) > 1:
        cmd = sys.argv[1]

    if cmd == "run":
        flow.run()

    if cmd == "schedule":
        flow.schedule = Schedule(clocks=[CronClock("* * * * *")])
        flow.run()

    if cmd == "register":
        flow.schedule = Schedule(clocks=[CronClock("* * * * *")])
        r = flow.register(project_name="demo")
