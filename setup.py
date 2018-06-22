from distutils.core import setup

setup(name='SlothD3MWrapper',
    version='1.0.0',
    description='A thin wrapper for interacting with New Knowledge time series tool library Sloth',
    packages=['SlothD3MWrapper'],
    install_requires=["typing",
        "Sloth==1.0.0"],
    dependency_links=[
        "git+https://github.com/NewKnowledge/sloth@18c5f76939ae355e46c83a71117687076b7a5734#egg=Sloth-1.0.0"
    ],
    entry_points = {
        'd3m.primitives': [
            'distil.Sloth.cluster = SlothD3MWrapper:Storc'
        ],
    },
)