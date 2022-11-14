from Utils import *


def test_download_for_windows():
    assert download_file('planoplan.exe') == 'planoplan.exe'


def test_download_for_mac():
    assert download_mac('PlanoplanEditorSetup.pkg') == 'PlanoplanEditorSetup.pkg'




