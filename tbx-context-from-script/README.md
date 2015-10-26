A test to see what calling environment is presented when executing a 
script tool. Confirmed nothing about calling envrionment. Here's the 
callstack:

    0, ntoskrnl.exe!PoStartNextPowerIrp+0x17e7
    1, ntoskrnl.exe!KeWaitForMultipleObjects+0xf5d
    2, ntoskrnl.exe!KeWaitForMutexObject+0x19f
    3, ntoskrnl.exe!PoStartNextPowerIrp+0xba4
    4, ntoskrnl.exe!PoStartNextPowerIrp+0x1821
    5, ntoskrnl.exe!PoStartNextPowerIrp+0x1a97
    6, python27.dll!PyLong_AsLongLongAndOverflow+0x5f4
    7, 0x3fdf38003fdfcc
    8, 0xa293c0020
    9, 0x100000000
    10, 0x293c00201e0a5de1
    11, python27.dll!PyLong_AsLongLongAndOverflow+0x5f4 (No unwind info)
    12, python27.dll!PyLong_Format+0x21 (No unwind info)
    13, python27.dll!PyString_AsEncodedString+0xed (No unwind info)
    14, arcgisscripting.pyd+0x379b (No unwind info)
    15, python27.dll!PyLong_AsDouble+0xf0 (No unwind info)
    16, python27.dll!PyObject_Str+0x77 (No unwind info)
