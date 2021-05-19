# Find controlled vocabulary for upload type
def upload_metadata(upload_input):
    import pandas as pd
    # Generate dataframe from the upload type options
    upload_md = pd.read_csv("metadata/upload_type.csv", header=0, dtype="str")
    # Find the controlled vocabulary of that option
    try:
        find_upload = upload_md[upload_md.eq(upload_input).any(axis=1)]
        upload = find_upload.iloc[0]["upload_MD"]
    except:
        upload = "other"
    return upload


# Find controlled vocabulary for publication type
def pub_metadata(pub_input):
    import pandas as pd
    # Generate dataframe from the publication type options
    pub_md = pd.read_csv("metadata/publication_type.csv", header=0, dtype="str")
    # Find the controlled vocabulary of that option
    try:
        find_publication = pub_md[pub_md.eq(pub_input).any(axis=1)]
        publication = find_publication.iloc[0]["publication_MD"]
    except:
        publication = "other"
    return publication


# Find controlled vocabulary for image type
def image_metadata(image_input):
    import pandas as pd
    # Generate dataframe from the image type options
    image_md = pd.read_csv("metadata/image_type.csv", header=0, dtype="str")
    # Find the controlled vocabulary of that option
    try:
        find_image = image_md[image_md.eq(image_input).any(axis=1)]
        image = find_image.iloc[0]["image_MD"]
    except:
        image = "other"  
    return image


# Generate the metadata: a dictionary from the variables
def generate_md(title, description, publication_date, upload, image, publication, creators):
    
    if publication != "None":
        data = {'metadata': {'title': f'{title}',
                             'description': f'{description}',
                             'publication_date': f'{publication_date}',
                             'upload_type': f'{upload}',
                             'publication_type': f'{publication}',
                             'creators': creators}}
        
        print("The metadata has been stored.\n"
              "You can always change it in Zenodo's website after you upload.")
        
    elif image != "None":
        data = {'metadata': {'title': f'{title}',
                             'description': f'{description}',
                             'publication_date': f'{publication_date}',
                             'upload_type': f'{upload}',
                             'image_type': f'{image}',
                             'creators': creators}}
    
        print("The metadata has been stored.\n"
              "You can always change it in Zenodo's website after you upload.")
        
    else: 
        data = {'metadata': {'title': f'{title}',
                             'description': f'{description}',
                             'publication_date': f'{publication_date}',
                             'upload_type': f'{upload}',
                             'creators': creators}}
        
        print("The metadata has been stored.\n"
              "You can always change it in Zenodo's website after you upload.\n")
        
    return data 

# Dataframe from the metadata
def print_md(data):
    import pandas as pd
    df = pd.DataFrame.from_dict(data['metadata'], orient='index', columns=["Metadata"])
    return df




















