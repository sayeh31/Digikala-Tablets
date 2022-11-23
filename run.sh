#!/bin/bash

exec python3 tabel_initial.py &
exec python3 runserver.py &
exec python3 startup.py