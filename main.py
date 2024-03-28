# DISCLAIMER:
# This generator is provided for educational and testing purposes only. By using this application, you acknowledge that:
#    The author(s) and any/all contributor(s) of this project make no representations or warranties of any kind regarding the accuracy, completeness, or suitability of the project for any purpose.
#    The author(s) and any/all contributor(s) of this project shall not be liable for any direct, indirect, special, incidental, or consequential damages arising out of the use or inability to use the project, even if advised of the possibility of such damages.
# Use this project at your own risk. You are solely responsible for any consequences resulting from the use of this generator.

import json

# This is just a basic ShareX template that we will modify to allow this to work.
sxTemplate = {
    "Version": "16.0.0",
    "Name": "",
    "DestinationType": "ImageUploader, TextUploader, FileUploader",
    "RequestMethod": "POST",
    "RequestURL": "",
    "Parameters": {
        "filename": "$filename$"
    },
    "Body": "Binary",
    "URL": "$json:upload.attachments[0].mapped_content_url$"
}

# Names that come before the .zendesk.com part of the URL.
znames = ["urlname1", "urlname2", "urlname3"] 

def createSXCU(zname):
    sxTemplate["Name"] = zname
    sxTemplate["RequestURL"] = "https://" + str(zname) + ".zendesk.com/api/v2/uploads.json" 
    with open(f"{zname}.sxcu", "w") as f:
        json.dump(sxTemplate, f, indent=4)

for zname in znames: 
    createSXCU(zname)
    
