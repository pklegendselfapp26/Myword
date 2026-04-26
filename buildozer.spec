[app]
title = My Word
package.name = myword
package.domain = org.myword
source.dir = .
source.include_exts = py,kv,json,png,jpg,ttf
version = 1.0

requirements = python3,kivy==2.2.1,kivymd==1.1.1,plyer,pillow

orientation = portrait
fullscreen = 0

# Lowering NDK API prevents triggering Android 14's strict C-level memory guards
android.minapi = 24
android.api = 34
android.ndk = 25b
android.ndk_api = 24

android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True

# Required to prevent instant crashes on Android 14 when asking for permissions
android.enable_androidx = True

[buildozer]
log_level = 2
warn_on_root = 1

# === THE SILVER BULLET ===
# Forces Buildozer to use the bleeding-edge Android wrapper containing the SDL2 patches
p4a.branch = develop
