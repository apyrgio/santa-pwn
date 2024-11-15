FROM dangerzone.rocks/dangerzone

# Copy the rasterizer secret to the root filesystem of the inner gVisor sandbox.
COPY rasterizer /home/dangerzone/dangerzone-image/rootfs
# Copy the gvisor secret to the root filesystem of the outer Dangerzone container
COPY gvisor /
