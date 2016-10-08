from flask import Flask, render_template
import extensions
import controllers
import config
import os

if __name__ == '__main__':
    # listen on external IPs
    app.run(host=config.env['host'], port=config.env['port'], debug=True)