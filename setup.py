from setuptools import setup

setup(
    name="gomind_web_browser",
    python_requires=">=3.6",
    version="0.0.0",
    description="GoMind web browser functions",
    url="https://github.com/GrupoDomini/gomind_web_browser.git",
    author="JeffersonCarvalhoGD",
    author_email="jefferson.carvalho@grupodomini.com",
    license="unlicense",
    packages=["gomind_web_browser"],
    zip_safe=False,
    install_requires=["selenium", "webdriver_manager"],
)
