[app]

# App name (makikita sa phone)
title = PGame

# Package name (DAPAT UNIQUE)
package.name = pgame
package.domain = org.raal.pgame

# Folder ng main.py
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,ttf

# Main file
entrypoint = main.py

# App version
version = 1.0

# Screen settings
fullscreen = 1
orientation = portrait

# Permissions (safe default)
android.permissions = INTERNET

# Android settings
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# ⭐ PYGAME REQUIREMENTS (IMPORTANT)
requirements = python3,pygame,sdl2,sdl2_image,sdl2_mixer,sdl2_ttf

# Architecture
android.archs = arm64-v8a,armeabi-v7a

# Logcat (para madaling mag-debug)
log_level = 2


[buildozer]

# Buildozer folder
log_level = 2
warn_on_root = 1
