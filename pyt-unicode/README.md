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

Codepage support
----------------

Starting from a CMD prompt, can also get [cp437](https://en.wikipedia.org/wiki/Code_page_437) as the default codepage.

Do our Pythons support wide unicode characters?

```python
import sys
sys.maxunicode > 0xffff
```

ver | supports UCS-4
--- | --------------
ArcGIS 10.3 | False
ArcGIS 10.3 Background GP | False
Pro 1.2 | True

apparently a [known issue with Windows + Py 2.x support](https://www.python.org/dev/peps/pep-0261/), fixed in Python 3.3+

Related
-------


SO:
 - http://stackoverflow.com/questions/19525319/arcpy-and-python-encoding-messing-up
  > By default, python in the command line is not going to change the code page to a UTF-8 based text for print statements to show up in Unicode. ArcGIS on the other hand specifically allows unicode values to be passed to it and has changed the code page within the command line so that the values you see printed are the values ArcGIS is using. This is why the command line should be the only environment where you see the import sys followed by import arcpy give you a different printed value.

CRs:

 - jpn report on truncated multibyte values: [58154](http://qamonitor/QACommon/CrLookup.aspx?id2=41641)
 - ask for documentation for [unicode in Python](http://qamonitor/QACommon/CrLookup.aspx?id2=619500)

Kube:

 - http://kube.esri.com/index.cfm?event=ehcontent.dspcontent&type=supportincidents&id=1136279&kw=addmessage%20unicode
 - http://kube.esri.com/index.cfm?event=ehcontent.dspcontent&type=supportincidents&id=1221799&kw=changed%20code%20page%20unicode

Locale codepage files:
 - \SupportFiles\ArcGIS\locale

SDE     ORACLE         INFORMIX    SYBASE    DB2      SQLSERVER ARCINFO
------  ------         --------    ------    ---      --------- -------
big5    zht16big5      big5        big5      950      big5      BIG5
big5    zht16hkscs     big5        big5      950      big5      BIG5
big5    zht16mswin950  big5        big5      950      big5      BIG5
tw_euc  zht32euc       EUCXtwn     euccns    964      euccns    zh_tw,EUC
zh      cgb2312-80     gb          eucgb     1383     eucgb     zh,EUC
zh      cgb2312-80     gb          eucgb     1383     eucgb     zh
sjis    ja16sjis       sjis-s      sjis      932      sjis      SJIS
jpn_euc ja16euc        ujis        eucjis    954      eucjis    ja,EUC
ko      ko16ksc5601    ksc         eucksc    949      eucksc    ko,EUC
ko      ko16ksc5601    ksc         eucksc    949      eucksc    ko
88591   we8iso8859p1   8859-1      iso_1     819      iso_1     88591
88592   ee8iso8859p2   8859-2      iso88592  912      iso_2     88592
88593   se8iso8859p3   8859-3      iso88593  none     iso_3     88593
88594   nee8iso8859p4  8859-4      iso88594  none     iso_4     88594
88595   cl8iso8859p5   8859-5      iso88595  915      iso_5     88595
88596   ar8iso8859p6   8859-6      iso88596  1089     iso_6     88596
88597   el8iso8859p7   8859-7      iso88597  813      iso_7     88597
88598   iw8iso8859p8   8859-8      iso88598  916      iso_8     88598
88599   we8iso8859p9   8859-9      iso88599  920      iso_9     88599
885910  ne8iso8859p10  8859-10     iso885910 none     iso_10    885910
885913  blt8iso8859p13 8859-13     iso885913 none     iso_13    885913
885915  we8iso8859p15  8859-15     iso885915 none     iso_15    885915
roman8  we8roman8      none        none      none     roman8    none
437     us8pc437       437         cp437     437      cp437     437
850     we8pc850       PC-Latin-1  cp850     850      cp850     850
851     el8pc851       851         cp851     851      cp851     851
852     ee8pc852       PC-Latin-2  cp852     852      cp852     852
855     ru8pc855       855         cp855     855      cp855     855
857     tr8pc857       857         cp857     857      cp857     857
860     we8pc860       860         cp860     860      cp860     860
861     is8pc861       861         cp861     861      cp861     861
862     iw8pc1507      862         cp862     862      cp862     862
863     cdn8pc863      863         cp863     863      cp863     863
864     none           864         cp864     864      cp864     864
865     n8pc865        865         cp865     865      cp865     865
866     ru8pc866       866         cp866     866      cp866     866
869     el8pc869       869         cp869     869      cp869     869
708     none           708         cp708     708      cp708     708
720     none           720         cp720     720      cp720     720
737     el8pc737       737         cp737     737      cp737     737
775     blt8pc775      775         cp775     775      cp775     775
1250    ee8mswin1250   CP1250      cp1250    1250     cp1250    1250
1251    cl8mswin1251   CP1251      cp1251    1251     cp1251    1251
1252    we8mswin1252   CP1252      cp1252    1252     cp1252    1252
1253    el8mswin1253   CP1253      cp1253    1253     cp1253    1253
1254    tr8mswin1254   CP1254      cp1254    1254     cp1254    1254
1255    iw8mswin1255   CP1255      cp1255    1255     cp1255    1255
1256    ar8mswin1256   CP1256      cp1256    1256     cp1256    1256
1257    blt8mswin1257  CP1257      cp1257    1257     cp1257    1257
1258    vn8mswin1258   CP1258      cp1258    1258     cp1258    1258


Other Resources
---------------

Python-specific:
 - [Python 3 HOWTO on Unicode](https://docs.python.org/3/howto/unicode.html)
 - [Python 2 HOWTO on Unicode](https://docs.python.org/2/howto/unicode.html)
 - [codecs module](https://docs.python.org/2/library/codecs.html)


Windows-specific:
 - [Windows locales](https://msdn.microsoft.com/en-us/goglobal/bb895996.aspx)
    + error crash reports include the Locale ID as a decimal value
 - [comparing iso8859 to windows 1252](http://i18nqa.com/debug/table-iso8859-1-vs-windows-1252.html)
 - [Windows 1252, Wikipedia](https://en.wikipedia.org/wiki/Windows-1252)

[Unicode as Windows Command Prompt](http://illegalargumentexception.blogspot.com/2009/04/i18n-unicode-at-windows-command-prompt.html)

[A treastise on why UTF-8 for everything in a Windows app](http://www.nubaria.com/en/blog/?p=289)
