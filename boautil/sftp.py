
import paramiko

import os
import socket
import sys
import traceback
import base64
import getpass


__author__ = 'joeny'


def load_key(key_path, hostname):
    """
    Load key

    :param key_path: key path
    :param hostname: hostname
    :return:
    """
    hostkeys = paramiko.util.load_host_keys(os.path.expanduser(key_path))

    try:

        if hostname in hostkeys:
            hostkey_type = hostkeys[hostname].keys()[0]
            hostkey = hostkeys[hostname][hostkey_type]

            return hostkey, hostkey_type
    except Exception as e:
        print(e)

        return None, None


def get_transport(hostname, port, username, password, hostkey):
    """
    Connect and use paramiko Transport to negotiate SSH2 across the connection

    :param hostname:
    :param port:
    :param username:
    :param password:
    :param hostkey:
    :return:
    """

    try:
        t = paramiko.Transport((hostname, port))
        t.connect(hostkey,
                  username,
                  password,
                  gss_host=socket.getfqdn(hostname))

        sftp = paramiko.SFTPClient.from_transport(t)

        # dirlist on remote host
        # dirlist = sftp.listdir('.')
        # print("Dirlist: %s" % dirlist)

    except Exception as e:
        print('*** Caught exception: %s: %s' % (e.__class__, e))
        traceback.print_exc()

        try:
            t.close()
        except IOError as e:
            pass
        sys.exit(1)

        return None

    return sftp, t


def walk_sftp(sftp, path):
    """
    Walk through the sftp

    :param sftp:
    :param path:
    :return:
    """
    data = dict(directory=path, files=[], folders=[])

    for item in sftp.listdir(path=path):
        filepath = os.path.join(path + '/', item)

        lstatout = str(sftp.lstat(filepath)).split()[0]

        if 'd' in lstatout:
            data['folders'].append(walk_sftp(sftp, filepath))
        else:
            data['files'].append(filepath)

    return data


def copy_directory(sftp, remote_keys, source_path):
    """
    Copy directory

    :param sftp:
    :param remote_keys:
    :param source_path:
    :return:
    """
    remote_path = remote_keys['directory']
    remote_dir_name = os.path.split(remote_path)[1]

    source_dir_path = os.path.join(source_path, remote_dir_name)

    if not os.path.isdir(source_dir_path):
        os.mkdir(source_dir_path)

    for fname in remote_keys['files']:
        base_filename = os.path.split(fname)[1]

        sftp.get(fname, os.path.join(source_dir_path, base_filename))

    for fdir in remote_keys['folders']:
        copy_directory(sftp, fdir, source_dir_path)


def copy_folder(sftp, remote_keys, source_path):
    """
    Copy folder

    :param sftp:
    :param remote_keys:
    :param source_path:
    :return:
    """
    remote_path = remote_keys['directory']
    remote_dir_name = os.path.split(remote_path)[1]

    # source_dir_path = os.path.join(source_path, remote_dir_name)
    source_dir_path = source_path

    for fname in remote_keys['files']:
        base_filename = os.path.split(fname)[1]

        sftp.get(fname, os.path.join(source_dir_path, base_filename))

    for fdir in remote_keys['folders']:
        copy_directory(sftp, fdir, source_dir_path)
