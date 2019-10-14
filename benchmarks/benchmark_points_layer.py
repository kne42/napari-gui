# See "Writing benchmarks" in the asv docs for more information.
# https://asv.readthedocs.io/en/latest/writing_benchmarks.html
# or the napari documentation on benchmarking
# https://github.com/napari/napari/blob/master/BENCHMARKS.md
import numpy as np
from napari.layers import Points


class Points2DSuite:
    """Benchmarks for the Points layer with 2D data"""

    params = [2 ** i for i in range(4, 18, 2)]

    def setup(self, n):
        np.random.seed(0)
        self.data = np.random.random((n, 2))
        self.layer = Points(self.data)

    def time_create_layer(self, n):
        """Time to create layer."""
        layer = Points(self.data)

    def time_set_view_slice(self, n):
        """Time to set view slice."""
        self.layer._set_view_slice()

    def time_update_thumbnail(self, n):
        """Time to update thumbnail."""
        self.layer._update_thumbnail()

    def time_get_value(self, n):
        """Time to get current value."""
        self.layer.get_value()

    def mem_layer(self, n):
        """Memory used by layer."""
        return self.layer

    def mem_data(self, n):
        """Memory used by raw data."""
        return self.data


class Points3DSuite:
    """Benchmarks for the Points layer with 3D data."""

    params = [2 ** i for i in range(4, 18, 2)]

    def setup(self, n):
        np.random.seed(0)
        self.data = np.random.random((n, 3))
        self.layer = Points(self.data)

    def time_create_layer(self, n):
        """Time to create layer."""
        layer = Points(self.data)

    def time_set_view_slice(self, n):
        """Time to set view slice."""
        self.layer._set_view_slice()

    def time_update_thumbnail(self, n):
        """Time to update thumbnail."""
        self.layer._update_thumbnail()

    def time_get_value(self, n):
        """Time to get current value."""
        self.layer.get_value()

    def mem_layer(self, n):
        """Memory used by layer."""
        return self.layer

    def mem_data(self, n):
        """Memory used by raw data."""
        return self.data
