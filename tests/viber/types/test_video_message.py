from botapi.viber.types import VideoMessage


def test_video_message_serialize():
    obj = VideoMessage(
        media='http://www.images.com/video.mp4',
        size=10000,
        duration=10,
        thumbnail='http://www.images.com/thumb.jpg',
        tracking_data='tracking data'
    )
    expected = {
        'type': 'video',
        'min_api_version': 1,
        'media': 'http://www.images.com/video.mp4',
        'size': 10000,
        'thumbnail': 'http://www.images.com/thumb.jpg',
        'duration': 10,
        'tracking_data': 'tracking data'
    }
    assert obj.serialize(add_min_api_ver=True) == expected
