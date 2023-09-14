import datetime
import sqlite3
from sqlite3 import Error
from django.shortcuts import render
from setuptools.extern import names
from .models import Modalities, Studies
import random
from datetime import timedelta
import uuid
from functools import lru_cache


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """

    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)


def create_connection():
    connection = None
    try:
        connection = sqlite3.connect('/home/michoff/PycharmProjects/test_site/db.sqlite3')
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def init_db(request):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test_datatable_studies LIMIT 10000")
    patients = cursor.fetchall()
    dct = [{'id': patient[0],
            'full_name': patient[1],
            'birth_date': patient[2],
            'study_id': patient[3],
            'study_datetime': patient[4],
            'modality': patient[5]} for patient in patients]
    return render(request, 'test_datatable/init_db.html', {'patients': dct})
