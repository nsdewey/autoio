""" Read useful information from the output file
"""

import ioformat
import autoparse.find as apf
import autoparse.pattern as app


def internal_coordinates(output_str):
    """ Read the internal coordinates defined in output.

        Coordinates returned as a list where each entry is
        (type, (idxs,)) where type is STRE, BEND, TORS, etc and
        idxs correspond to the atom indices of a Cartesian
        geometry associated with the internal coordinates.

        :param output_str: string the INTDER output file
        :type output_str: str
        :rtype: tuple(tuple(str, tuple(int)))
    """

    begin_ptt = 'DEFINITION OF INTERNAL COORDINATES'
    end_ptt = 'VALUES OF SIMPLE INTERNAL COORDINATES'
    block_ptt = app.block_pattern(begin_ptt, end_ptt)
    block = apf.last_capture(block_ptt, output_str)

    if block is not None:
        block = ioformat.remove_whitespace_from_string(block)

        intl_coords = ()
        for line in block.splitlines()[1:]:
            tmp = line.strip().split('=')[1]
            tmp2 = tmp.split()
            # Get the coord typ and idxs
            # only get non-zero idxs as zeros correspond to no atoms
            typ = tmp2[0]
            idxs = tuple(int(val) for val in tmp2[1:])
            idxs = tuple(val-1 for val in idxs if val > 0)

            intl_coords += ((typ, idxs),)
    else:
        intl_coords = None

    return intl_coords


def ted_assignments(output_str):
    """ Parse the TED assignments to each vibrational mode which include
        the vibrational frequency as well as the index of the internal
        coordinates that make up the mode. For each internal coordinate,
        the percentage of contribution to the vibrational mode is also
        returned.

        The output is a tuple for each mode given as (freq, {idx: percentage})
        where freq is in cm-1 and the percentage is given in N%.

        :param output_str: string the INTDER output file
        :type output_str: str
        :rtype: tuple(tuple(float, dict[int: float]))
    """

    # Block patterns
    begin_ptt = 'DOMINANT COMPONENTS OF TED'
    end_ptt = 'NORMAL MODE ANALYSIS IN CARTESIAN COORDINATES'
    block_ptt = app.block_pattern(begin_ptt, end_ptt)
    block = apf.last_capture(block_ptt, output_str)

    # Other patterns
    pct_ptt = app.block_pattern(app.escape('('), app.escape(')'))
    coord_ptt = app.INTEGER + app.SPACE + app.escape('(')

    if block is not None:
        block = ioformat.remove_whitespace_from_string(block)

        # Parse line for mode info
        freqs, idxs_lst, pcts_lst = (), (), ()
        for line in block.splitlines():
            # Get the mod frequency
            freq = float(line.split()[1])
            freqs += (freq,)
            # Get the idx numbers of coordinates comprising mode (in 0-index)
            idxs = apf.all_captures(coord_ptt, line)
            idxs = tuple(int(val.replace(' (', ''))-1 for val in idxs)
            idxs_lst += (idxs,)
            # Get the percentages of coordinates comprising mode
            pcts = apf.all_captures(pct_ptt, line)
            pcts = tuple(float(val.strip()) for val in pcts)
            pcts_lst += (pcts,)

        # Build the TED list
        ted = ()
        for freq, idxs, pcts in zip(freqs, idxs_lst, pcts_lst):
            ted += ((freq, dict(zip(idxs, pcts))),)
    else:
        ted = None

    return ted
