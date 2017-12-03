#!/usr/bin/env python3

import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
from canvas import Canvas
import os

def vr_jet(pt, rho=30):
    return np.clip(rho / pt, 0.02, 0.4)
def ftag_cone(pt):
    pt_mev = pt * 1e3
    return 0.239 + np.exp(-1.22 - 1.64e-5 * pt_mev)
def track_jet(pt):
    return np.full(pt.shape, 0.2)
def label(pt):
    return np.full(pt.shape, 0.3)

def line(ax, xval, words, color='purple'):
    ax.axvline(xval, color=color)
    arrowprops=dict(arrowstyle='->', color=color)
    ax.annotate(words, (xval, 0.1), (20, 0.0), textcoords='offset points',
                color=color, arrowprops=arrowprops)
    return
    bbox=dict(facecolor='none', edgecolor='red')
    ax.text(xval, 0.1, words, ha='right', va='bottom', rotation=90,
            color='purple', bbox=bbox)

def draw(odir, name, jet_pt=[400, 40]):
    low, high = 10, 2000
    pt = np.logspace(np.log10(low), np.log10(high), 250+1)
    if not os.path.isdir(odir):
        os.mkdir(odir)
    with Canvas(f'{odir}/{name}') as can:
        can.ax.plot(pt, label(pt), color='blue', label='FTag Label Cone')
        can.ax.plot(pt, ftag_cone(pt), '-', color='darkgreen', label="Track Association Cone")
        can.ax.plot(pt, vr_jet(pt), '-r', label=r"VR Jet ($\rho = 30$ GeV)")
        can.ax.plot(pt, track_jet(pt), linestyle='--', color='orange', label=r'Track Jet ($R = 0.2$)')
        can.ax.legend(framealpha=1)
        can.ax.set_ylabel(r'$R$ or $\Delta R$')
        can.ax.set_xlabel(r'jet $p_{\rm T}$ [GeV]')
        can.ax.set_xlim(10, high)
        can.ax.set_ylim(0, 0.6)
        can.ax.set_xscale('log')
        for num, pt in enumerate(jet_pt, 1):
            line(can.ax, pt, f'Jet {num}\n{pt} GeV')

def run():
    draw('figures', 'radii-vs-pt.pdf', jet_pt=[])
    draw('figures', 'radii-vs-pt-jets.pdf')

if __name__ == '__main__':
    run()
