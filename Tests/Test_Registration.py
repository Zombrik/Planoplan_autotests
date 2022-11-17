from Utils import *


def test_registration():
    del_email()
    assert registration() == 'trial'


def test_registration_google():
    assert registration_google() == "obuchenie"


def test_registration_vk():
    assert registration_vk() == "obuchenie"


def test_koda_podtverjdenia():
    assert kod_podtverjdenia() == 'Letter inbox'