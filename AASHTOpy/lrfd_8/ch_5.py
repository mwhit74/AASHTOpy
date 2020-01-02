import math

def eq56322d1(Aps=0.0, fps=0.0, dp=0.0, aps=0.0, As1=0.0, fs1=0.0, d1=0.0,
              a1=0.0, As2=0.0, fs2=0.0, d2=0.0, a2=0.0, alpha_1=0.0, 
              fcp=0.0, b=0.0, bw=0.0, hf=0.0, a3=0.0):
    """Eq. 5.6.3.2.2-1: Moment capacity equation based on Whitney stress block
    
    For flanged section subject to flexture about one axis and for biaxial
    flexure with axial load as specified in Article 5.6.4.5, where the
    approximate stress distribution specified in Article 5.6.2.2 is used and
    where the compression flange depth is lass than a = beta_1 * c, as 
    determined in accordance with Eqs. 5.6.3.1.1-3, 5.6.3.1.1-4, 5.6.3.1.2-3,
    or 5.6.3.1.2-4, the nominal flexure resistance may be taken as:
        
        Mn = Aps*fps*(dp-aps/2)+As1*fs1*(d1-a1/2)-As2*fs2*(d2-a2/2)+
              alpha_1*fcp*(b-b_w)*hf*(a2/2-hf/2)
    
    Args:
        Aps (float): 
            area of prestressing steel, (in^2)
            
        fps (float): 
            average stress in prestressing steel at nominal bending resistance
            specified in Eq. 5.6.3.1.1-1 (ksi)
            
        dp (float): 
            distance from extreme compresion fiber to the centroid of 
            prestressing steel, (in.)
            
        aps (float): 
            c*beta_1, depth of equivalent stress block, (in.), for the 
            prestressing steel
            
        As1 (float): 
            area of nonprestressed tension reinforcement, (in^2)
            
        fs1 (float): 
            stress in the nonprestressed tension reinforcement at nominal
            flexural resistance, (ksi), as specified in Article 5.6.2.1
            
        d1 (float): 
            distance from extreme compression fiber to the centroid of the
            nonprestressed tensile reinforcement, (in.)
            
        a1 (float):
            c*beta_1, depth of equivalent stress block, (in.), for the 
            nonprestress tension reinforcement 
            
        As2 (float): 
            area of nonprestressed compression reinforcement, (in^2)
        
        fs2 (float):
            stress in the nonprestressed compression rinforcment at nominal 
            flexural resistance, (ksi), as specified in Article 5.6.2.1
            
        d2 (float):
            distance from extreme compression fiber to the centroid of the
            compression reinforcement, (in.)
            
        a2 (float): 
            c*beta_1, depth of equivalent stress block, (in.), for the 
            nonprestress tension reinforcement 
            
        fcp (float): 
            design concrete compressive strengt, (ksi)
        
        alpha_1 (float):
            stress block factor specified in Article 5.6.2.2
            
        b (float): 
            width of the compression face of the member; for a flange section
            in compression, the effective width of the flange as specified in 
            Article 4.6.2.6, (in.)
            
        bw (float):
            web width or diameter of a circular section, (in.)
            
        beta_1 (float): 
            stress block factor specified in Article 5.6.2.2
        
        hf (float):
            compression flange depth of an I- or T- member, (in.)
            
    Returns:
        Mn (tuple(float, str)): 
            nominal flexural resistance, (kip-in)
            
    Notes:
        See Article 5.6.3.2.3 - Rectangular Section
        See Article 5.6.3.2.4 - Other Cross-Sections
        
    """
    
    Mn = (Aps*fps*(dp-aps/2)+As1*fs1*(d1-a1/2)-As2*fs2*(d2-a2/2)+
              alpha_1*fcp*(b-b_w)*hf*(a2/2-hf/2))
    
    text = (f'Mn = (Aps*fps*(dp-aps/2)+As1*fs1*(d1-a1/2)-As2*fs2*(d2-a2/2)+' +
            f'alpha_1*fcp*(b-b_w)*hf*(a3/2-hf/2)) \n' +
            f'Mn = {Aps:.2f}*{fps:.2f}*({dp:.2f}-{aps:.2f}/2)+' +
            f'{As1:.2f}*{fs1:.2f}*({d1:.2f}-{a1:.2f}/2)+' +
            f'{As2:.2f}*{fs2:.2f}*({d2:.2f}-{a2:.2f}/2)+' + 
            f'{alpha_1:.2f}*{fcp:.1f}*({b:.2f}-{bw:.2f})*{hf:.2f}*' +
            f'({a2:.2f}/2-{hf:.2f}/2) \n' +
            f'Mn = {Aps*fps*(dp-aps/2)+As1*fs1*(d1-a1/2)-As2*fs2*(d2-a2/2)+' +
            f'alpha_1*fcp*(b-b_w)*hf*(a3/2-hf/2):.2f}')
    
    return Mn, text
    

