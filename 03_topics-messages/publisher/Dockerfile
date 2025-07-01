FROM ros:jazzy

SHELL ["/bin/bash", "-c"]

WORKDIR /app

RUN apt-get update && apt-get install -y
RUN apt-get install vim nano -y

COPY test_package test_package
RUN cd test_package && colcon build

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["bash"]