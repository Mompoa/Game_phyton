[app]

# (str) Title of your application
title = Flappy YOLL

# (str) Package name
package.name = flappyyoll

# (str) Package domain (needed for android/ios packaging)
package.domain = org.yoll.game

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,wav,ogg

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3==3.10.12,pygame==2.5.2,cython==0.29.36

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
#p4a.source_dir = /home/user/src/python-for-android
#p4a.checkout_dir = /home/user/src/python-for-android

# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2   # <-- Mahalaga 'to para sa Pygame!
p4a.bootstrap = sdl2

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android API to use
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
# android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements.
#android.accept_sdk_license = False

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that extends PythonActivity
#android.activity_class_name = org.kivy.android.PythonActivity

# (str) Extra xml to write directly inside the <manifest> element of AndroidManifest.xml
# use that parameter to provide a filename from where to load your custom XML code
#android.extra_manifest_xml =

# (str) Extra string to write directly inside the <manifest> tag of AndroidManifest.xml
# use that parameter to provide your XML as string
#android.extra_manifest_xml_string =

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Android logcat only display log for activity's pid
#android.logcat_pid_only = False

# (str) Android additional adb arguments
#android.adb_args = -H host.docker.internal

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (int) overrides automatic versionCode computation (used in build.gradle)
# this is not the same as app version and should only be edited if you know what you're doing
# android.numeric_version = 1

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) XML file for custom backup rules (see official auto backup documentation)
# android.backup_rules =

# (str) If you need to insert variables into your AndroidManifest.xml file,
# you can do so with the manifestPlaceholders property.
# This property takes a map of key-value pairs. (via string)
# Usage example : android.manifest_placeholders = [myCustomUrl:\"org.kivy.customurl\"]
# android.manifest_placeholders = [:]

# (bool) enables AndroidX support. Enable when 'android.gradle_dependencies'
# contains an 'androidx' package, or any package from Kotlin orgs.
android.enable_androidx = True

# (list) add java compile options
android.add_compile_options = sourceCompatibility = 1.8 targetCompatibility = 1.8

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (bool) enable --enable-androidx flag (for p4a build)
#p4a.enable_androidx = True

# (list) add java package
#android.add_src =

# (list) add aar project
#android.add_aar =

# (list) gradle plugins
#android.gradle_plugins =

# (bool) Indicate whether the screen should stay on
# Don't use awake in your game code if you use this!
android.wakelock = False

# (list) Android application permissions
# (See https://developer.android.com/reference/android/Manifest.permission for permissions)
android.permissions = INTERNET,VIBRATE

# (list) features (list of strings or tuples) to add to the manifest
#android.features = [('android.hardware.usb.host', 'usb accessory')]

# (int) Target Android API, should be as high as possible.
#android.target_api = 31

# (int) Minimum API your APK / AAB will support.
#android.minapi =

# (int) Android SDK version to use
#android.sdk =

# (str) Android NDK version to use
#android.ndk =

# (int) Android NDK API to use. This is the minimum API your app will support,
# it should usually match android.minapi.
#android.ndk_api =

# (int) Android NDK r version to download (if not in android.ndk_path)
#android.ndk_r =

# (int) Android NDK side by side version to use (if available)
#android.ndk_side_by_side_version =

# (int) Android NDK side by side major version to use (if available)
#android.ndk_side_by_side_major_version =

# (str) Android NDK architecture to use (if not autodetected)
#android.ndk_arch =

# (bool) enables Android auto backup feature (Android API >=23)


# (str) XML file for custom backup rules (see official auto backup documentation)
#android.backup_rules =

# (str) If you need to insert variables into your AndroidManifest.xml file,
# you can do so with the manifestPlaceholders property.
# This property takes a map of key-value pairs. (via string)
# Usage example : android.manifest_placeholders = [myCustomUrl:\"org.kivy.customurl\"]
# android.manifest_placeholders = [:]

# Change this to True for release builds!
#android.release = False

# (str) Android signing properties
#android.keystore =

