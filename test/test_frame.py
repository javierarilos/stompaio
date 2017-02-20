from stompaio.client import Frame


def test_new_empty_frame():
    frame = Frame(command='CONNECT')
    assert frame.command == 'CONNECT'


def test_frame_from_str_command():
    frame = Frame.from_str('CONNECT\n')
    assert frame.command == 'CONNECT'


def test_frame_from_str_command():
    frame_str = 'CONNECT\nheader1:value1\nheader2:value2\nheader3:value3\n\n'

    frame = Frame.from_str(frame_str)

    assert frame.command == 'CONNECT'
    assert frame.header('header1') == 'value1'
    assert frame.header('header2') == 'value2'
    assert frame.header('header3') == 'value3'
