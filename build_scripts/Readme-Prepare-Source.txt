To prepare chromium full source:
* create empty folder <FolderA>;
* copy tools/download_dependencies.py to the folder, enter to the folder and run the scrypt;
* wait until script finish, downloaded sources size ~ 26GB;
* create another folder <FolderB> and clone git@github.com:demetrionq/chromium.git , use the following command
    git clone --branch develop --depth 100 git@github.com:demetrionq/chromium.git
* after cloning copy .git folder to <FolderA>/src;
* enter to <FolderA>/src and run
    git reset --hard
* create folder <FolderA>/src/out/android_<platform>
* copy to the directory file args.gn (edit if needed);
* run commands
    gn gen out/amdroid_<platform>
    autoninja -C out/amdroid_<platform> chrome_public_apk
to compile with minSdkVersion=24 use
    autoninja -C out/amdroid_<platform> monochrome_public_bundle