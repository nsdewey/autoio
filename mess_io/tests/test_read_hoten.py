""" test mess_io.reader.hoten
"""

import os
import numpy as np
from ioformat import pathtools
import mess_io


PATH = os.path.dirname(os.path.realpath(__file__))
IPATH = os.path.join(PATH, 'data', 'inp')
OPATH = os.path.join(PATH, 'data', 'out')
HOT_INP_SGL = pathtools.read_file(IPATH, 'me_ktp_hoten_ch2o_oh.inp')
HOT_LOG_SGL = pathtools.read_file(OPATH, 'me_ktp_hoten_ch2o_oh.logf')
HOT_INP_DBL = pathtools.read_file(IPATH, 'me_ktp_hoten_c3h7.inp')
HOT_LOG_DBL = pathtools.read_file(OPATH, 'me_ktp_hoten_c3h7.logf')


def test_get_hot_species():
    """ test mess_io.read.get_hot_species
    """
    assert mess_io.reader.hoten.get_hot_species(HOT_INP_SGL) == {
        'W1': 0.0}
    assert mess_io.reader.hoten.get_hot_species(HOT_INP_DBL) == {
        'CH3CH2CH2': 3.19, 'CH3CHCH3': 0.0}


def test_extract_hot_branching():
    """ test mess_io.read.extract_hot_branching
    """
    hotspecies_en = {'W1': 0.0}
    species_lst = ('W1', 'CO+H')
    hoten_branch_dct = mess_io.reader.hoten.extract_hot_branching(
        HOT_LOG_SGL, hotspecies_en, species_lst, filter=True)
    hoten = hoten_branch_dct['W1']
    assert np.allclose(hoten[3.16][1200].iloc[0].values,
                       np.array([0, 1]))
    assert np.allclose(hoten[3.16][1200].iloc[-1].values,
                       np.array([1, 0]))
    assert np.allclose(hoten[3.16][1200].loc[21.0].values,
                       np.array([0.000075, 0.999925]), atol=1e-5)

    hotspecies_en = {'CH3CH2CH2': 3.19, 'CH3CHCH3': 0.0}
    species_lst = ('CH3CH2CH2', 'CH3CHCH3', 'C2H4+CH3', 'CH3CHCH2+H')
    hoten_branch_dct = mess_io.reader.hoten.extract_hot_branching(
        HOT_LOG_DBL, hotspecies_en, species_lst, filter=True)
    hoten = hoten_branch_dct['CH3CHCH3']
    assert np.allclose(hoten[100][1800].iloc[0].values,
                       np.array([2.27908435e-08, 1.73930121e-06, 5.13793577e-02, 9.48618880e-01]),
                       atol=1e-5)
    assert np.allclose(hoten[100][1800].iloc[-1].values,
                       np.array([2.15953354e-04, 9.99784047e-01,
                                 0.00000000e+00, 0.00000000e+00]),
                       atol=3e-4) # seems large but bf above is almost 1
    assert np.allclose(hoten[100][1800].loc[91.4].values,
                       np.array([0.002120,  0.441947,  0.011999,    0.543935]),
                       atol=1e-5)

def test_extract_fne():

    dct_bf_tp_df = mess_io.reader.hoten.extract_fne(HOT_LOG_SGL)
    
    assert np.allclose((dct_bf_tp_df['W1'][0.1][1000]).values,
                       np.array([0.98928607, 0.01071393]))

    dct_bf_tp_df = mess_io.reader.hoten.extract_fne(HOT_LOG_DBL)

    assert np.allclose((dct_bf_tp_df['CH3CH2CH2'][0.1][1000]).values,
                       np.array([9.91380043e-01, 6.53250422e-07, 8.51326353e-03, 1.06040650e-04]))
    assert np.allclose((dct_bf_tp_df['CH3CHCH3'][0.1][1000]).values,
                       np.array([2.21902815e-07, 9.99562230e-01, 1.73923828e-06, 4.35809132e-04]))

if __name__ == '__main__':
    test_get_hot_species()
    test_extract_fne()
    test_extract_hot_branching()
