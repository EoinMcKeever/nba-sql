import bcrypt

email = 'eoinmckeever0@gmail.com'
password = 'scoil Aonghusa'
hashedPassword = bytes(password, 'utf-8')
salt = '$2a$11$BskwriWPCvnk/aIpIXvd.u'
hashedsalt = bytes(salt, 'utf-8')

salted_password = bcrypt.hashpw(hashedPassword, hashedsalt)

print(salted_password)

