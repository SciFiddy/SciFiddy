* [wsl](https://learn.microsoft.com/en-us/windows/wsl/)
* https://learn.microsoft.com/en-us/windows/wsl/install
* https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers
* https://learn.microsoft.com/en-us/windows/wsl/use-custom-distro
* [OpenSolaris](https://en.wikipedia.org/wiki/OpenSolaris)


## Ubuntu 22

* https://askubuntu.com/questions/159575/how-do-i-make-java-default-to-a-manually-installed-jre-jdk/159585#159585


    `sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/java-19-openjdk-amd64/bin/java 1919`



    ```bash
    abc@LAPTOP-AC4DSIST:/$ sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/java-19-openjdk-amd64/bin/java 1919
    update-alternatives: warning: forcing reinstallation of alternative /usr/lib/jvm/java-19-openjdk-amd64/bin/java because link group java is broken
    abc@LAPTOP-AC4DSIST:/$ java -version
    openjdk version "19.0.1" 2022-10-18
    OpenJDK Runtime Environment (build 19.0.1+10-Ubuntu-1ubuntu122.04)
    OpenJDK 64-Bit Server VM (build 19.0.1+10-Ubuntu-1ubuntu122.04, mixed mode, sharing)
    ```



* https://askubuntu.com/questions/1195661/install-tomcat-9-on-ubuntu-server-18-04-3

    tryna run tomcat...

    ```bash
    sudo groupadd tomcat
    ```
