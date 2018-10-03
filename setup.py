from distutils.core import setup

setup(name='SlothD3MWrapper',
    version='2.0.0',
    description='A thin wrapper for interacting with New Knowledge time series tool library Sloth',
    packages=['SlothD3MWrapper'],
    install_requires=["typing",
        "Sloth==2.0.0"],
    dependency_links=[
        "git+https://github.com/NewKnowledge/sloth@d38b8892fbefb4425d211d2cd858cfad91a2113e#egg=Sloth-2.0.0"
    ],
    entry_points = {
        'd3m.primitives': [
            'distil.Sloth.cluster = SlothD3MWrapper:Storc'
        ],
    },
)