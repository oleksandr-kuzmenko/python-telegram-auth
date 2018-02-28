from setuptools import setup


with open('README.rst') as f:
    long_description = f.read()


setup(
    name='python-telegram-auth',
    version='0.0.1',
    description='Implementation of Telegram authorization for websites',
    long_description=long_description,
    keywords='python telegram auth login',
    url='https://github.com/alxpy/python-telegram-auth',
    author='Oleksandr Kuzmenko',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    py_modules=['python_telegram_auth'],
    python_requires='>=3',
)
