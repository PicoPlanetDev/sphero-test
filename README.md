# sphero-test

A collection of scripts to test and demo capabilities of Sphero BOLT. Might be used as a teaching tool.

spherov2 docs: [https://spherov2.readthedocs.io](https://spherov2.readthedocs.io)

## Usage

```
cd sphero-test
python -m venv venv # optional
source venv/bin/activate # optional
pip install -r requirements.txt
cd src
python3 helloworld.py
```

## Running a server

From the spherov2 docs, run the following command to start a server that non-BLE enabled clients could connect to over WiFi to control nearby spheros:

`python -m spherov2.adapter.tcp_server`

If you'd like, you can add a host address and port to the above command. The default is `0.0.0.0` on port `50004`:

`python -m spherov2.adapter.tcp_server HOST PORT`
