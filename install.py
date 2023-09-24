#!/usr/bin/env python3
import os
import shutil
import subprocess

def is_root():
    return os.geteuid() == 0

def log_progress(m):
    print(f'⟳ {m}…')

def log_success(m):
    print(f'✅ {m}')

def log_exception(e):
    print(f'❌ {str(e)}')
    raise e

def assert_dir(some_dir, message = ''):
    if len(message) > 0:
        m = message + '; '
    if not os.path.exists(some_dir):
        log_exception(Exception(f'path does not exist: {some_dir}; {m}exiting'))
    if not os.path.isdir(some_dir):
        log_exception(f'path is not directory: {some_dir}; {m}exiting')
    log_success(f'directory exists: {some_dir}')

def copy_files_under_dir(src_dir, dest_dir):
    dirpath = os.path.normpath(os.path.join(os.getcwd(), src_dir))
    files = os.listdir(dirpath)
    for f in files:
        src = os.path.join(dirpath, f)
        try:
            shutil.copy(src, dest_dir)
        except:
            log_exception(Exception(f'failed to copy file; src: {src}; dest_dir: {dest_dir}'))
        log_success(f'copied file; src: {src}; dest_dir: {dest_dir}')

def reload_systemd_daemon():
    log_progress('reloading systemd daemon')
    subprocess.run(["systemctl", "daemon-reload"])

if __name__ == '__main__':
    if not is_root():
         log_exception(Exception('this script must be run as root'))
    log_progress('started installer…')    
    assert_dir('/usr/local/sbin')
    assert_dir('/usr/local/bin')
    assert_dir('/etc/systemd', 'does your system support systemd?')
    assert_dir('/etc/systemd/system', 'does your system support systemd?')
    assert_dir('/etc/systemd/user', 'does your system support systemd?')
    copy_files_under_dir('./usr/local/sbin/', '/usr/local/sbin/')
    copy_files_under_dir('./usr/local/bin/', '/usr/local/bin/')
    copy_files_under_dir('./etc/systemd/system/', '/etc/systemd/system/')
    copy_files_under_dir('./etc/systemd/user/', '/etc/systemd/user/')
    reload_systemd_daemon()
    print('done.')

