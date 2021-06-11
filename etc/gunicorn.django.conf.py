"""
gunicorn Django config file

"""
import multiprocessing
# from pathlib import Path

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1

# pythonpath = Path(__file__).absolute().parent.parent / 'ask'
