from ctypes import *
import Log

SOFT_DOG_DATA_SIZE = 256
SOFT_DOG_LIBRARY = "win32dll.dll"


def checkSoftDogLibraryIsExist():
    Log.d(SOFT_DOG_LIBRARY + " is exist.")
    return True


def _readSoftDogData(outBuffer):

    # TODO
    # Check SOFT_DOG_LIBRARY if is exits.
    if not checkSoftDogLibraryIsExist():
        return False

    windll = WinDLL(SOFT_DOG_LIBRARY)
    if not windll:
        Log.e("Load soft dog library: " + SOFT_DOG_LIBRARY + " failed!!!")
        return False
    
    Log.d("Load soft dog library: " + SOFT_DOG_LIBRARY + " Success.")

    if not windll.DogRead:
        Log.e("Can not find function entry: DogRead")
        return False

    dataBytes = c_ulong(90)
    readAddr = c_ulong(0)
    windll.DogRead.argtypes = [c_ulong, c_ulong, c_char_p]
    windll.DogRead(dataBytes, readAddr, outBuffer)

    return True


def readSoftDogData():
    softDogData = ""
    outBuffer = (c_char * SOFT_DOG_DATA_SIZE)('\0')

    if _readSoftDogData(outBuffer):
        for item in outBuffer:
            if item == '\0':
                break
            softDogData = softDogData + item

    return softDogData





    
