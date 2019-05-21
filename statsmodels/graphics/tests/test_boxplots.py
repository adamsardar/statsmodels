import numpy as np
import pytest

from statsmodels.graphics.boxplots import violinplot, beanplot
from statsmodels.datasets import anes96

try:
    import matplotlib.pyplot as plt
except ImportError:  # pragma: no cover
    pass


@pytest.mark.matplotlib
def test_violinplot_beanplot(close_figures):
    # Test violinplot and beanplot with the same dataset.
    data = anes96.load_pandas()
    party_ID = np.arange(7)
    labels = ["Strong Democrat", "Weak Democrat", "Independent-Democrat",
              "Independent-Independent", "Independent-Republican",
              "Weak Republican", "Strong Republican"]

    age = [data.exog['age'][data.endog == id] for id in party_ID]

    fig = plt.figure()
    ax = fig.add_subplot(111)
    violinplot(age, ax=ax, labels=labels,
               plot_opts={'cutoff_val':5, 'cutoff_type':'abs',
                          'label_fontsize':'small',
                          'label_rotation':30})

    fig = plt.figure()
    ax = fig.add_subplot(111)
    violinplot(age, ax=ax, labels=labels,
               plot_opts={'cutoff_val':5, 'cutoff_type':'abs',
                          'label_fontsize':'small',
                          'label_rotation':30,
                          'bw_factor':.2})

    fig = plt.figure()
    ax = fig.add_subplot(111)
    beanplot(age, ax=ax, labels=labels,
             plot_opts={'cutoff_val':5, 'cutoff_type':'abs',
                        'label_fontsize':'small',
                        'label_rotation':30})

    fig = plt.figure()
    ax = fig.add_subplot(111)
    beanplot(age, ax=ax, labels=labels, jitter=True,
             plot_opts={'cutoff_val': 5, 'cutoff_type': 'abs',
                        'label_fontsize': 'small',
                        'label_rotation': 30})

    fig = plt.figure()
    ax = fig.add_subplot(111)
    beanplot(age, ax=ax, labels=labels, jitter=True, side='right',
             plot_opts={'cutoff_val': 5, 'cutoff_type': 'abs',
                        'label_fontsize': 'small',
                        'label_rotation': 30})

    fig = plt.figure()
    ax = fig.add_subplot(111)
    beanplot(age, ax=ax, labels=labels, jitter=True, side='left',
             plot_opts={'cutoff_val': 5, 'cutoff_type': 'abs',
                        'label_fontsize': 'small',
                        'label_rotation': 30})

    fig = plt.figure()
    ax = fig.add_subplot(111)
    beanplot(age, ax=ax, labels=labels,
             plot_opts={'bean_legend_text': 'text'})
