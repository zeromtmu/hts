# (C) 2015 Elke Schaper

"""
    :synopsis: The Readout Class.

    .. moduleauthor:: Elke Schaper <elke.schaper@isb-sib.ch>
"""

import itertools
import logging
import numpy as np
import os
import pickle
import re
from string import ascii_lowercase, ascii_uppercase


LOG = logging.getLogger(__name__)




class Readout(plate_data.PlateData):

    """ ``Readout`` describes one plate matrix

    Attributes:
        width (int): Width of the plate
        height (int): Height of the plate
        data (np.array of np.arrays): A matrix of plate values
        axes (dict of list): The naming of the two axes of the plates (e.g. {"x": ["A", "B", ...], "y": [1, 2, 3, 4, ...]})


    """

    def __str__(self):
        """
            Create string for Readout instance.
        """
        try:
            data = ("<Readout instance>\nContains a numpy array of arrays."
                    "\nwidth: {}\nheight: {}".format(self.width, self.height))
        except:
            data = "<Readout instance>"
            LOG.warning("Could not create string of Readout instance.")

        return data


    def __init__(self, data, **kwargs):

        # Run super __init__
        super(PlateLayout, self).__init__()

        # Perform PlateLayout specific __init__

        # This is what you've originally done- what should you do with it now?
        # Convert all data to floats
        #self.data = np.array([np.array([float(read) if read else np.nan for read in column]) for column in data])



    def filter_wells(self, starting_tag = "neg"):
        """
            Return all values of wells that start with ``starting_tag`` in the
            plate_data as a np.array
        """
        if not hasattr(self, "plate_data"):
            raise Exception('Readout does not have a plate_data attribute')
        else:
            filter_result = []
            for i_height,i_width in itertools.product(range(self.height), range(self.width)):
                if self.plate_layout.layout[i_height][i_width].startswith(starting_tag):
                    filter_result.append(self.data[i_height][i_width])
        return filter_result


    def min(self):
        """
            Return the min of all values
        """
        return self.data.min()


    def max(self):
        """
            Return the max of all values
        """
        return self.data.max()


    def set_plate_layout(self, plate_layout):
        self.plate_layout = plate_layout


    def write(self, format, path=None, return_string=None, *args):
        """ Serialize and write ``Readout`` instances.

        Serialize ``Readout`` instance using the stated ``format``.

        Args:
            format (str):  The output format: Currently only "pickle".
            path (str): Path to output file

        .. todo:: Write checks for ``format`` and ``path``.
        """

        if format == 'pickle':
            with open(file, 'wb') as fh:
                pickle.dump(self, fh)
        else:
            raise Exception('Format is unknown: {}'.format(format))

        if path:
            with open(path, 'w') as fh:
                fh.write(output)
        if return_string:
            return output

