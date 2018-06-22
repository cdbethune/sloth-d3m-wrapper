from distutils.core import setup

setup(name='SlothD3MWrapper',
    version='1.0.0',
    description='A thin wrapper for interacting with New Knowledge time series tool library Sloth',
    packages=['SlothD3MWrapper'],
    install_requires=["typing",
        "Sloth==1.0.0"],
    dependency_links=[
        "git+https://github.com/NewKnowledge/sloth@caf91db91b79c4bcc07763faad7f38eb2ebf0b46#egg=Sloth-1.0.0"
    ],
    entry_points = {
        'd3m.primitives': [
            'distil.Sloth.cluster = SlothD3MWrapper:Storc'
        ],
    },
)