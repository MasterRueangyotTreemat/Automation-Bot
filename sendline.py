import requests


def Lineconfig(command):
	url = 'https://notify-api.line.me/api/notify'
	token = 'Ng3KNR23QI8gscf4r4ZTYVGAUYQtWRooEOfocwJI1CK' ## EDIT
	header = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
	return requests.post(url, headers=header, data = command)

def sendtext(message):
	# send plain text to line
	command = {'message':message}
	return Lineconfig(command)


def sticker(sticker_id,package_id):
	command = {'message':" ",'stickerPackageId':package_id,'stickerId':sticker_id}
	return Lineconfig(command)


def sendimage(url):
	command = {'message':" ",'imageThumbnail':url,'imageFullsize':url}
	return Lineconfig(command)




#sendtext('Hi สวัสดีชาวโลก')
#sticker(3,1)
#sendimage('https://lh3.googleusercontent.com/l09NtAZT74fuG7wVxEKgMjwVkD-8D6XQJWkBKrZvdx_PX89W8mOV2wheoCN1IbwHlVEHfk7qZAs=w210-h260-n')

#Bot Check gmail
