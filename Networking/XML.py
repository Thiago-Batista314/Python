import xml.etree.ElementTree as et

print('=='*10)
print('Example 1:')
data = '''<person>
              <name>Chuck</name>
              <phone type="intl">
                  +1 734 303 4456
              </phone>
              <email hide="yes"/>
          </person>'''

tree = et.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('phone').text)

print('=='*10)
print('Example 2:')

input = '''
<stuff>
  <users>
    <user x="2">
        <id>01</id>
        <name>Chuck</name>
    </user>
    <user x="7">
        <id>09</id>
        <name>Charles</name>
    </user>    
  </users>
</stuff>
'''

stuff = et.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for account in lst:
    print('Name:', account.find('name').text)
    print('Id:', account.find('id').text)
    print('Atribute:', account.get('x'))
