##### Android Studio and toolchain

1. Install SDK at ~/android/sdk
2. Install tools


| Tool              | Description                                                              |
|-------------------|--------------------------------------------------------------------------|
| adb               | interacts with apps and emulators                                        |
| aapt              | build tool, apk compilation                                              |
| apktool           | (un)packs apk, smali/baksmali                                            |
| smali/baksmali    | (.dex -> .smali(.class)) (disassembler)                                  |
| keytool           | generate keystore with a key                                             |
| jarsigner         | sign apk with the key                                                    |
| tar/7z            | unpack apk                                                               |
| apksigner         | sign apk                                                                 |
| zipalign          | optimization                                                             |
|                   |                                                                          |
| dex2jar           | (.dex -> .class(.smali)) and back + dextools (disassembler)              |
| jadx              | (.dex -> .class(.smali) -> .java) (CLI + UI) (decompiler + disassembler) |
| FernFlower/JD-GUI | (.class -> .java) + GUI (decompiler)                                     |


    # zipalign, appt, apksigner, dexdump under ~\tools\android\sdk\build-tools\<version>\
    # adb under ~\tools\android\sdk\platform-tools
    
    # 7z in Program Files/7-Zip + tar in PATH
    # keytool, jarsigner is available in JAVA_HOME/bin

    # android ctl