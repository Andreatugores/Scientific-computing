def upload_to_zenodo(path, filename, data):

    # Tools
    import time
    import requests
    import json

    # Ask for token
    ACCESS_TOKEN = input(str("Please, paste your token: "))
    input("Press Enter to start the uploading process. Note this can take some time.")
    print("Requesting access to your acount...")

    # Access the API
    params = {'access_token': ACCESS_TOKEN}
    r_0 = requests.get('https://zenodo.org/api/deposit/depositions', params=params)
    r0_status = r_0.status_code

    # In case of errors
    while r0_status not in (200, 201, 202, 204):
        if r0_status in (400, 401, 403):
            error_message = f"""{r0_status}: Request failed. The access to your account was forbidden.
            The reason for this error is a missing or invalid token.
            Check your token or generate a new one from:
            https://zenodo.org/account/settings/applications/tokens/new/
            """
            print(error_message)
            input("When you are ready, press Enter.")
            ACCESS_TOKEN = input(str("Please, paste your token: "))
            input("Press Enter to start the uploading process. Note this can take some time.")
            print("Requesting access to your acount...")

            # Access the API
            params = {'access_token': ACCESS_TOKEN}
            r_0 = requests.get('https://zenodo.org/api/deposit/depositions', params=params)
            r0_status = r_0.status_code
        else:
            input("We are sorry to inform that there is troubling accesing "
                  "to the Zenodo servers right now. We will have to take you "
                  "back to the main menu. Please, press enter.")
            return

    # Acces: Success
    if r0_status in (200, 201, 202, 204):
        print(f"{r0_status}: Request succeeded. The access to your account was granted. Please wait...\n")

    # Create empty upload
    headers = {"Content-Type": "application/json"}

    r_1 = requests.post('https://zenodo.org/api/deposit/depositions', params=params, json={}, headers=headers)
    r1_status = r_1.status_code

    print(f"{r1_status}: Request succeeded. An empty upload was created. Please wait...\n")

    bucket_url = r_1.json()["links"]["bucket"]
    deposition_id = r_1.json()['id']

    # Put
    with open(path, "rb") as fp:
        r_2 = requests.put("%s/%s" % (bucket_url, filename), data=fp, params=params)
    r2_status = r_2.status_code

    print(f"{r2_status}: Request succeeded. Access granted. Your file was uploaded...\n")


    # Post
    r_3 = requests.put('https://zenodo.org/api/deposit/depositions/%s' % deposition_id,
                       params=params, data=json.dumps(data), headers=headers)
    r3_status = r_3.status_code

    print(f"{r3_status}: Request succeeded. Access granted. The metadata was updated. \n")

    return