def eq5424d1(fcp, wc = 0.145, k1 = 1.0):
    """Eq. 5.4.2.4-1: Concrete modulus of elasticity.

    In the absence of measured data, the modulus of elasticity, Ec, for
    normal weight concrete with design compressive strengths up to 15.0
    ksi and lightweight concrete up to 10.0 ksi, with unit weight between
    0.090 and 0.155 kcf, may be taken as: 
        
        Ec = 120000*k1*math.pow(wc,2)*math.pow(fcp, 0.33)

    Args:
        fcp (float): 
            compressive strength of concrete for use in
            design, (ksi)
            
        wc (float, optional): 
            unit weight of conrete, (kcf); refer to Table 3.5.1 or 
            Article C5.4.2.4; defaults to 0.145
            
        k1 (float, optional): 
            correction factor for source of aggregate to be taken as 1.0
            unless determined by physical test, as approved by the owner;
            defaults to 1.0

    Returns:
        Ec (tuple(float, str)): 
            concrete modulus of elasticity, (ksi); formatted text output
            with values substituted into equation and final calculated
            value

    """

    Ec = 120000*k1*math.pow(wc, 2)*math.pow(fcp, 0.33)

    text = (f'Ec = 120,000*kc1*math.pow(wc,2)*math.pow(fcp,0.33)\n' +
            f'Ec = 120,000*{k1:.2f}*math.pow({wc:.3f},2)*' +
            f'math.pow({fcp:.1f},0.33)' + '\n' +
            f'Ec = {120000*k1*math.pow(wc,2)*math.pow(fcp,0.33):.1f}')

    return Ec, text
                               
def eq510821ad1(ldb, lambda_rl, lambda_cf, lambda_rc, lambda_er, lambda_lw):
    """Calculates the modified tension development length.

    The modified tension development length, ld, shall not be less than the
    basic tension develpoment length, ldb, specified herein adjusted by the
    modifiction factor or factors specified in Articles 5.10.8.2.1b and 
    5.10.8.2.1c. The tension development length shall not be less than 12.0
    inches, except for development of shear reinforcement specificed in 
    Article 5.10.8.2.6.

    The modified tension development length, ld, in inches, shall be taken
    as:
        
        ld = ldb * (lambda_rl*lambda_cf*lambda*rc*lambda_er)/lambda_lw

    Modification factors shall be applied to the basic development length
    to account for the various effects specified herein. They shall be
    taken equal to 1.0 unless they are specified to increase ld in 
    Article 5.10.8.2.1b, or to decrease ld in Article 5.10.8.2.1c. 

    Args:
        ldb (float): 
            basic tension development length per Eq 5.10.8.2.1a-2
        
        lambda_rl (float): 
            reinforcement location factor
        
        lambda_cf (float): 
            coating factor
        
        lambda_lw (float): 
            concrete density modification factor as specified in Article
            5.4.2.8
            
        lambda_rc (float): 
            reinforcement confinement factor
        
        lambda_er (float): 
            excess reinforcement factor

    Returns:
        ld (tuple(float, str)):
            modified tension development length, (in.); formatted text 
            output with values substituted into equation and final 
            calculated value

    """

    ld = ldb * (lambda_rl*lambda_cf*lambda_rc*lambda_er)/lambda_lw

#    text = (f'ld = ldb * (lambda_rl*lambda_cf*lambda_rc*lambda_er)\n' +
#            f'/lambda_lw\n' +
#            f'ld = {ldb:.2f} * ({lambda_rl:.2f}*{lambda_cf:.2f}*' +
#            f'{lambda_rc:.2f}*{lambda_er:.2f})/{lambda:.2f}\n' +
#            f'ld = {ld:.2f}')

    return ld, text

def eq510821ad2(db, fy, fcp):
    """Calculates the basic tension development length.

    """


            
