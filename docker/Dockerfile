FROM ubuntu:18.04

RUN apt-get update && apt-get -y install git python openjdk-11-jdk-headless libncurses5 lsb-release sudo python-pip
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata

RUN git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
ENV PATH="/depot_tools:${PATH}"

COPY install-build-deps-android.sh /tmp/install-build-deps-android.sh	
RUN bash /tmp/install-build-deps-android.sh