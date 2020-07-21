#!/usr/bin/env python3
import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel("INFO")


def cidrsubnet(prefix: str, newbits: int, netnum: int) -> str:
    """
    Implementation of the cidrsubnet function from
    https://www.terraform.io/docs/configuration/functions/cidrsubnet.html
    """
    if ':' in prefix:
        raise ValueError("IP6 addresses not supported")
    # Split the ip address into network and host
    address, notation = prefix.split("/")
    new_notation = int(notation) + newbits
    # Binary representation
    b = "".join([bin(int(x))[2:].zfill(8) for x in address.split(".")])
    b = b[:int(notation)] + bin(netnum)[2:].zfill(newbits) + b[new_notation:]
    address = ".".join([str(int(b[x:x+8], 2)) for x in range(0, 32, 8)])

    return address + '/' + str(new_notation)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        logger.error("Usage: ./cidrsubnet prefix newbits netnum "
                     "i.e. ./cidrsubnet 10.1.2.0/24 4 15")
        sys.exit(1)
    prefix = sys.argv[1]
    newbits = int(sys.argv[2])
    netnum = int(sys.argv[3])
    logger.info("calculating...")
    print(cidrsubnet(prefix, newbits, netnum))
