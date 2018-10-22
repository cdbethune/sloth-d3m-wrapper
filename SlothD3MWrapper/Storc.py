import sys
import os.path
import numpy as np
import pandas
import typing
from json import JSONDecoder
from typing import List

from Sloth import Sloth

from d3m.primitive_interfaces.base import PrimitiveBase, CallResult

from d3m import container, utils
from d3m.metadata import hyperparams, base as metadata_base, params

__author__ = 'Distil'
__version__ = '2.0.0'

Inputs = container.pandas.DataFrame
Outputs = container.pandas.DataFrame

class Params(params.Params):
    pass


class Hyperparams(hyperparams.Hyperparams):
    nclusters = hyperparams.UniformInt(lower=1, upper=sys.maxsize, default=3, semantic_types=[
        'https://metadata.datadrivendiscovery.org/types/TuningParameter'
    ])
    pass

class Storc(PrimitiveBase[Inputs, Outputs, Params, Hyperparams]):
    metadata = metadata_base.PrimitiveMetadata({
        # Simply an UUID generated once and fixed forever. Generated using "uuid.uuid4()".
        'id': "77bf4b92-2faa-3e38-bb7e-804131243a7f",
        'version': __version__,
        'name': "Sloth",
        # Keywords do not have a controlled vocabulary. Authors can put here whatever they find suitable.
        'keywords': ['Time Series','Clustering'],
        'source': {
            'name': __author__,
            'uris': [
                # Unstructured URIs.
                "https://github.com/NewKnowledge/sloth-d3m-wrapper",
            ],
        },
        # A list of dependencies in order. These can be Python packages, system packages, or Docker images.
        # Of course Python packages can also have their own dependencies, but sometimes it is necessary to
        # install a Python package first to be even able to run setup.py of another package. Or you have
        # a dependency which is not on PyPi.
         'installation': [{
            'type': metadata_base.PrimitiveInstallationType.PIP,
            'package': 'cython',
            'version': '0.28.5',
            ),
        },{
            'type': metadata_base.PrimitiveInstallationType.PIP,
            'package_uri': 'git+https://github.com/NewKnowledge/sloth-d3m-wrapper.git@{git_commit}#egg=SlothD3MWrapper'.format(
                git_commit=utils.current_git_commit(os.path.dirname(__file__)),
            ),
        }],
        # The same path the primitive is registered with entry points in setup.py.
        'python_path': 'd3m.primitives.distil.Sloth.cluster',
        # Choose these from a controlled vocabulary in the schema. If anything is missing which would
        # best describe the primitive, make a merge request.
        'algorithm_types': [
            metadata_base.PrimitiveAlgorithmType.SPECTRAL_CLUSTERING,
        ],
        'primitive_family': metadata_base.PrimitiveFamily.TIME_SERIES_SEGMENTATION,
    })

    def __init__(self, *, hyperparams: Hyperparams, random_seed: int = 0)-> None:
        super().__init__(hyperparams=hyperparams, random_seed=random_seed)

        self._decoder = JSONDecoder()
        self._params = {}

    def fit(self) -> None:
        pass

    def get_params(self) -> Params:
        return self._params

    def set_params(self, *, params: Params) -> None:
        self.params = params

    def set_training_data(self, *, inputs: Inputs, outputs: Outputs) -> None:
        pass

    def produce(self, *, inputs: Inputs, timeout: float = None, iterations: int = None) -> CallResult[Outputs]:
        """
        Produce primitive's best guess for the structural type of each input column.

        Parameters
        ----------
        inputs : Input pandas frame where each row is a series.  Series timestamps are store in the column names.

        Returns
        -------
        Outputs
            The output is a dataframe containing a single column where each entry is the associated series' cluster number.
        """
        # setup model up
        sloth = Sloth()

        # set number of clusters for k-means
        nclusters = self.hyperparams['nclusters']

        labels = sloth.ClusterSeriesKMeans(inputs.values, nclusters)
        return CallResult(pandas.DataFrame(labels))


if __name__ == '__main__':
    client = Storc(hyperparams={'nclusters':6})
    frame = pandas.read_csv("path/csv_containing_one_series_per_row.csv",dtype=str)
    result = client.produce(inputs = frame)
    print(result)