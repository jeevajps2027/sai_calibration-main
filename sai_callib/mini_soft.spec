# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files, collect_submodules
import os

# Environment variables
os.environ["DJANGO_SETTINGS_MODULE"] = "sai_calibrations.settings"

# Collect 'channels' submodules
hiddenimports = collect_submodules('channels')

block_cipher = None

a = Analysis(
    ['manage.py'],
    pathex=['C:/Users/jeeva/OneDrive/Desktop/sai_calibration/sai_callib'],
    binaries=[],
    
    datas=[
        ('app/templates/app', 'app/templates/app'),
        ('app/static', 'app/static'),
        ('app/views', 'app/views'),
        ('app/migrations', 'app/migrations'),
        ('sai_calibrations/asgi.py', 'sai_calibrations/asgi.py'),  # Include ASGI file
        ('sai_calibrations/settings.py', 'sai_calibrations/settings.py'),  # Include settings
    ],

    hiddenimports=[
        *hiddenimports,  # Unpack the collected submodules
        'whitenoise.middleware',
        'serial.tools.list_ports',
        'pyserial',
        'serial',
        'kaleido',
        'whitenoise',
        'channels_redis.core',
        'channels_redis',
        'redis',
        'django.core.asgi',
        'django.core.wsgi',  # Add this for WSGI fallback
        'sai_calibrations.asgi',    # Explicitly include ASGI module
    ],

    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='sai_calibration',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    icon='C:\\Users\\jeeva\\OneDrive\\Desktop\\four_channel\\four_channel\\app\\static\\images\\Gauge.ico',

    
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,  # Disable UPX compression
    upx_exclude=[],
    name='sai_calibration'
)
