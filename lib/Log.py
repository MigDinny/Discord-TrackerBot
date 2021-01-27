# Logging system
# (possibly with colors, depends on OS and my will to code that)
# prints a message on console with a TAG

# Methods

# warning() - for warnings related due to something happen that could raise an exception
# error() - for an error that could possibly/certainly crash the program or reproduce undesirable effects
# info() - for any information that could be useful when inspecting the server
# debug() - for debugging purposes

def printLog(logType, message):
    if (logType == 'w'):
        print("[WARNING]:", message)
    
    if (logType == 'e'):
        print("[ERROR]:", message)
    
    if (logType == 'i'):
        print("[INFO]:", message)

    if (logType == 'd'):
        print("[DEBUG]:", message)

def warning(msg):
    printLog('w', msg)

def error(msg):
    printLog('e', msg)

def info(msg):
    printLog('i', msg)

def debug(msg):
    printLog('d', msg)

# abrev

def w(msg):
    warning(msg)

def e(msg):
    error(msg)

def i(msg):
    info(msg)

def d(msg):
    debug(msg)