import click
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import os
import json
from credentials import apiKey
app = ClarifaiApp(api_key = apiKey)


@click.command()
@click.argument('path',type = click.Path(exists=True),required = True)
def quality(path):
    model = app.models.get('Landscape quality')
    """ORGANIZE PHOTOS BASED ON QUALITY"""


    if not os.path.exists(path+'/'+'good'):
        os.mkdir(path+'/'+"good")
    if not os.path.exists(path+"/"+"bad"):
        os.mkdir(path+"/"+"bad")


    for filename in os.listdir(path):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith("jpg") or filename.endswith("JPG"):
            image = ClImage(file_obj = open(path+"/"+filename,'rb'))
            jsonResp = model.predict([image])
            goodphoto = jsonResp['outputs'][0]['data']['concepts'][0]['name']
            if goodphoto =='high quality':
                os.rename(path+'/'+filename,path+"/good"+filename)
                print(filename+" : Good photo")
            elif goodphoto == 'low quality':
                os.rename(path+"/"+filename, path+"/bad"+filename)
                print(filename+" : BAD Photo")


if __name__ == '__main__':
    quality('photos')