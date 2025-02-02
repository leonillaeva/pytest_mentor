import yaml

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

if __name__ == '__main__':

    stream = open("simple_file_tutorial_1.yml", 'r')
    dictionary = yaml.load(stream, Loader)
    for key, value in dictionary.items():
        print(key + " : " + str(value))

    stream.close()
