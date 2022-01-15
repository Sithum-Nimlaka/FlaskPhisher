from pyngrok import ngrok


def ngrokTunnel(port):
    http_tunnel = ngrok.connect(port)
    x = str(http_tunnel)
    x = (x[14:51])
    x = x.replace('"', "")
    return x
