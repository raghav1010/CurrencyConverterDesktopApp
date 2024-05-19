<p align="center">
  <img src="cov.png" width="400" alt="logo"/>
</p>

---

![Python](https://img.shields.io/badge/-Python-black?style=for-the-badge&logoColor=white&logo=Python&color=2F73BF)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)


## 📋 Table of Contents

1. 🤔 [What is this CurrencyConvertor?](#what-is-this-currency-convertor)
2. 🔨 [Installation](#installation)
3. 🚀 [Getting Started](#getting-started)
4. 👨‍💻 [Build](#build-the-app)
5. ©️ [License](#license)
6. ❤️ [Contributors](#contributors)


## <a name="what-is-this-currency-convertor">🤔 What is this Currency Convertor ?</a>
A desktop application build on top of a Python **Eel** framework, web scrapping script to extract data using foreign exchange rates API. The front end is designed in HTML CSS .

## <a name="installation">🔨 Installation</a>

To install this project, you will need to have on your machine :

![Python](https://img.shields.io/badge/-Python-black?style=for-the-badge&logoColor=white&logo=Python&color=2F73BF)

Install pip for virtual environment management: https://pip.pypa.io/en/stable/getting-started/

## <a name="getting-started"> 🚀 Getting Started</a>
- Clone the repo and cd into the directory:

```sh
$ git clone git@github.com:raghav1010/CurrencyConverterDesktopApp.git
$ cd CurrencyConverterDesktopApp
```

- Setup virtualenv and install requirements:

```sh
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

- Run the app

```sh
$ python3 cur.py
```

## <a name="build-the-app"> 👨‍💻  Build</a>
You can pass any valid `pyinstaller`  flag in the following command to further customize the way your app is built.
```sh
$ python3 -m eel cur.py web --noconsole --onefile --icon=static/icon.icns
```

## <a name="license">©️ License</a>

This project is licensed under the [MIT License](http://opensource.org/licenses/MIT).

## <a name="contributors">❤️ Contributors</a>

There is no contributor yet. Want to be the first ?