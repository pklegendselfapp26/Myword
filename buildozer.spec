[app]
title = My Word
package.name = myword
package.domain = org.myword
source.dir = .
source.include_exts = py,kv,json,png,jpg,ttf
version = 1.0

# Removed 'openssl'. Python3 builds it automatically now.
# Explicitly listing it forces an old recipe that crashes NDK 28!
requirements = python3,kivy==2.3.1,kivymd==1.1.1,plyer,pillow

orientation = portrait
fullscreen = 0

# === THE ULTIMATE ANDROID 16 MEMORY FIX ===
android.minapi = 24
android.api = 35
android.ndk = 28c
android.ndk_api = 24

# This flag forces the C-compiler to perfectly align to Realme's 16KB processor
android.extra_ldflags = -Wl,-z,max-page-size=16384

android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True
android.enable_androidx = True

[buildozer]
log_level = 2
warn_on_root = 1

# Uses the master wrapper to support NDK 28c
p4a.branch = develop
