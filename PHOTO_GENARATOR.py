import json
import time
import requests


class IMAGE_CREATE:
    def __init__(self,API):
        self.API = API
        self.url = "https://api.starryai.com/creations/"
    def CREATE_IMAGE(self,promt,negative_promt="blurry, distorted, extra limbs, extra fingers, malformed hands, bad anatomy, unrealistic proportions, low quality, watermark, text, cropped, deformed, ugly, mutated"):
            #realvisxl
            #luna_3d
            #anime
            #anime_v2
        payload = {
            "model": "realvisxl",
            "aspectRatio": "square",
            "highResolution": False,
            "images": 1,
            "steps": 20,
            "initialImageMode": "color",
            "prompt": f"{promt}",
            "negativePrompt": f"{negative_promt}"
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-Key": f"{self.API}"
        }

        response = requests.post(self.url, json=payload, headers=headers)
        jsondata = json.loads(response.text)
        print(response.text)
        id = jsondata["id"]
        while True:
            print("--FOTO BEKLENIYOR--")

            url = f"https://api.starryai.com/creations/{id}"

            headers = {
                "accept": "application/json",
                "X-API-Key": f"{self.API}"
            }

            response = requests.get(url, headers=headers)

            jsondata = json.loads(response.text)
            status = jsondata["status"]

            if status == "completed":
                img = jsondata["images"][0]["url"]
                print(img)
                print("--FOTO HAZIR--")
                return img
            time.sleep(5)


"""
ART = IMAGE_CREATE(API="pydUukSnUQvhyqX-BbHF-BqEbMdFyw") 
ART.CREATE_IMAGE("ss")

"""