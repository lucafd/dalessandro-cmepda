# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Luca Baldini (luca.baldini@pi.infn.it)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Unit test for the pdf.
"""

import unittest
import sys

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
if sys.flags.interactive: # questo è quello che dice che devo runnare in modalità interattiva
    plt.ion()

from splrand.pdf import ProbabilityDensityFunction

class TestPdf(unittest.TestCase):
    """
    """

    def test_uniform(self):
        """
        """
        x = np.linspace(0., 1., 100)
        y = np.full(x.shape, 1.)
        pdf = ProbabilityDensityFunction(x, y)
        self.assertAlmostEqual(pdf(0.5), 1.) # primo vero test, perché almost equal
        self.assertAlmostEqual(pdf.integral(0., 1.), 1.) # integral viene dalla spline
        self.assertAlmostEqual(pdf.prob(0.25, 0.75), 0.5)
        # andiamo a vedere interfaccia per interfaccia per verificare che sia così
        # plt.plot(x, y) 
        # non fa nulla se faccio il test, ma se tira fuori un plot in teoria ferma tutto, quindi in realtà non fa nulla: per lanciarlo l'opzione è -i interactive.
    
    def test_triangular(self):
        x = np.linspace(0., 1., 100)
        y = 2. * x
        pdf = ProbabilityDensityFunction(x, y)
        # qua ha plottato la pdf, la pdf.cdf, la pdf.ppf e torna
        # qua invece?
        r = pdf.rnd(1000000)
        plt.hist(r, bins=20) # questo lo plotta.
    
    # qua qualcosa di sportivo e magic
    def test_fancy(self):
        """
        """
        x = np.linspace(0., 1., 100)
        y = np.zeros(x.shape)
        y[x <= 0.5] = 2. * x[x <= 0.5]
        y[x > 0.75] = 3.
        pdf = ProbabilityDensityFunction(x, y)
        plt.figure('Fancy pdf')
        xgrid = np.linspace(0., 1., 1000)
        plt.plot(xgrid, pdf(xgrid))
        print(pdf.integral(0., 1.))
        # now we plot cdf and ppf
        plt.plot(xgrid, pdf.cdf(xgrid))
        plt.plot(xgrid, pdf.ppf(xgrid))
        # TODO dare un occhiata a questa cosa meglio, e si possono generare numeri random

if __name__ == '__main__':
    unittest.main(exit=not sys.flags.interactive)