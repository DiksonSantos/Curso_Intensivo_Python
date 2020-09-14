from collections import OrderedDict



favorite_languages = OrderedDict()

favorite_languages['jen'] = 'delphi'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = "fortran"
favorite_languages["dikson"] = 'python-3'

for name, language in favorite_languages.items():
    print(name.upper() + " " + " Sua Linguagem Favorita é: " +
          language.title() + ".")
