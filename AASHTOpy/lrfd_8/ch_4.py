import math

def eq4623d1(L1, W1):
    """Eq. 4.6.2.3-1: Equivalent strip width for one lane.

    The equivalent width of longitudinal strips per lane
    for both shear and moment with one lane, i.e., two lines
    of wheels, loaded my be dtermined as
    
        E = 10.0 + 5.0 * math.sqrt(L1 * W1)

    Commentary:
    The strip width has been divided by 1.20 to account for
    the multiple presence effect.

    Args:
        L1 (float): modified span length taken equal to the lesser
                    of the actual span or 60.0, (ft)

        W1 (float): modified edge-to-edge width of bridge taken to
                    be equal to the lesser of the actual width or 60.0
                    for multilane loading, or 30.0 for single-lane
                    loading, (ft)

    Returns:
        E (tuple(float, str)): 
            equivalent width, (in.); formatted text output of equation
            with values substituted into equation and the final calculated
            value

    """

    E = 10.0 + 5.0 * math.sqrt(L1 * W1)

    text = (f'E = 10.0 + 5.0 * math.sqrt(L1 * W1) \n' +
            f'E = 10.0 + 5.0 * math.sqrt({L1:.3f} * {W1:.3f})\n' + 
            f'E = {10.0 + 5.0 * math.sqrt(L1 * W1):.3f}')

    return E, text

def eq4623d2(L1, W1, W, NL):
    """Eq. 4.6.2.3-2: Equivalent strip width for two lanes.

    The equivalent width of lingitudinals strips per lane
    for both shear and moment with more than one lane
    loaded may be determined as
    
        E = min(84.0 + 1.44*math.sqrt(L1*W1), (12.0*W)/NL)

    Args:
        L1 (float): modified span length taken equal to the lesser
                    of the actual span or 60.0, (ft)

        W1 (float): modified edge-to-edge width of bridge taken to
                    be equal to the lesser of the actual width or 60.0
                    for multilane loading, or 30.0 for single-lane
                    loading, (ft)

        W (float): physical edge-to-edge width of bridge, (ft)

        NL (float): number of design lanes as specified in
                    Article 3.6.1.1.1

    Returns:
        E (tuple(float, str)): 
            equivalent width, (in.); formatted text output of equation
            with values substituted into equation and the final calculated
            value

    """
    NL = math.floor(NL)

    E = min(84.0 + 1.44*math.sqrt(L1*W1), (12.0*W)/NL)

    text = (f'E = min(84.0 + 1.44*math.sqrt(L1*W1), (12.0*W)/NL)\n' +
            f'E = min(84.0 + 1.44 * math.sqrt({L1:.3f} * {W1:.3f}), ' +
            f'(12.0*{W:.3f})/{NL:.0f})\n' + 
            f'E = {min(84.0 + 1.44 * math.sqrt(L1 * W1), (12.0*W)/NL):.3f}')

    return E, text
