import jenkins

server = jenkins.Jenkins('http://localhost:8080',
                         username='admin',
                         password='f909736f8d9744649a604f3f61a74c53')  # place password here


user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
