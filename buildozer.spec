[app]
title = My Word
package.name = myword
package.domain = org.myword
source.dir = .
source.include_exts = py,kv,json,png,jpg,ttf
version = 1.0

# Added openssl back for native secure HTTPS dictionary lookups
# Bumped Kivy to 2.3.0 which is the most stable for modern Android
requirements = python3,kivy==2.3.0,kivymd==1.1.1,plyer,pillow,openssl

orientation = portrait
fullscreen = 0

# === THE CRITICAL FIX ===
# Downgrading to 33 bypasses Android 14's fatal pthread_mutex_lock crash
android.minapi = 24
android.api = 33
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
