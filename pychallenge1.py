import string
alpha = string.ascii_lowercase

x = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
url = 'map'

newalpha = 'cdefghijklmnopqrstuvwxyzab'
table = x.maketrans(alpha, newalpha)
print(x.translate(table))
print(url.translate(table))