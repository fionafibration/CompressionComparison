import lzma, gzip, zlib
import sys
import svgwrite

if __name__ == '__main__':
    data = sys.stdin.read().encode('utf-8')

    lzma_compressed = lzma.compress(data)
    gzip_compressed = gzip.compress(data)
    zlib_compressed = zlib.compress(data)

    original_size = len(data)

    lzma_size = len(lzma_compressed)
    gzip_size = len(gzip_compressed)
    zlib_size = len(zlib_compressed)

    lzma_ratio = lzma_size / original_size
    gzip_ratio = gzip_size / original_size
    zlib_ratio = zlib_size / original_size

    #lzma_ratio = .6
    #gzip_ratio = 1.1
    #zlib_ratio = .2


    print(lzma_ratio * 100, gzip_ratio * 100, zlib_ratio * 100)

    dwg = svgwrite.Drawing('out.svg', (1200, 400))

    # Title
    dwg.add(dwg.text('Compression Algorithms Compared', insert=(600, 30), font_size=30, text_anchor='middle'))

    # Subtitle
    dwg.add(dwg.text('By percentage of original size', insert=(600, 50), font_size=15, text_anchor='middle'))

    # LZMA
    dwg.add(dwg.circle(center=(300, 200), r=(lzma_ratio * 100), fill='blue'))

    dwg.add(dwg.text('LZMA: %.2f%%' % (lzma_ratio * 100), insert=(300, 200), font_size=15, text_anchor='middle'))

    # GZIP
    dwg.add(dwg.circle(center=(600, 200), r=(gzip_ratio * 100), fill='green'))

    dwg.add(dwg.text('GZIP: %.2f%%' % (gzip_ratio * 100), insert=(600, 200), font_size=15, text_anchor='middle'))

    # ZLIB
    dwg.add(dwg.circle(center=(900, 200), r=(zlib_ratio * 100), fill='red'))

    dwg.add(dwg.text('ZLIB: %.2f%%' % (zlib_ratio * 100), insert=(900, 200), font_size=15, text_anchor='middle'))

    dwg.save()