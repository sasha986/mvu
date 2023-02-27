import hashlib
import os
from functools import partial

from django.conf import settings

def hash_file(file, block_size=65536):
    hasher = hashlib.sha1()
    for buf in iter(partial(file.read, block_size), b''):
        hasher.update(buf)

    return hasher.hexdigest()


def hash_video_filename(instance, filename):
    """
    :type instance: dolphin.models.File
    """
    instance.video.open()
    filename_base, filename_ext = os.path.splitext(filename)

    return settings.VIDEO_RELATIVE_PATH + "{0}.{1}".format(hash_file(instance.video), filename_ext)

def hash_thumbnail_filename(instance, filename):
    """
    :type instance: dolphin.models.File
    """
    instance.thumbnail.open()
    filename_base, filename_ext = os.path.splitext(filename)

    return settings.THUMBNAIL_RELATIVE_PATH + "{0}.{1}".format(hash_file(instance.thumbnail), filename_ext)