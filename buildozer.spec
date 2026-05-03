[app]
title = My Word
package.name = myword
package.domain = org.myword
source.dir = .
source.include_exts = py,kv,json,png,jpg,ttf
version = 1.0

# Kivy 2.3.0 and NDK 25b is the golden combination for compiling Pillow
requirements = python3,kivy==2.3.0,kivymd==1.1.1,plyer,pillow,openssl

orientation = portrait
fullscreen = 0

# === WE MUST USE NDK 25b TO PREVENT THE 8-MINUTE CRASH ===
android.minapi = 24
android.api = 34
android.ndk = 25b
android.ndk_api = 24

android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True
android.enable_androidx = True

[buildozer]
log_level = 2
warn_on_root = 1