# (str) Android key alias
#android.keyalias =

# (str) Android keystore password
#android.keystorepass =

# (str) Android key password
#android.keypass =

# (str) Android signing key type (rsa, dsa, ec)
#android.keytype = rsa

# (str) Android signing digest algorithm (sha1, sha256)
#android.digest = sha256

# (str) Android signing v1/v2/v3 scheme
#android.v1sign = True
#android.v2sign = True
#android.v3sign = True

# (str) Android extra command line arguments for gradle
#android.gradle_args =

# (str) Android additional libraries to copy
#android.add_libs_armeabi_v7a =
#android.add_libs_arm64_v8a =
#android.add_libs_x86 =
#android.add_libs_mips =

# (list) Android AAR archives to add
#android.add_aars =

# (list) Gradle dependencies to add to the project (Android Gradle plugin)
#android.gradle_dependencies =

# (bool) Enable --enable-androidx flag (for p4a build)
#p4a.enable_androidx = True

# (str) extra command line arguments to pass when invoking pythonforandroid.toolchain
#p4a.extra_args =

# (str) python-for-android fork to use, defaults to upstream (kivy)
#p4a.fork = kivy

# (str) python-for-android branch to use, defaults to master
#p4a.branch = master

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
#p4a.source_dir =

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#p4a.local_recipes =

# (str) Filename to the hook for p4a
#p4a.hook =

# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2

# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
#p4a.port =

# Control passing the --use-setup-py vs --ignore-setup-py to p4a
#p4a.setup_py = False

# Control passing --use-pkgname vs not to p4a (default is False for kivy bootstrap)
#p4a.use_p4a_fork = False

# Control passing the --private vs --dir argument to p4a
#p4a.private = .

# (str) python-for-android fork to use, defaults to upstream (kivy)
#p4a.url =

# Control passing the --bootstrap argument to p4a
#p4a.bootstrap =

# Control passing the --requirements argument to p4a
#p4a.requirements =

# Control passing the --archs argument to p4a
#p4a.archs =

# Control passing the --copy-libs argument to p4a
#p4a.copy_libs =

# Control passing the --color=always argument to p4a
#p4a.color = always

# Control passing the --storage-paths argument to p4a
#p4a.storage_paths =

# Control passing the --no-byte-compile argument to p4a
#p4a.no_byte_compile = False

# Control passing the --ignore-setup-py argument to p4a
#p4a.ignore_setup_py = False

# Control passing the --use-setup-py argument to p4a
#p4a.use_setup_py = False

# (str) python-for-android dist name to use
#p4a.dist_name =

# (str) extra command line arguments to pass when invoking pythonforandroid.toolchain
#p4a.extra_args =

# (str) python-for-android recipe blacklist to use
#p4a.recipe_blacklist =

# (str) python-for-android recipe whitelist to use
#p4a.recipe_whitelist =

# (bool) Whether or not to sign the debug build (set to False to speed up debug builds)
#android.sign_debug = True

# Change to True to build an .aab (Android App Bundle) instead of an .apk
#android.release_aab = False

# (str) --target argument to pass to p4a when building the dist
#p4a.target =

# (str) --name argument to pass to p4a when building the dist
#p4a.name =

# (bool) --use-setup-py argument to pass to p4a when building the dist
#p4a.use_setup_py = False

# (str) --bootstrap argument to pass to p4a when building the dist
#p4a.bootstrap = sdl2

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run outside a virtualenv, set to 0 to disable
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .xcodeproj, .app, etc)
# bin_dir = ./bin

#    -----------------------------------------------------------------------------
#    List as sections
#
#    You can define all the "list" as [section:key].
#    Each line will be considered as a option to the list.
#    Let's take [app] / source.exclude_patterns.
#    Instead of doing:
#
#[app]
#source.exclude_patterns = license,images/*/*.jpg
#
#    This can be translated into:
#
#[app:source.exclude_patterns]
#license
#images/*/*.jpg
#    -----------------------------------------------------------------------------
