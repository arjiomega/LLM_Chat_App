from setuptools import setup, find_packages

setup(
    name='ph_travel_chatbot',  # Replace with your project name
    version='0.1.0',  # Replace with your version
    packages=find_packages(where='src'),
    package_dir={'': 'src'},  # Tells setuptools where to find the packages
    install_requires=[
        'streamlit==1.39.0',
        'openai==1.52.0',
        'beautifulsoup4==4.12.3',
        'scikit-learn==1.5.2',
        'langchain',
        'langchain_community',
    ],
    python_requires='>=3.12.5',  # Ensuring compatibility with Python 3.12.5
    classifiers=[
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Change to your project's license
        'Operating System :: OS Independent',
    ],
    # You can include additional metadata like author, description, etc.
    author='Richard Joseph Omega',
    author_email='richardjoseph.omega@gmail.com',
    description='',
    long_description='',
    long_description_content_type='text/markdown',  # Assuming your README is in markdown
    url='https://github.com/arjiomega/LLM_Chat_App',  # Replace with your project URL
)
