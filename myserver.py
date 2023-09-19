import socketpool
import wifi
import time



webServer = None
logger = None

def setLogger(_logger):

    global logger
    logger = _logger

def loadFile(filename):
    logger.info(f'Loading file: {filename}...')
    try:
        fileData = io.open(filename, mode="r")
        logger.info(f'File Loaded: {filename}' )
        return json.load(fileData)

    except:
        raise Exception(f'There was an error loading file: {filename}')

def startWebServer():
    global CONFIG_DATA
    global webServer

    #TO DO: TEST TO ENSURE THE INDEX.HTML FILE IS ACTUALLY BEING SERVED
    print("Starting web server...")


    # from adafruit_httpserver.mime_type import MIMEType
    from adafruit_httpserver import Server, MIMETypes, Request, Response, FileResponse, JSONResponse, GET, POST, PUT, DELETE
    # from adafruit_httpserver.request import HTTPRequest
    # from adafruit_httpserver.response import HTTPResponse
    # from adafruit_httpserver.server import HTTPServer

    MIMETypes.configure(
        default_to="text/plain",
        keep_for=[".html", ".css", ".js"]
    )
    pool = socketpool.SocketPool(wifi.radio)
    webServer = Server(pool, "/static", debug=True)
    
    
    # @webServer.route("/test", append_slash=True)
    # def test(req: Request):
    #     logger.info("GET - /test")

    #     return Response(req, "TEST")

    # @webServer.route("/api/songs", append_slash=True)
    # def apiSongs(req: Request):

    #     if req.method == "GET":
    #         logger.info("GET - /api/songs")
    #         return JSONResponse(req, {"songs": ["song1", "song2"]})
    
    # @webServer.route("/")
    # def base(req: Request):

    #     logger.info("GET - /")

    #     with open("index.html") as f:
    #         try:
    #             html = f.read().format("hidden", "TEST TEST STESTSETSETSETSETSET")
    #             return Response(req, html, content_type="text/html")
    #         except Exception as e:
    #             logger.error(str(e))
    #             raise Exception("Error")
    #             return Response(req, "TEST")

    logger.info(f"listening on http://{wifi.radio.ipv4_gateway_ap}:80")
    webServer.start(str(wifi.radio.ipv4_gateway_ap))