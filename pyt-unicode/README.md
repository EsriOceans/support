Ultimately, AddMessage is going to display the Python strings passed to it in the [Windows-1252](https://en.wikipedia.org/wiki/Windows-1252). If I pass it valid 1252 bytestreams, it will display them correctly, but not UTF-8 encoded values (which occupy two bytes -- it interprets them as one byte 1252 strings instead).


The best way I've found to to handle this consistently in Py2+3, Pro+ArcMap is a hack and a half:

1. convert the string to cp1252, replacing unknown characters with the cp1252 unknown symbol:
  ```python
    s = "票西表島構内評豹掛川日本迎票府怖扶敷".encode("windows-1252", "replace")
  ```
  This will mostly handle Unicode strings, though some codepoints are missing, such as ,[川](https://en.wiktionary.org/wiki/%E5%B7%9D), codepoint 0x5DDD, or [kanxi radical 47](https://en.wikipedia.org/wiki/Radical_47) (river), which is part of the [Kangxi radical](https://en.wikipedia.org/wiki/Kangxi_radical) system.

2. Decode the resulting string as 'utf-8', even though it is really encoded as cp1252, and ignore any unknown characters in the output stream:    
```python
    arcpy.AddMessage(t.decode("utf-8", errors="ignore"))
```

Note that if you set `errors="replace"` instead, you'll get two error characters: the original entry from the cp1252 instance, and a second one from the utf-8 error. 

If you want a parameter value to be correctly encoded and displayed, combine the steps:

```python
param_1.value = "票西表島構内評豹掛川日本迎票府怖扶敷".encode("cp1252", "ignore").decode("utf-8", "ignore")
```

Related
-------

CRs:

 - jpn report on truncated multibyte values: [58154](http://qamonitor/QACommon/CrLookup.aspx?id2=41641)
 - ask for documentation for [unicode in Python](http://qamonitor/QACommon/CrLookup.aspx?id2=619500)

Kube:

 - http://kube.esri.com/index.cfm?event=ehcontent.dspcontent&type=supportincidents&id=1136279&kw=addmessage%20unicode


