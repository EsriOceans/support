
```python
    locale.getlocale()
    ('English_United States', '1252')
    
    locale.getdefaultlocale()
    ('en_US', 'cp1252')


def preferred_encoding():
    enc = locale.getpreferredencoding(do_setlocale=False) # 'cp1252'

    # if none or ascii, set to 'cp1252'.
    if enc is None or enc == 'ascii':
        enc = 'cp1252'

    return enc


def unicode_to_pref(obj):
    enc = codecs.getencoder(preferred_encoding())
    return enc(obj, 'strict')[0]


def pref_to_unicode(obj):
    dec = codecs.getdecoder(preferred_encoding())
    return dec(obj, 'strict')[0]

```

