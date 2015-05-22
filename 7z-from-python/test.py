from py7zlib import Archive7z
fp = open('genegis_vector.sd', 'rb')
archive = Archive7z(fp)
archive.version
xml = archive.getmember('esriinfo/metadata/metadata.xml')
xml.read()
archive.files_map
rchive.list()
md_file = archive.files[6]
md_file.read()
md_file.attributes
md_file.uncompressed
md_file.size
md = archive.files_map['esriinfo/metadata/metadata.xml']
md.size
md.uncompressed
md.read()
md.reset
