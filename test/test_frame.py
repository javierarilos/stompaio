from stompaio.client import Frame


def test_new_empty_frame():
    frame = Frame(command='CONNECT')
    assert frame.command == 'CONNECT'


def test_frame_from_str():
    frame = Frame.from_str('CONNECT\n')
    assert frame.command == 'CONNECT'
