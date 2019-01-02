from distutils.core import setup

setup(name='SlothD3MWrapper',
    version='2.0.1',
    description='A thin wrapper for interacting with New Knowledge time series tool library Sloth',
    packages=['SlothD3MWrapper'],
    install_requires=["typing",
        "Sloth==2.0.2"],
    dependency_links=[
        "git+https://github.com/NewKnowledge/sloth@4a4c8d3e22fec9a995dbcf7a065aa63f35bcec0f#egg=Sloth-2.0.2"
    ],
    entry_points = {
        'd3m.primitives': [
            'distil.Sloth.cluster = SlothD3MWrapper:Storc'
        ],
    },
)