"""Optional: bundle into one self-contained campus-map.html (python3 build.py)."""
h = open('index.html').read()
tag = '<script src="colleges.js"></script>'
assert tag in h
h = h.replace(tag, '<script>\n' + open('colleges.js').read().replace('</script>', '<\\/script>') + '\n</script>')
open('campus-map.html', 'w').write(h)
print('wrote campus-map.html')
