[app]
title = My Word
package.name = myword
package.domain = org.myword
source.dir = .
source.include_exts = py,kv,json,png,jpg,ttf
version = 1.0

# Simplified requirements so p4a doesn't trip over itself
requirements = python3,kivy==2.3.0,kivymd==1.1.1,requests,openssl,plyer,pillow

orientation = portrait
fullscreen = 0

android.minapi = 26
android.api = 34
android.ndk = 25b
android.sdk = 34
android.ndk_api = 26

android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
