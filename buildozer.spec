[app]
title = My Word
package.name = myword
package.domain = org.myword
source.dir = .
source.include_exts = py,kv,json,png,jpg,ttf
version = 1.0

# === THE NDK 27 COMPILATION FIX ===
# Upgrading to Kivy 2.3.1 fixes the GitHub wheel compilation crash
requirements = python3,kivy==2.3.1,kivymd==1.1.1,plyer,pillow,openssl

orientation = portrait
fullscreen = 0

# The 16KB memory alignment for modern processors
android.minapi = 26
android.api = 34
android.ndk = 27c
android.ndk_api = 26

android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True
android.enable_androidx = True

[buildozer]
log_level = 2
warn_on_root = 1

# Pull the bleeding-edge Android wrapper to support NDK 27
p4a.branch = develop
