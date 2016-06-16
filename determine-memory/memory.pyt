import arcpy
import ctypes
from ctypes import wintypes

GetCurrentProcess = ctypes.windll.kernel32.GetCurrentProcess
GetCurrentProcess.argtypes = []
GetCurrentProcess.restype = wintypes.HANDLE

SIZE_T = ctypes.c_size_t

class PROCESS_MEMORY_COUNTERS_EX(ctypes.Structure):
    _fields_ = [
        ('cb', wintypes.DWORD),
        ('PageFaultCount', wintypes.DWORD),
        ('PeakWorkingSetSize', SIZE_T),
        ('WorkingSetSize', SIZE_T),
        ('QuotaPeakPagedPoolUsage', SIZE_T),
        ('QuotaPagedPoolUsage', SIZE_T),
        ('QuotaPeakNonPagedPoolUsage', SIZE_T),
        ('QuotaNonPagedPoolUsage', SIZE_T),
        ('PagefileUsage', SIZE_T),
        ('PeakPagefileUsage', SIZE_T),
        ('PrivateUsage', SIZE_T),
    ]

GetProcessMemoryInfo = ctypes.windll.psapi.GetProcessMemoryInfo
GetProcessMemoryInfo.argtypes = [
    wintypes.HANDLE,
    ctypes.POINTER(PROCESS_MEMORY_COUNTERS_EX),
    wintypes.DWORD,
]
GetProcessMemoryInfo.restype = wintypes.BOOL

def get_current_process():
    """Return handle to current process."""
    return GetCurrentProcess()

def get_memory_info(process=None):
    """Return Win32 process memory counters structure as a dict."""
    if process is None:
        process = get_current_process()
    counters = PROCESS_MEMORY_COUNTERS_EX()
    ret = GetProcessMemoryInfo(process, ctypes.byref(counters),
                               ctypes.sizeof(counters))
    if not ret:
        raise ctypes.WinError()
    info = dict((name, getattr(counters, name))
                for name, _ in counters._fields_)
    return info

def get_memory_usage(process=None):
    """Return this process's memory usage in bytes."""
    info = get_memory_info(process=process)
    return info['PrivateUsage']/(1024.0**2)

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Memory]

class Memory(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Memory Use"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = None
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        arcpy.AddMessage("Initial memory usage: {0:.2f}MB".format(get_memory_usage()))
        import numpy as np

        t = np.ones(100000000)
        arcpy.AddMessage("Memory usage with 100M element array: {0:.2f}MB".format(get_memory_usage()))

