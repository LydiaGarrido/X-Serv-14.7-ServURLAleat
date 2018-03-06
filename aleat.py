#!/usr/bin/python3

import socket
import random
import webapp


class NumeroAleat(webapp.webApp):

    def process(self, parsedRequest):
        numero_aleat = random.randint(1, 1000000)
        return ("200 OK", "<html><body><h1><a href=http://localhost:1234/" +
                str(numero_aleat) + ">Dame otra</h1></body></html>")

if __name__ == "__main__":
        my_webapp = NumeroAleat("localhost", 1234)
