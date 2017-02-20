from stompaio.client import Frame


def test_new_empty_frame():
    frame = Frame(command='CONNECT')
    assert frame.command == 'CONNECT'
