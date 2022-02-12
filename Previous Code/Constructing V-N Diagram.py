from ADRpy import airworthiness as aw
from ADRpy import unitconversions as co
from ADRpy import atmospheres as at

"""The Flight Envelope of a Fixed Wing Aircraft"""


designbrief = {}

designdef = {'aspectratio': 11.1, 'wingarea_m2': 12.1, 'weight_n': 5872}

designperf = {'CLmaxclean': 1.45, 'CLminclean': -1, 'CLslope': 6.28}

designpropulsion = "piston"

designatm = at.Atmosphere()

csbrief={'cruisespeed_keas': 107, 'divespeed_keas': 150,
         'altitude_m': 0,
         'weightfraction': 1, 'certcat': 'norm'}

concept = aw.CertificationSpecifications(designbrief, designdef, designperf, designatm, designpropulsion, csbrief)

points = concept.flightenvelope(textsize=15, figsize_in=[15, 10], show=True)



"""Twin turboprop commuter"""

# designbrief = {}

designdef = {'aspectratio': 10.48, 'wingarea_m2': co.feet22m2(310), 'weight_n': co.lbf2n(17120)}

designperf = {'CLmaxclean': 1.6, 'CLminclean': -1, 'CLslope': 6.28}

designpropulsion = "turboprop"

designatm = at.Atmosphere()  # set the design atmosphere to a zero-offset ISA

# Max operating speed: 248KIAS up to 13,200ft, M0.48 above (at 20,000ft M0.48 = 293KTAS = 214KEAS)
csbrief = {'cruisespeed_keas': 204, 'divespeed_keas': 248,
           'altitude_m': co.feet2m(0),
           'weightfraction': 0.7, 'certcat': 'comm'}

Beech1900Dspec = aw.CertificationSpecifications(designbrief, designdef, designperf, designatm, designpropulsion, csbrief)

points = Beech1900Dspec.flightenvelope(textsize=15, figsize_in=[15, 10], show=True)


