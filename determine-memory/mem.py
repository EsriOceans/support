import ctypes


def ram():
    kernel32 = ctypes.windll.kernel32
    c_ulong = ctypes.c_ulong

    class MEMORYSTATUS(ctypes.Structure):
        _fields_ = [
            ('dwLength', c_ulong),
            ('dwMemoryLoad', c_ulong),
            ('dwTotalPhys', c_ulong),
            ('dwAvailPhys', c_ulong),
            ('dwTotalPageFile', c_ulong),
            ('dwAvailPageFile', c_ulong),
            ('dwTotalVirtual', c_ulong),
            ('dwAvailVirtual', c_ulong)
        ]

    memory_status = MEMORYSTATUS()
    memory_status.dwLength = ctypes.sizeof(MEMORYSTATUS)
    kernel32.GlobalMemoryStatus(ctypes.byref(memory_status))
    return (memory_status.dwTotalPhys, memory_status.dwAvailPhys)

r = ram()
(total, available) = r
print("total memory installed: {}".format(total / (1024**2)))
print("available memory: {}".format(available / (1024**2)))
