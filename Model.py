import pickle
def model_pkl():
    try:
        with open("https://colab.research.google.com/drive/10HxPEArtAbUjJAwV4IPYn-xZIxiWK33i?usp=share_link") as pickl:
            model_pk=pickle.read(pickl)
    except FileNotFoundError:
        print("file not found")
    finally:
        return model_pk