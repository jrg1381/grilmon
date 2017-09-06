#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psutil
import subprocess
import os
from flask import Flask, jsonify
from flask import render_template


class ScheduledShutdown:
    def __init__(self):
        self.marker = "marker"
        self.shutdown_scheduled = False

    @property
    def shutdown_scheduled(self):
        return self.shutdown_scheduled

    @shutdown_scheduled.getter
    def shutdown_scheduled(self):
        return os.path.exists(self.marker)

    @shutdown_scheduled.setter
    def shutdown_scheduled(self, is_scheduled):
        if is_scheduled:
            with open(self.marker, 'w'):
                pass
        else:
            try:
                os.remove(self.marker)
            except OSError:
                print("Error")
                pass

app = Flask(__name__)
shutdown_pending = ScheduledShutdown()


def _process_list():
    return [[x.name(), x.pid, x.username()] for x in psutil.process_iter() if "chromium" in x.name()]


@app.route('/api/processes')
def processes():
    return jsonify(_process_list())


@app.route('/')
def main():
    return render_template('index.html')


def _run_process(arguments):
    p = subprocess.run(arguments,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
    return jsonify({"stdout": str(p.stdout, "utf8"),
                    "stderr": str(p.stderr, "utf8"),
                    "returnCode": p.returncode})


@app.route("/api/shutdown", methods=['POST'])
def shutdown():
    if shutdown_pending.shutdown_scheduled:
        shutdown_pending.shutdown_scheduled = False
        return _run_process(["shutdown", "-c"])
    else:
        shutdown_pending.shutdown_scheduled = True
        return _run_process(["shutdown", "-h", "+5"])


@app.route("/api/close-browser", methods=['POST'])
def close_browser():
    return _run_process(["killall", "chromium-browser"])


if __name__ == "__main__":
    main()
