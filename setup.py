from distutils.core import setup

setup(name='SlothD3MWrapper',
    version='2.0.0',
    description='A thin wrapper for interacting with New Knowledge time series tool library Sloth',
    packages=['SlothD3MWrapper'],
    install_requires=["typing",
        "Sloth==2.0.0"],
    dependency_links=[
        "git+https://github.com/NewKnowledge/sloth@c2e550cb9d1417a1e59480018163a6167d1926c6#egg=Sloth-2.0.0"
    ],
    entry_points = {
        'd3m.primitives': [
            'distil.Sloth.cluster = SlothD3MWrapper:Storc'
        ],
    },
)